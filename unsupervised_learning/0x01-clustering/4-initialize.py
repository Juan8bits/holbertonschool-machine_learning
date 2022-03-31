#!/usr/bin/env python3
"""
    Functions:
        def initialize(X, k)
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """ initializes variables for a Gaussian Mixture Model
        Args:
            X: ndarray (n, d) dataset
            k: positive int
        Returns:
            pi, m, S, or None, None, None on failure
            pi ndarray (k,) priors for each cluster, initialized evenly
            m ndarray (k, d) containing the centroid means for each
                cluster, initialized with K-means
            S ndarray (k, d, d) containing the covariance
                matrices for each cluster, initialized as identity matrices
    """
    if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0:
        return None, None, None
    n, d = X.shape
    pi = np.ndarray(k)
    pi[:] = 1 / k
    m, clss = kmeans(X, k)
    S = np.ndarray((k, d, d))
    S[:] = np.identity(d)
    return pi, m, S
