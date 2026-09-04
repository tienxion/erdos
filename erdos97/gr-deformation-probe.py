#!/usr/bin/env python3
"""Floating-point second-order lift diagnostics; never an existence certificate."""
import json
from pathlib import Path

import numpy as np
from scipy.linalg import null_space


def probe(seed):
    m, n = len(seed['lines']), len(seed['points'])
    y = np.array([a['Y'] for a in seed['lines']])
    b = np.array([a['C'] for a in seed['lines']])
    v = np.array([p['V'] for p in seed['points']])
    w = np.array([p['W'] for p in seed['points']])
    edges = np.array(seed['incidence'])
    ii, jj = edges.T
    offw, offv, dim = 2*m, 2*m+n, 2*m+2*n
    J = np.zeros((len(edges), dim))
    for k, (i, j) in enumerate(edges):
        J[k, i], J[k, m+i] = -1, -v[j]
        J[k, offw+j], J[k, offv+j] = 1, -y[i]
    ul, singular, vr = np.linalg.svd(J, full_matrices=True)
    rank = sum(singular > singular[0]*1e-11)
    stresses, kernel = ul[:, rank:], vr[rank:].T

    # Infinitesimal PGL(3): homogeneous matrix with final diagonal entry zero.
    projective = []
    for k in range(8):
        a, c, e, f, g, h, p, q = np.eye(8)[k]
        dv = a*v+c*w+e-v*(p*v+q*w)
        dw = f*v+g*w+h-w*(p*v+q*w)
        dy = f-a*y-p*b-c*y*y+g*y-q*b*y
        db = h-e*y-c*b*y+g*b-q*b*b
        projective.append(np.r_[db, dy, dw, dv])
    P = np.array(projective).T
    projective_error = np.max(np.abs(J@P))
    residual_kernel = kernel @ null_space(P.T@kernel, rcond=1e-10)

    h = w[jj]-b[ii]-(v[jj]**2+y[ii]**2)/2
    K = np.r_[(y**4-6*b*b)/8,
              -(y**3+3*b*y)/2,
              -(v**4+6*w*w)/8,
              -v**3/2]
    first_error = np.max(np.abs(J@K+h*h/2))
    I = (3/16)*(stresses.T@(y[ii]**4*v[jj]**2+y[ii]**2*v[jj]**4))
    I6 = (1/80)*(stresses.T@(v[jj]-y[ii])**6)

    # Solve the linear relaxation of Q(alpha)=I. Products of parameters
    # are independent here; failure rules out this numerical relaxation.
    columns, monomials = [], []
    d = residual_kernel.shape[1]
    for a in range(d):
        for c in range(a, d):
            av = residual_kernel[:, a]
            cv = residual_kernel[:, c]
            product = av[m+ii]*cv[offv+jj]
            if a != c:
                product += cv[m+ii]*av[offv+jj]
            columns.append(stresses.T@product)
            monomials.append([a, c])
    Q = np.array(columns).T if columns else np.zeros((len(I), 0))
    # Absolute as well as relative tolerance: an all-roundoff matrix must
    # not generate enormous fictitious correction coefficients.
    uq, sq, vq = np.linalg.svd(Q, full_matrices=False)
    keep = sq > 1e-10*max(1., np.linalg.norm(Q))
    coefficients = (vq[keep].T@((uq[:, keep].T@I)/sq[keep])
                    if any(keep) else np.zeros(Q.shape[1]))
    relaxed_residual = I-Q@coefficients
    return dict(
        scope='Numerical diagnostic for a specified projective chart only.',
        incidence_residual=float(max(abs(w[jj]-b[ii]-y[ii]*v[jj]))),
        jacobian_rank=int(rank), kernel_dimension=int(dim-rank),
        stress_dimension=stresses.shape[1],
        singular_values=singular.tolist(),
        projective_kernel_error=float(projective_error),
        residual_kernel_dimension=d,
        first_order_correction_error=float(first_error),
        second_order_identity_error=float(max(abs(I-I6))),
        second_order_stress_norm=float(np.linalg.norm(I)),
        quotient_quadratic_norm=float(np.linalg.norm(Q)),
        quotient_quadratic_numerical_rank=int(sum(keep)),
        quotient_quadratic_singular_values=np.linalg.svd(Q, compute_uv=False).tolist(),
        relaxed_relative_residual=float(np.linalg.norm(relaxed_residual)/max(np.linalg.norm(I), 1e-100)),
        relaxed_coefficients=coefficients.tolist(),
        monomials=monomials,
        stress_load=I.tolist(), quotient_quadratic_matrix=Q.tolist())


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    seed = json.loads((root/'grunbaum-rigby-seed.json').read_text())
    result = probe(seed)
    (root/'gr-deformation-probe.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ['singular_values', 'quotient_quadratic_matrix',
                                   'stress_load']}, indent=2))
