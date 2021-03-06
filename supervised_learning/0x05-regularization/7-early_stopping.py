#!/usr/bin/env python3
""" Functions:
        early_stopping(cost, opt_cost, threshold, patience, count)
"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """ Function that determines if you should stop gradient descent early.
    Early stopping should occur when the validation cost of the network has
    not decreased relative to the optimal validation cost by more than the
    threshold over a specific patience count.

    Args:
        cost (): is the current validation cost of the NN.
        opt_cost (): is the lowest recorded validation cost of the NN.
        threshold (): is the threshold used for early stopping.
        patience (): is the patience count used for early stopping.
        count (): is the count of how long the threshold has not been met.
    Returns:
        A boolean of whether the network should be stopped early, followed
        by the updated count.
    """
    if (opt_cost - cost - threshold > 0):
        count = 0
    else:
        count += 1
    NN_should_be_stopped_early = False
    if (count == patience):
        NN_should_be_stopped_early = True

    return (NN_should_be_stopped_early, count)
