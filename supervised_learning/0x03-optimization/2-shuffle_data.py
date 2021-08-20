#!/usr/bin/env python3
""" Functions:
        shuffle_data(X, Y)
"""
import numpy as np


def shuffle_data(X, Y):
    """ Function that shuffles the data points in two matrices
        the same way.

    Args:
        X (Numpy array): Numpy.ndarray of shape (m, nx) to shuffle.
            m is the number of data points.
            nx is the number of features in X.
        Y (Numpy array): Numpy.ndarray of shape (m, ny) to shuffle.
            m is the same number of data points as in X.
            ny is the number of features in Y.
    Return:
        The shuffled X and Y matrices.
    """
    shuffle = np.random.permutation(len(X))

    X = X[shuffle]
    Y = Y[shuffle]
    return X, Y
