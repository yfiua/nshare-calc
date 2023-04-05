#!/bin/env python3

import pulp
import numpy as np

def optimize(total, p, w):
    # Sanity
    N = len(p)
    if N != len(w):
        print("Dimensions of price and weight do not agree!")
        return 0

    # Normalize weights
    w = w / np.sum(w)

    # Define the problem as a minimization problem
    problem = pulp.LpProblem("Minimize total difference", pulp.LpMinimize)

    # Define decision variables
    t = pulp.LpVariable.dicts('t', range(N), cat='Continuous')
    n = pulp.LpVariable.dicts('n', range(N), lowBound=0, cat='Integer')

    # Define the objective function
    problem += pulp.lpSum(t)

    # Define the constraints
    # https://math.stackexchange.com/questions/1954992/linear-programming-minimizing-absolute-values-and-formulate-in-lp
    for i in range(N):
        problem += t[i] >= p[i] * n[i] - total * w[i]
        problem += t[i] >= total * w[i] - p[i] * n[i]

    problem += pulp.lpDot(p, n) <= total

    # Solve the problem
    status = problem.solve()

    # Convert result to numpy array
    n = np.array([n[i].varValue for i in range(N)])

    return n

if __name__ == "__main__":
    # params
    N = 2
    total = 100
    p = [6, 5.5]
    w = [0.6, 0.4]

    n = optimize(total, p, w)

    # Print the optimal solution
    print("Optimal Solution:")
    print(n)
    #print("Total difference =", pulp.value(problem.objective))
