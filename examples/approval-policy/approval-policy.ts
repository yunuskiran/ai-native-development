/**
 * Book teaching model for APPROVAL only, not the SaaS or an independent oracle.
 * Inputs are trusted, already-established domain records. Types are not runtime
 * validation. No authentication, HTTP, storage, audit, retries or concurrency.
 */
export type Role = 'requester' | 'approver' | 'admin';

export type Actor = Readonly<{
  id: string;
  tenantId: string;
  activeMembership: boolean;
  roles: readonly Role[];
}>;

export type AccessRequest = Readonly<{
  id: string;
  tenantId: string;
  requesterId: string;
  policyVersion: 'v1' | 'v2';
  risk: 'standard' | 'high';
  state: 'pending' | 'approved' | 'rejected';
  approvedBy: readonly string[];
}>;

export type ApprovalResult =
  | Readonly<{ ok: true; request: AccessRequest }>
  | Readonly<{
      ok: false;
      reason: 'foreign_tenant' | 'inactive_member' | 'not_approver'
        | 'self_approval' | 'terminal' | 'duplicate_actor';
    }>;

export function requiredApprovals(request: AccessRequest): 1 | 2 {
  return request.policyVersion === 'v2' && request.risk === 'high' ? 2 : 1;
}

export function approve(request: AccessRequest, actor: Actor): ApprovalResult {
  // These are internal model reasons, not an HTTP disclosure/error contract.
  if (actor.tenantId !== request.tenantId) return { ok: false, reason: 'foreign_tenant' };
  if (!actor.activeMembership) return { ok: false, reason: 'inactive_member' };
  if (!actor.roles.includes('approver')) return { ok: false, reason: 'not_approver' };
  if (actor.id === request.requesterId) return { ok: false, reason: 'self_approval' };
  if (request.state !== 'pending') return { ok: false, reason: 'terminal' };
  if (request.approvedBy.includes(actor.id)) return { ok: false, reason: 'duplicate_actor' };

  const approvedBy = [...request.approvedBy, actor.id];
  return {
    ok: true,
    request: {
      ...request,
      approvedBy,
      state: approvedBy.length >= requiredApprovals(request) ? 'approved' : 'pending',
    },
  };
}
