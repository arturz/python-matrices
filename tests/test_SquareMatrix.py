from unittest import TestCase
from matrix.operations import SquareMatrix
from helpers.utils import make_list, mock_input, assert_output


class TestSquareMatrix(TestCase):
    @mock_input(make_list("""
        5
        1  4 -5  6  9
        0  4 -4  0  0
        -2 0  2  0 -2
        1  2  1 -3  4
        5 -2  2  0  0
    """))
    @assert_output(["2640.0"])
    def test_calculate_determinant(self):
        print(SquareMatrix().prompt_values().get_determinant())

    @mock_input(make_list("""
        2
        9 6
        12 8
    """))
    @assert_output(["0.0"])
    def test_calculate_determinant_2(self):
        print(SquareMatrix().prompt_values().get_determinant())

    @mock_input(make_list("""	
        4
        3 4 5 9
        -3 -4 -5 10
        0 0 0 -19
        2 3 4 5
    """))
    @assert_output(["0.0"])
    def test_calculate_determinant_3(self):
        print(SquareMatrix().prompt_values().get_determinant())

    @mock_input(make_list("""
        1
        4
    """))
    @assert_output(["4.0"])
    def test_calculate_determinant_4(self):
        print(SquareMatrix().prompt_values().get_determinant())

    @mock_input(make_list("""
        3
        3 8 1
        -4 1 1
        -4 1 1
    """))
    @assert_output(["0.0"])
    def test_calculate_determinant_5(self):
        print(SquareMatrix().prompt_values().get_determinant())

    @mock_input(make_list("""
        4
        1 2 3 0
        -1 2 -2 -5
        0 -1 0 2
        4 1 2 -1
    """))
    @assert_output(make_list("""
        0.0 0.33 1.0 0.33
        0.8 1.33 3.4 0.13
        -0.2 -1.0 -2.6 -0.2
        0.4 0.67 2.2 0.07
    """))
    def test_analytical_inversion(self):
        SquareMatrix().prompt_values().invert(method="analytical").print_values()

    @mock_input(make_list("""
        2
        9 6
        12 8
    """))
    @assert_output([SquareMatrix.CANNOT_BE_INVERTED])
    def test_analytical_inversion_2(self):
        SquareMatrix().prompt_values().invert(method="analytical").print_values()

    @mock_input(make_list("""
        4
        2 -5 -1 1
        -1 0 -1 0
        -4 1 -1 0
        3 4 2 -1
    """))
    @assert_output(make_list("""
        1.0 0.0 1.0 1.0
        3.0 -1.0 4.0 3.0
        -1.0 -1.0 -1.0 -1.0
        13.0 -6.0 17.0 12.0
    """))
    def test_analytical_inversion_3(self):
        SquareMatrix().prompt_values().invert(method="analytical").print_values()

    @mock_input(make_list("""
        1
        4
    """))
    @assert_output(["0.25"])
    def test_analytical_inversion_4(self):
        SquareMatrix().prompt_values().invert(method="analytical").print_values()