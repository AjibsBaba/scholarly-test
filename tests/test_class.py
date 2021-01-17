import pytest
from scripts.main import calculate_liquid_volume as clv


def check_inputs(i=2, j=3, k=2.3):
    """
    Test Case to Confirm if the input validation is functioning
    :param i: Number of Rows
    :param j: Number of Glasses
    :param k: Amount of liquid
    :return:
    """
    if j > i:
        with pytest.raises(ValueError):
            "Invalid Input"
    elif i or j or k != float or int:
        with pytest.raises(ValueError):
            "Invalid Input"
    else:
        assert clv(i, j, k)


def calculate_volume(i=2, j=2, k=2.0):
    """
    Test Case to check the function
    :param i: Number of Rows
    :param j: Number of Glasses
    :param k: Amount of liquid
    :return: Amount of liquid in Jth jug
    """
    res = clv(i, j, k)
    assert res
