import pytest
from ..__main__ import setdis


def test_case_1():
    assert setdis(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [
            'pop',
            'remove 9',
            'discard 9',
            'discard 8',
            'remove 7',
            'pop ',
            'discard 6',
            'remove 5',
            'pop ',
            'discard 5'
        ]
    ) == 4
