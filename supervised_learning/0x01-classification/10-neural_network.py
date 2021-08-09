#!/usr/bin/env python3
"""  Neural Network Class
"""
import numpy as np


class NeuralNetwork:
    """ Defines a neural network with one hidden layer performing
        binary classification.
    """
    def __init__(self, nx, nodes):
        """ Method to instantiates a Neural Network

        Args:
            nx (int): Number of input features.
            nodes (int): Number of nodes found in the hidden layer.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')
        self.__W1 = np.random.normal(0, 1, (nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(0, 1, (1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Getter method that returns the value of the attribute "W1".
        """
        return self.__W1

    @property
    def b1(self):
        """ Getter method that return the value of the attribute "b1".
        """
        return self.__b1

    @property
    def A1(self):
        """ Getter method that return the value of the attribute "A1".
        """
        return self.__A1

    @property
    def W2(self):
        """ Getter method that return the value of the attribute "W2".
        """
        return self.__W2

    @property
    def b2(self):
        """ Getter method that return the value of the attribute "b2".
        """
        return self.__b2

    @property
    def A2(self):
        """ Getter method that return the value of the attribute "A2".
        """
        return self.__A2

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
        preactivation_1 = (self.W1 @ X) + self.b1
        activation_1 = 1 / (1 + np.exp(-preactivation_1))
        preactivation_2 = (self.W2 @ activation_1) + self.b2
        activation_2 = 1 / (1 + np.exp(-preactivation_2))
        self.__A1 = activation_1
        self.__A2 = activation_2
        return self.A1, self.A2
