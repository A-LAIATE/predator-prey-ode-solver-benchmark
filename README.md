# Predator–Prey ODE Solver Benchmark
---
A short, self-contained benchmarking report (Jupyter Notebook) comparing numerical methods for solving a predator–prey (Lotka–Volterra) system of ODEs, with a recommendation based on accuracy and runtime efficiency.

## Problem (what this notebook solves)
---
A predator–prey model for prey `x(t)` and predator `y(t)`:

dx/dt = αx − βxy + f(t)  
dy/dt = δxy − γy + g(t)

Two test cases are used:
1) **Forced case with exact solution** (used to measure numerical error against ground truth).  
2) **Unforced case** where the solution should be periodic and population maxima should remain consistent (used as a qualitative/behavioral check).

## Methods compared (used in this notebook)
---
- **Runge–Kutta (4th order)** *(selected via `solver(...)` in `solvers.py` as `"Runge-Kutta"`)*  
- **SSPRK3 (3rd order)** *(selected via `solver(...)` in `solvers.py` as `"SSPRK3"`)*  
- **Midpoint method (2nd order / RK2)** *(implemented directly in the notebook as a custom baseline)*  

## Evaluation approach
---
- Run each method over a sequence of step sizes up to a specified final time `T`.
- Compare:
  - Accuracy (e.g., error vs exact solution in test case 1)
  - Computational efficiency (wall-clock runtime)
  - Qualitative stability/behavior in the periodic test case


--- 
