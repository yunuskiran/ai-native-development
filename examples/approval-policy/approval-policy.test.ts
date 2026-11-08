import assert from 'node:assert/strict';
import test from 'node:test';
import { approve, requiredApprovals } from './approval-policy.ts';
import type { AccessRequest, Actor } from './approval-policy.ts';

const request = (overrides: Partial<AccessRequest> = {}): AccessRequest => ({
  id: 'request-A-1', tenantId: 'A', requesterId: 'mira',
  policyVersion: 'v1', risk: 'high', state: 'pending', approvedBy: [],
  ...overrides,
});
const actor = (overrides: Partial<Actor> = {}): Actor => ({
  id: 'leon', tenantId: 'A', activeMembership: true, roles: ['approver'], ...overrides,
});

test('creation-bound v1 high-risk policy still permits one eligible approval', () => {
  const original = request();
  assert.equal(requiredApprovals(original), 1);
  const result = approve(original, actor());
  assert.equal(result.ok, true);
  if (!result.ok) assert.fail('eligible v1 approval should succeed');
  assert.equal(result.request.state, 'approved');
  assert.equal(result.request.policyVersion, 'v1');
});

test('standard-risk v2 still requires one approval', () => {
  const result = approve(request({ policyVersion: 'v2', risk: 'standard' }), actor());
  assert.equal(result.ok, true);
  if (!result.ok) assert.fail('standard v2 approval should succeed');
  assert.equal(result.request.state, 'approved');
});

test('high-risk v2 stays pending after one actor and completes after a distinct second', () => {
  const first = approve(request({ policyVersion: 'v2' }), actor());
  if (!first.ok) assert.fail('first approval should be valid');
  assert.equal(first.request.state, 'pending');
  const second = approve(first.request, actor({ id: 'priya' }));
  if (!second.ok) assert.fail('distinct second approval should be valid');
  assert.equal(second.request.state, 'approved');
  assert.deepEqual(second.request.approvedBy, ['leon', 'priya']);
});

test('repeating the first approver cannot count as the distinct second approver', () => {
  const partial = request({ policyVersion: 'v2', approvedBy: ['leon'] });
  assert.deepEqual(approve(partial, actor()), { ok: false, reason: 'duplicate_actor' });
  assert.deepEqual(partial.approvedBy, ['leon']);
  assert.equal(partial.state, 'pending');
});

test('pending-state requester with approver and admin roles is denied; positive control works', () => {
  const pending = request();
  assert.deepEqual(approve(pending, actor({ id: 'mira', roles: ['requester', 'approver', 'admin'] })),
    { ok: false, reason: 'self_approval' });
  const control = approve(request(), actor());
  assert.equal(control.ok, true);
});

test('revoked membership is denied despite an approver role', () => {
  assert.deepEqual(approve(request(), actor({ activeMembership: false })),
    { ok: false, reason: 'inactive_member' });
});

test('foreign-tenant approver cannot change this tenant request', () => {
  assert.deepEqual(approve(request(), actor({ tenantId: 'B' })),
    { ok: false, reason: 'foreign_tenant' });
});

test('administrator status alone does not supply an approver role', () => {
  assert.deepEqual(approve(request(), actor({ roles: ['admin'] })),
    { ok: false, reason: 'not_approver' });
});

test('an eligible actor cannot approve either terminal request state', () => {
  for (const state of ['approved', 'rejected'] as const) {
    assert.deepEqual(approve(request({ state }), actor()), { ok: false, reason: 'terminal' });
  }
});

test('a successful partial approval returns fresh state without mutating its input', () => {
  const original = request({ policyVersion: 'v2' });
  const before = structuredClone(original);
  const result = approve(original, actor());
  if (!result.ok) assert.fail('first approval should be valid');
  assert.deepEqual(original, before);
  assert.notEqual(result.request, original);
  assert.notEqual(result.request.approvedBy, original.approvedBy);
});
