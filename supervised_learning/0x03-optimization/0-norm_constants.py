#!/usr/bin/env python3
""" Functions:
        normalization_constants(X)
"""
import numpy as np


def normalization_constants(X):
    """ Function that calculates the normalization (standardization)
        constants of a matrix.

    Args:
        X (numpy array): Numpy array of shape(m, nx) to normalize.
            m is the number of data points.
            nx is the number of features.
    Return:
        The mean and standard deviation of each feature, respectively.
    """
    return np.mean(X, axis=0), np.std(X, axis=0)
