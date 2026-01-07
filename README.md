# Predator–Prey ODE Solver Benchmark

  A short, self-contained benchmarking report using *Jupyter Notebook*, comparing numerical methods for solving a _Predator–Prey or Lotka–Volterra_ system of ODEs, with a recommendation based on accuracy and runtime efficiency.



## Problem

A predator–prey model for prey `x(t)` and predator `y(t)`:

dx/dt = αx − βxy + f(t)  
dy/dt = δxy − γy + g(t)

Two test cases are used:
- **Forced case with exact solution.** Used to measure numerical error against ground truth.  
- **Unforced case.** Where the solution should be periodic and population maxima should remain consistent. _Note:_ Used as a qualitative and behavioral check.



## Methods compared 

- **Runge–Kutta (4th order):** *Selected via `solver(...)` in `solvers.py` as `"Runge-Kutta"`.*
- **SSPRK3 (3rd order):** *Selected via `solver(...)` in `solvers.py` as `"SSPRK3"`.*
- **Midpoint method (2nd order / RK2):** *Implemented directly in the notebook as a custom baseline.*  



## Evaluation approach

- Run each method over a sequence of step sizes up to a specified final time `T`.
- Compare:
  - Accuracy. _Such as error vs exact solution in test case 1._
  - Computational efficiency. _Wall-clock runtime._
  - Qualitative. _Stability and behavior in the periodic test case._


## Summary

**Results**


_**Runge–Kutta (4th order)**_

  A well-balanced choice that delivers dependable performance with reasonable computational cost, making it suitable as a general-purpose default.


_**SSPRK3 (3rd order)**_

  Recommended when higher-fidelity results are required, particularly at smaller time steps at the expense of increased computational effort.


_**Midpoint (RK2)**_

  The fastest option, but less accurate; best suited for quick exploratory runs or instructional/early-stage analysis where a concise overview is sufficient.


**Recommendation**

  The three methods are sufficient for the current scope and decision-making. For stronger confidence, further research and inspection or validation is recommended such as a) broader parameter sweeps; b) additional solvers; and c) more rigorous error and stability checks, before using the approach in wider or higher-stakes modelling contexts.
