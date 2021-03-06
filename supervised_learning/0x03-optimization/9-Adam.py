#!/usr/bin/env python3
""" Functions:
        update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t)
"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """ Function that updates a variable in place using the Adam
        optimization algorithm.

    Args:
        alpha (): is the learning rate
        beta1 (): Is the momentum weight
        beta2 (): is the momentum weight
        epsilon (): is a small number to avoid division by zero
        var (): is a numpy.ndarray containing the variable to be updated
        grad (): is a numpy.ndarray containing the gradient of var
        v (): is the previous first moment of var
        s (): is the previous second moment of var
        t (): is the time step used for bias correction

    Return:
        The updated variable, the new first moment, and the new second moment,
        respectively
    """
    Vd = (beta1 * v) + ((1 - beta1) * grad)
    Sd = (beta2 * s) + ((1 - beta2) * (grad ** 2))
    Vd_correct = Vd / (1 - beta1 ** t)
    Sd_correct = Sd / (1 - beta2 ** t)

    w = var - alpha * (Vd_correct / ((Sd_correct ** (0.5)) + epsilon))
    return w, Vd, Sd
