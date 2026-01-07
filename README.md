# Predator–Prey ODE Solver Benchmark

A short, self-contained benchmarking report (Jupyter Notebook) comparing numerical methods for solving a predator–prey (Lotka–Volterra) system of ODEs, with a recommendation based on accuracy and runtime efficiency.



## Problem (what this notebook solves)

A predator–prey model for prey `x(t)` and predator `y(t)`:

dx/dt = αx − βxy + f(t)  
dy/dt = δxy − γy + g(t)

Two test cases are used:
1) **Forced case with exact solution** (used to measure numerical error against ground truth).  
2) **Unforced case** where the solution should be periodic and population maxima should remain consistent (used as a qualitative/behavioral check).



## Methods compared (used in this notebook)

**Runge–Kutta (4th order):** *(selected via `solver(...)` in `solvers.py` as `"Runge-Kutta"`)*  


**SSPRK3 (3rd order):** *(selected via `solver(...)` in `solvers.py` as `"SSPRK3"`)* 


**Midpoint method (2nd order / RK2):** *(implemented directly in the notebook as a custom baseline)*  



## Evaluation approach

- Run each method over a sequence of step sizes up to a specified final time `T`.

- Compare:
  - Accuracy (e.g., error vs exact solution in test case 1)
  - Computational efficiency (wall-clock runtime)
  - Qualitative stability/behavior in the periodic test case



## Summary (results & recommendation)

**Results** 

***Accuracy (forced case with exact solution):*** 

Runge–Kutta (4th order) achieved the lowest worst-case error across all tested step sizes. SSPRK3 was consistently less accurate, and the Midpoint (RK2) baseline had the largest errors—especially at coarser step sizes.


***Stability (unforced periodic case):*** 

Runge–Kutta and SSPRK3 preserved near-consistent prey/predator maxima for small-to-moderate step sizes. The Midpoint method increasingly distorted the oscillation amplitudes as the step size increased.


**Recommendation:** 

Use **Runge–Kutta (4th order)** as the default for the best accuracy–cost balance. Use **SSPRK3** when you need faster runs and can tolerate reduced accuracy. Keep **Midpoint (RK2)** as a fast baseline/educational comparator rather than a primary solver.




## Summary (results & recommendation)


**Runge–Kutta (4th order).** 

A well-balanced choice that delivers dependable performance with reasonable computational cost, making it suitable as a general-purpose default.
**SSPRK3 (3rd order).** 
Recommended when higher-fidelity results are required—particularly at smaller time steps—at the expense of increased computational effort.


**Midpoint (RK2).** 

The fastest option, but less accurate; best suited for quick exploratory runs or instructional/early-stage analysis where a concise overview is sufficient.


**Current sufficiency and next steps.** 

The three methods are sufficient for the current scope and decision-making. For stronger confidence, further research and inspection/validation is recommended (e.g., broader parameter sweeps, additional solvers, and more rigorous error/stability checks) before using the approach in wider or higher-stakes modelling contexts.
