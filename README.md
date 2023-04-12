# nshare-calc
Python library for calculating the optimal number of shares given a portfolio using integer programming.

## Problem statement

Given a portfolio with total asset $S$, price vector $\mathbf p$ and weight vector $\mathbf w$, find integer vector $\mathbf n$ such that

* The total value of all stocks must not exceed the total asset, i.e., $\mathbf p \cdot \mathbf n \leq S$;
* Minimize the total absolute difference between the desired values and the actual values for all stocks, i.e., $\Sigma_i |S w_i - p_i n_i|$.

## Installation

```
pip install nshare-calc
```

## Usage

```
from nshare_calc import calc_n

# params
S = 100
p = [6, 5.5]
w = [0.6, 0.4]         # w will be automatically normalized

n = calc_n(S, p, w)    # Result: n = [10.  7.]
```
