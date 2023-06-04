#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        returns the product of two conformable matrices in a lazy way
    """

    return (np.matmul(m_a, m_b))
