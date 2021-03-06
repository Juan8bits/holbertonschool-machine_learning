#!/usr/bin/env python3
""" Functions:
        create_layer(prev, n, activation)
"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ Function that creates the forward propagation graph for the
        neural network.

    Args:
        x (tensor object): Placeholder for the input data.
        layer_sizes (list): A list containing the number of nodes in each
            layer of the network. Defaults to [].
        activations (list): A list containing the activation functions for
            each layer of the network. Defaults to [].
    Return:
        The prediction of the network in tensor form.
    """
    A = create_layer(x, layer_sizes[0], activations[0])
    for i in range(1, len(layer_sizes)):
        A = create_layer(A, layer_sizes[i], activations[i])
    return A
