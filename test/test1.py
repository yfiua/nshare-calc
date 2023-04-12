#!/usr/bin/python3

from nshare_calc import calc_n

if __name__ == "__main__":
    # params
    S = 100
    p = [6, 5.5]
    w = [0.6, 0.4]

    n = calc_n(S, p, w)

    # Print the optimal solution
    print("Optimal Solution:")
    print(n)
