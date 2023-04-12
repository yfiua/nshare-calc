#!/bin/env python3

import pulp
import numpy as np

def calc_n(S, p, w):
    # Sanity
    N = len(p)
    if N != len(w):
        print("Dimensions of price and weight do not agree!")
        return 0

    # Normalize weights
    w = w / np.sum(w)

    # Define the problem as a minimization problem
    problem = pulp.LpProblem("nshare_calc", pulp.LpMinimize)

    # Define decision variables
    t = pulp.LpVariable.dicts('t', range(N), cat='Continuous')
    n = pulp.LpVariable.dicts('n', range(N), lowBound=0, cat='Integer')

    # Define the objective function
    problem += pulp.lpSum(t)

    # Define the constraints
    # https://math.stackexchange.com/questions/1954992/linear-programming-minimizing-absolute-values-and-formulate-in-lp
    for i in range(N):
        problem += t[i] >= p[i] * n[i] - S * w[i]
        problem += t[i] >= S * w[i] - p[i] * n[i]

    problem += pulp.lpDot(p, n.values()) <= S

    # Solve the problem
    status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

    # Convert result to numpy array
    n = np.array([n[i].varValue for i in range(N)])

    return n
