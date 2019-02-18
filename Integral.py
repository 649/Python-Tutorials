#!/usr/bin/env python
from scipy.integrate import quad

def integrand(x):
    return x**2

# f(x) = x^2
# 0 <= x <= 1
# ANS: 1/3
ans, err = quad(integrand, 0, 1)
print(ans)
