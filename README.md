# Predator–Prey ODE Solver Benchmark

A short, self-contained benchmarking report using *Jupyter Notebook*, comparing numerical methods for solving a *(predator–prey or Lotka–Volterra)* system of ODEs, with a recommendation based on accuracy and runtime efficiency.



## Problem

A predator–prey model for prey `x(t)` and predator `y(t)`:

dx/dt = αx − βxy + f(t)  
dy/dt = δxy − γy + g(t)

Two test cases are used:
1. **Forced case with exact solution.** Used to measure numerical error against ground truth.  
2. **Unforced case.** Where the solution should be periodic and population maxima should remain consistent. **Note.** _Used as a qualitative/behavioral check._



## Methods compared 

1. **Runge–Kutta (4th order):** *Selected via `solver(...)` in `solvers.py` as `"Runge-Kutta"`*  
2. **SSPRK3 (3rd order):** *Selected via `solver(...)` in `solvers.py` as `"SSPRK3"`* 
3. **Midpoint method (2nd order / RK2):** *(implemented directly in the notebook as a custom baseline)*  



## Evaluation approach

1. Run each method over a sequence of step sizes up to a specified final time `T`.

2. Compare:
  - Accuracy (e.g., error vs exact solution in test case 1)
  - Computational efficiency (wall-clock runtime)
  - Qualitative stability/behavior in the periodic test case


---
## Summary

**Results**


***Runge–Kutta (4th order).***

A well-balanced choice that delivers dependable performance with reasonable computational cost, making it suitable as a general-purpose default.


***SSPRK3 (3rd order):***

Recommended when higher-fidelity results are required, particularly at smaller time steps at the expense of increased computational effort.


***Midpoint (RK2).*** 

The fastest option, but less accurate; best suited for quick exploratory runs or instructional/early-stage analysis where a concise overview is sufficient.


**Recommendation**

The three methods are sufficient for the current scope and decision-making. For stronger confidence, further research and inspection/validation is recommended (e.g., broader parameter sweeps, additional solvers, and more rigorous error/stability checks) before using the approach in wider or higher-stakes modelling contexts.
