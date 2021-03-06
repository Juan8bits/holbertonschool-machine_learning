#!/usr/bin/env python3
"""  Neuron Class
"""
import numpy as np


class Neuron:
    """ Class that defines a single neuron performing
        binary classification.
    """
    e = 2.7182818285

    def __init__(self, nx):
        """ Constructor
        Args:
            nx (int): Number of input features to the neuron.
        Attributes:
            W: The weights vector for the neuron.
            b: The bias for the neuron.
            A: The activated output of the neuron (prediction).
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.normal(0, 1, (1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ Getter method that return the value of the attribute "W".
        """
        return self.__W

    @property
    def A(self):
        """ Getter method that return the value of the attribute "A".
        """
        return self.__A

    @property
    def b(self):
        """ Getter method that return the value of the attribute "A".
        """
        return self.__b

    def forward_prop(self, X):
        """ Method that Calculates the forward propagation of the neuron.

        preactivation: y = mx + b
        activation with sigmoidea:
        1 / (1 + e ^(-x))

        Args:
            X (numpy object): Numpy.ndarray with shape (nx, m) that
            contains the input data.
                - nx is the number of input features to the neuron.
                - m is the number of examples.
        """
        # preactivation = np.matmul(self.__W, X) + self.__b
        preactivation = (self.W @ X) + self.b
        activation = 1 / (1 + np.exp(-preactivation))
        self.__A = activation
        return self.A

    def cost(self, Y, A):
        """ Method that calculates the cost of the model using
            logistic regression.

        J=−1/m * ∑mi=1 y(i)log(a(i))+(1−y(i))log(1−a(i))
        Args:
            Y (numpy object): Numpy.ndarray with shape (1, m) that contains the
                correct labels for the input data
            A (numpy object): Numpy.ndarray with shape (1, m) containing the
                activated output of the neuron for each example
        """
        m = Y.shape[1]
        j = -(1/m)*np.sum(Y*np.log(A) + (1-Y) * np.log(1.0000001-A))
        return j
