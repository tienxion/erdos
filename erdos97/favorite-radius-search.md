# Arbitrary-favorite-radius C3 search: negative heuristic result

**Status: no proof, counterexample, or robust exact-looking candidate.** This
bounded experiment tests a larger family than requiring every representative's
favorite radius to equal the side length of its own equilateral orbit. It does
not rule out any polygon size or any symmetry class.

## Parametrization and objective

For each `m = 9, 12, 15, 20`, choose `m` representatives in one 120-degree polar
sector and include their two rotations. Positive angular gaps give a fixed
cyclic order; logarithmic radial variables allow unequal orbit radii. Mean
squared orbit radius is normalized to one, and the first polar angle is zero.
There are `2m - 2` real shape parameters.

For each representative, sort its distances to all `3m - 1` other vertices.
Among all consecutive windows of four distances, choose the window with the
smallest relative variance and minimize its four mean-zero relative deviations.
The common favorite radius is inferred independently for each representative.
This minimum over contact windows is only piecewise smooth.

The residual also penalizes normalized turn sine below `0.0002` and adjacent
edge length below `0.004`. Angular gaps have a small positive lower bound; all
unconstrained parameters lie in `[-5.5, 5.5]`. These are numerical search choices,
not deductions about an exact construction. Positive turn penalties are soft,
so the full hull must still be checked.

## Seeds and bounded runs

The initial 16 runs used a regular polygon, a smooth near-regular perturbation,
and two samplings of the primary Bárány–Roldán-Pensado 12-point seed:

`(1,0), (.906,.114), (.645,.359), (-.498,.871)`, plus 120-degree rotations.

The decimal coordinates here are exact scaled integers from the paper, not
approximations to its unspecified fifteenth-vertex construction. The source is
[Section 3 of the primary paper](https://www.renyi.hu/~barany/cikkek/134.pdf).
Normal-angle and approximate equal-arclength samples were taken on the smooth
support curve

\[
h(\theta)=\beta^{-1}\log\sum_p e^{\beta p\cdot u(\theta)}+\epsilon,
\qquad \epsilon=0.025,
\]

with `beta = 12` or `25`. Its exact support identity is

\[
h+h''=\frac{H(w)}{\beta}
 +\beta\operatorname{Var}_w(p\cdot t)+\epsilon>0.
\]

Thus the underlying curve has positive curvature; the sampled coordinates and
optimization remain floating-point computations.

A further 48 deterministic runs (random seed `970004`) varied sampling phase,
angular gaps, and smooth radial perturbations. Half included an initial stage
that fixed one of the four best contact windows at each representative, followed
by the ordinary adaptive-window objective. This helps probe alternative contact
choices without requiring the own-orbit side length. The 64 runs took about
48 seconds of total recorded run time, with explicit per-run and total bounds.

## Independent checks and results

For each `m`, the best complete-hull result was checked again from its serialized
Cartesian coordinates. This check recomputes original squared distances to the
four selected, distinct, non-self targets; all pair separations; consecutive
cross products; and the convex hull of all `3m` points.

Define the reported error by

\[
\max_i \frac{\max_{j\in S_i}|p_i-p_j|^2
                    -\min_{j\in S_i}|p_i-p_j|^2}
                   {\frac14\sum_{j\in S_i}|p_i-p_j|^2}.
\]

| Orbits | Vertices / hull vertices | Best error | Minimum pair separation | Minimum raw turn cross product |
|---:|---:|---:|---:|---:|
| 9 | 27 / 27 | 0.001981222 | 0.01909 | 8.42e-7 |
| 12 | 36 / 36 | 0.008084548 | 0.01796 | 1.02e-7 |
| 15 | 45 / 45 | 0.003306698 | 0.004987 | 6.02e-9 |
| 20 | 60 / 60 | 0.002505021 | 0.01157 | 2.88e-8 |

These are substantial remaining errors, not near-exact equalities. The best
27-vertex result came from the smoothed primary seed with alternate-window
initialization. Seven of its nine representatives selected their two own-orbit
neighbors among the four contacts; the other two selected none. Their inferred
favorite radii are about `1.023` and `1.052` times their own-orbit side lengths.
Thus this particular search genuinely left the own-orbit favorite-radius
restriction, but it did not close the equations.

Many optimizations push turn sines very close to the imposed `0.0002` floor.
As a diagnostic, we froze the best contact lists and removed the convexity
penalty, retaining the edge-collapse penalty. Each of these four extra runs was
bounded by eight seconds. Smaller errors then came with failed hull checks:

| Orbits | Error after convexity relaxation | Remaining hull vertices |
|---:|---:|---:|
| 9 | 0.000071515 | 21 / 27 |
| 12 | 0.000858537 | 27 / 36 |
| 15 | 0.001263579 | 39 / 45 |
| 20 | 0.000704843 | 9 / 60 |

The relaxed examples also push some separations to the imposed `0.004` floor.
This demonstrates a failure mode of these runs: making the intended equalities
closer is accompanied by nonconvexity and clustering. It is not an impossibility
proof or evidence that every other contact graph must behave this way.

## Reproduction and saved data

From the workspace root:

```sh
erdos97/.venv/bin/python erdos97/favorite-radius-search.py --seconds-per-run 9 --max-nfev 90
erdos97/.venv/bin/python erdos97/favorite-radius-restarts.py
erdos97/.venv/bin/python erdos97/favorite-radius-audit.py
```

The corresponding JSON files are `favorite-radius-results.json`,
`favorite-radius-restart-results.json`, and `favorite-radius-audit.json`. They
contain the selected contacts, original squared lengths, optimizer statuses,
coordinates, parameters, and geometric checks. No computation remains running.
