# Importing packages for tests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# calculate the mean of the independent variables and the dependent variables

def mean_iv(x):
    return sum(x) / float(len(x))


def mean_dv(y):
    return sum(y) / float(len(y))


# calculate the variance
def variance(values, mean):
    return sum([(val - mean)**2 for val in values])

# Calculate covariance between independent variable and dependent variable


def covariance(IV, mean_iv, DV, mean_dv):
    covariance = 0.0
    for r in range(len(IV)):
        covariance = covariance + (IV[r] - mean_iv) * (DV[r] - mean_dv)
    return covariance

# calculate m


def m_(covariance, variance_of_x):
    return covariance / variance_of_x

# calculate c


def c_(mean_of_y, m, mean_of_x):
    return mean_of_y - m * mean_of_x


if __name__ == "__main__":
    df = pd.read_csv("../data/Real estate.csv")
    print(df.head())
    x = df['X2 house age']
    y = df['Y house price of unit area']
    iv_mean = mean_iv(x)
    dv_mean = mean_dv(y)
    variance_x, variance_y = variance(x, iv_mean), variance(y, dv_mean)
    covariance_ = covariance(x, iv_mean, y, dv_mean)
    m = m_(covariance_, variance_x)
    c = c_(dv_mean, m, iv_mean)
    print(m, c)
