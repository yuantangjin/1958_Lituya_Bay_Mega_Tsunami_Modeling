# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:57:36 2024

@author: dell
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

# Assume the known x, y, vs, hw data
# x_data = np.array([2.31, 1.83, 1.59, 1.44, 1.31,
#                    2.72, 2.16, 1.88, 1.71, 1.54,
#                    3.14, 2.50, 2.17, 1.97, 1.78,
#                    3.81, 3.03, 2.63, 2.39, 2.16,
#                    4.61, 3.66, 3.18, 2.89, 2.61])   # x data

# y_data = np.array([2.85, 1.68, 1.22, 0.99, 0.76,
#                    3.08, 1.75, 1.29, 1.01, 0.81,
#                    3.12, 1.87, 1.39, 1.07, 0.86,
#                    3.59, 2.05, 1.44, 1.13, 0.90,
#                    3.95, 2.27, 1.67, 1.33, 1.02])   # y data

# vs_data = np.array([55.0, 55.0, 55.0, 55.0, 55.0,
#                     65.0, 65.0, 65.0, 65.0, 65.0,
#                     75.0, 75.0, 75.0, 75.0, 75.0,
#                     91.0, 91.0, 91.0, 91.0, 91.0,
#                     110.0,110.0,110.0,110.0,110.0])  # vs data

# hw_data = np.array([58.0, 92.0, 122.0, 148.0, 181.0,
#                     58.0, 92.0, 122.0, 148.0, 181.0,
#                     58.0, 92.0, 122.0, 148.0, 181.0,
#                     58.0, 92.0, 122.0, 148.0, 181.0,
#                     58.0, 92.0, 122.0, 148.0, 181.0])  # hw data

# Define fitting function y = k(vs, hw) * (x + a(vs, hw)) + b(vs, hw)
# def func(x, vs, hw, k0, k1, k2, a0, a1, a2, b0, b1, b2):
#     k = k0 + k1 * vs + k2 * hw
#     a = a0 + a1 * vs + a2 * hw
#     b = b0 + b1 * vs + b2 * hw
#     return k * (x + a) + b

# Fitting results of global surge amplitude
# Assume the known x, y, vs, hw data
x_data = np.array([2.31, 1.83, 1.59, 1.44, 1.31,
                   2.72, 2.16, 1.88, 1.71, 1.54,
                   3.14, 2.50, 2.17, 1.97, 1.78,
                   3.81, 3.03, 2.63, 2.39, 2.16,
                   4.61, 3.66, 3.18, 2.89, 2.61])   # x data

y_data = np.array([2.89, 1.80, 1.38, 1.15, 0.92,
                   3.15, 1.87, 1.48, 1.20, 0.97,
                   3.23, 2.04, 1.51, 1.25, 1.01, 
                   3.64, 2.21, 1.66, 1.37, 1.10,  
                   4.24, 2.56, 1.92, 1.55, 1.24])   # y data

vs_data = np.array([55.0, 55.0, 55.0, 55.0, 55.0,
                    65.0, 65.0, 65.0, 65.0, 65.0,
                    75.0, 75.0, 75.0, 75.0, 75.0,
                    91.0, 91.0, 91.0, 91.0, 91.0,
                    110.0,110.0,110.0,110.0,110.0])  # vs data

hw_data = np.array([58.0, 92.0, 122.0, 148.0, 181.0,
                    58.0, 92.0, 122.0, 148.0, 181.0,
                    58.0, 92.0, 122.0, 148.0, 181.0,
                    58.0, 92.0, 122.0, 148.0, 181.0,
                    58.0, 92.0, 122.0, 148.0, 181.0])  # hw data

# Define fitting function y = k(vs, hw) * (x + a(vs, hw)) + b(vs, hw)
def func(vars, k0, k1, k2, a0, a1, a2, b0, b1, b2):
    x, vs, hw = vars  # Unpack vars to x, vs, hw
    k = k0 + k1 * vs + k2 * hw
    a = a0 + a1 * vs + a2 * hw
    b = b0 + b1 * vs + b2 * hw
    return k * (x + a) + b

# Perform curve fitting, p0 is the initial guess for parameters
# popt, pcov = curve_fit(func, (x_data, vs_data, hw_data), y_data, p0=[1, 1, 1, 1, 1, 1, 1, 1, 1])
popt, pcov = curve_fit(func, (x_data, vs_data, hw_data), y_data, p0=[1, 1, 1, 1, 1, 1, 1, 1, 1])

# Retrieve the fitting parameters
k0, k1, k2, a0, a1, a2, b0, b1, b2 = popt
print("Fitting parameters:", popt)

# Plot the fitting curve
y_fit = func((x_data, vs_data, hw_data), *popt)

plt.scatter(x_data, y_data, label="Original data")
plt.plot(x_data, y_fit, color='red', label="Fitted curve")
plt.legend()
plt.show()

print("—————————————————————Error Evaluation—————————————————————")
# 1. Calculate the coefficient of determination R^2
r2 = r2_score(y_data, y_fit)
print(f"Coefficient of Determination (R^2): {r2:.4f}")

# 2. Calculate Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)
mse = mean_squared_error(y_data, y_fit)
rmse = np.sqrt(mse)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# 3. Calculate residuals and plot the residuals
residuals = y_data - y_fit
plt.figure()
plt.scatter(x_data, residuals)
plt.axhline(0, color='red', linestyle='--', lw=2)
plt.title("Error Figure")
plt.xlabel("x")
plt.ylabel("Error")
plt.show()

# 4. Calculate Residual Sum of Squares (RSS)
rss = np.sum(residuals**2)
print(f"Residual Sum of Squares (RSS): {rss:.4f}")

print("Fitting complete")
