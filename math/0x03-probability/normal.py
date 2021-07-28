#!/usr/bin/env python3
""" Class to represents a normal distribution.
"""


class Normal:
    """ Class to represents a normal distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """ Constructor

        Args:
            data (List): List of the data to be used to estimate
                the distribution. Defaults to None.
            mean (): Mean of the distribution. Defaults to 0..
            stddev (float): Standard deviation of the distribution.
                Defaults to 1..
        """
        if data is None:
            if stddev < 1:
                raise ValueError('stddev must be a positive value')
            self.stddev = float(stddev)
            self.mean = float(mean)
        elif not isinstance(data, list):
            raise TypeError('data must be a list')
        elif not len(data) > 1:
            raise ValueError('data must contain multiple values')
        else:
            self.mean = sum(data)/len(data)
            num = 0
            for i in data:
                num += (i - self.mean)**2
            self.stddev = (num/len(data)) ** (1/2)
