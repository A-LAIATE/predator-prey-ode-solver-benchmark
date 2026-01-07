from typing import Callable, List, Tuple, TypeVar

import numpy as np

TABLEAU = {
    "Heun": (
        np.array([[0.0, 0.0], [1.0, 0.0]]),
        np.array([0.5, 0.5]),
        np.array([0.0, 1.0]),
    ),
    "Ralston": (
        np.array([[0.0, 0.0], [2 / 3, 0.0]]),
        np.array([0.25, 0.75]),
        np.array([0.0, 2 / 3]),
    ),
    "Van der Houwen": (
        np.array([[0.0, 0.0, 0.0], [1 / 2, 0.0, 0.0], [0.0, 0.75, 0.0]]),
        np.array([2 / 9, 1 / 3, 4 / 9]),
        np.array([0.0, 1 / 2, 3 / 4]),
    ),
    "SSPRK3": (
        np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.25, 0.25, 0.0]]),
        np.array([1 / 6, 1 / 6, 2 / 3]),
        np.array([0.0, 1.0, 1 / 2]),
    ),
    "Runge-Kutta": (
        np.array(
            [
                [0.0, 0.0, 0.0, 0.0],
                [0.5, 0.0, 0.0, 0.0],
                [0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
            ]
        ),
        np.array([1 / 6, 1 / 3, 1 / 3, 1 / 6]),
        np.array([0.0, 0.5, 0.5, 1.0]),
    ),
    "3/8-rule": (
        np.array(
            [
                [0.0, 0.0, 0.0, 0.0],
                [1 / 3, 0.0, 0.0, 0.0],
                [-1 / 3, 1.0, 0.0, 0.0],
                [1.0, -1.0, 1.0, 0.0],
            ]
        ),
        np.array([1 / 8, 3 / 8, 3 / 8, 1 / 8]),
        np.array([0.0, 1 / 3, 2 / 3, 1]),
    ),
    "Ralston-4": (
        np.array(
            [
                [0.0, 0.0, 0.0, 0.0],
                [0.4, 0.0, 0.0, 0.0],
                [0.29697761, 0.15875964, 0.0, 0.0],
                [0.21810040, -3.05096516, 3.83286476, 0.0],
            ]
        ),
        np.array([0.17476028, -0.55148066, 1.20553560, 0.17118478]),
        np.array([0.0, 0.4, 0.45573725, 1.0]),
    ),
}

y_type = TypeVar("y_type", np.ndarray, np.double)


def solver(
    rhs: Callable[[np.double, y_type], y_type],
    y0: y_type,
    t0: np.double,
    dt: np.double,
    T: np.double,
    method: str,
) -> Tuple[List[np.double], List[y_type]]:
    """
    Solve the differential equation(s).

    Solve the differential equation specified by

    y'(t) = rhs(t, y) subject to y(t_0) = y_0.

    The problem is solved numerical using METHOD from t0 to T using a time step dt.

    Parameters
    ----------

    rhs
            A function describing the right hand side of the differential equation(s)
    y0
            The starting value of y
    t0
            The starting value of t
    dt
            The time step
    T
            The final or stopping time
    method
            The method used to advance to solver. method should be one of:
            Heun, Ralston, Van De Houwen, SSPRK3, Runge-Kutta, 3/8-rule, Ralston-4

    Returns
    -------

    t
            The time points where the solution was found
    y
            The estimate of the solution at each time point
    """

    # set initial data into solution arrays
    t_out = [t0]
    y_out = [y0]

    # extract method helpers
    matrix, weights, nodes = TABLEAU[method]
    s = len(weights)
    k: List[y_type | None] = [None for _ in range(s)]

    # count steps
    timesteps = int(T / dt)

    # time loop
    for step in range(timesteps):
        # build k's
        for i in range(s):
            temp = sum(matrix[i, j] * k[j] for j in range(i))
            k[i] = rhs(t_out[-1] + dt * nodes[i], y_out[-1] + dt * temp)

        y_update = sum([k[i] * weights[i] for i in range(s)])

        y_new = y_out[-1] + dt * y_update
        t_new = t_out[-1] + dt

        t_out.append(t_new)
        y_out.append(y_new)

    return t_out, y_out


def example_code_1():
    """
    Example code for single differential equation

    The problem is y'(t) = y subject to y(0) = 1.0.

    The problem is solved with dt = 0.1 until T = 1.0 using Heun's method
    """

    def rhs1(t: np.double, y: np.double) -> np.double:
        return -y

    t, y = solver(rhs1, 1.0, 0.0, 0.1, 1.0, "Heun")


def example_code_2():
    """
    example code for system of differential equations

    The problem is (x'(t), y'(t)) = (-y(t), x(t)) subject to (x(0), y(0)) = (1.0, 0.0)

    The problem is solved with dt = 0.1 until T = 1.0 using the Runge-Kutta method
    """

    def rhs2(t: np.double, y: np.ndarray) -> np.ndarray:
        return np.array([-y[1], y[0]])

    t, y = solver(rhs2, np.array([1.0, 0.0]), 0.0, 0.1, 1.0, "Runge-Kutta")


if __name__ == "__main__":
    for method, (matrix, weights, nodes) in TABLEAU.items():
        # test methods are explicit
        np.testing.assert_almost_equal(np.tril(matrix), matrix)
        # test methods are consistent
        np.testing.assert_almost_equal(sum(weights), 1.0)
        # test dimensions match
        n, m = matrix.shape
        assert n == m
        assert n == len(weights)
        assert n == len(nodes)

    example_code_1()
    example_code_2()
