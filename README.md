# nshare_calc
Python library for calculating the optimal number of shares given a portfolio using integer programming.

## Problem statement

Given a portfolio with total asset $S$, price vector $\mathbf p$ and weight vector $\mathbf w$, find integer vector $\mathbf n$ such that

* The total value of all stocks must not exceed the total asset, i.e., $\mathbf p \cdot \mathbf n \leq S$;
* Minimize the total absolute difference between the desired values and the actual values for all stocks, i.e., $\Sigma_i |S w_i - p_i n_i|$.
