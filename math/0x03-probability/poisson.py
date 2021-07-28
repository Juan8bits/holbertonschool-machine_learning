#!/usr/bin/env python3
""" Class to represent a poisson distribution
"""


class Poisson:
    """ Class that represent a poisson distribution
    """
    def __init__(self, data=None, lambtha=1.):
        """ Constructor

        Args:
            data (list): Is a list of the data to be used to estimate
                the distribution. Defaults to None.
            lambtha (float): The expected number of occurences in a
                given time frame. Defaults to 1..
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        elif not isinstance(data, list):
            raise TypeError('data must be a list')
        elif not len(data) > 1:
            raise ValueError('data must contain multiple values')
        else:
            self.lambtha = sum(data) / len(data)
