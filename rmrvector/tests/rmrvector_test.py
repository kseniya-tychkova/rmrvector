# -*- coding: utf-8 -*-

import pytest
from rmrvector import rmrvector


@pytest.mark.parametrize('data, valid_vec', [
    ([1, 3], [1, 1, 1]),
    ([2, 2, 5, 1], [2, 2, 5])
])
def test_check_vec_initialization(data, valid_vec):
    """ Test checks that we can correctly uncompress vectors. """

    vec = rmrvector.Vector(data)

    # uncompress vector:
    full_vec = [x for x in vec]

    # check that result is correct:
    assert full_vec == valid_vec


@pytest.mark.parametrize('data1, data2, expected_result', [
    ([1, 3], [1, 2], 2),
    ([2, 2, 5, 1], [2, 2, 1, 1], 13),
    ([0, 4], [6, 2, 7, 2], 0),
    ([-1, 2, 2, 1], [-5, 3], 0)
])
def test_check_multiply_vectors(data1, data2, expected_result):
    """ Test checks that we can multiply vectors. """

    res = rmrvector.scalar_product(data1, data2)

    # check that result is correct:
    assert res == expected_result
