from unittest import TestCase
from matrix.operations import TriangularMatrix
from helpers.utils import make_list, mock_input, assert_output


class TestTriangularMatrix(TestCase):
    @mock_input(make_list("""
        3
        3 0 0
        0 4 0
        0 0 -19/59
    """))
    @assert_output(make_list("""
        0.33 0.0 0.0
        0.0 0.25 0.0
        0.0 0.0 -3.11
    """))
    def test_invert_diagonal_matrix(self):
        TriangularMatrix().prompt_values().invert().print_values()

    @mock_input(make_list("""
        4
        1 0 0 0
        2 1 0 0
        3 -2 1 0
        4 1 -5 1
    """))
    @assert_output(make_list("""
        1.0 0.0 0.0 0.0
        -2.0 1.0 0.0 0.0
        -7.0 2.0 1.0 0.0
        -37.0 9.0 5.0 1.0
    """))
    def test_invert_lower_triangular_matrix(self):
        TriangularMatrix().prompt_values().invert().print_values()

    @mock_input(make_list("""
        4
        3 0 0 0
        6 -2 0 0
        4 8 4 0
        5 1 6 2
    """))
    @assert_output(make_list("""
        0.33 0.0 0.0 0.0
        1.0 -0.5 0.0 0.0
        -2.33 1.0 0.25 0.0
        5.67 -2.75 -0.75 0.5
    """))
    def test_invert_lower_triangular_matrix_2(self):
        TriangularMatrix().prompt_values().invert().print_values()

    @mock_input(make_list("""
        4
        5 4 -1 2
        0 -1 2 6
        0 0 1/3 4
        0 0 0 2
    """))
    @assert_output(make_list("""
        0.2 0.8 -4.2 5.8
        0.0 -1.0 6.0 -9.0
        0.0 0.0 3.0 -6.0
        0.0 0.0 0.0 0.5
    """))
    def test_invert_upper_triangular_matrix(self):
        TriangularMatrix().prompt_values().invert().print_values()

    @mock_input(make_list("""
        4
        3 0 0 0
        6 0 0 0
        4 8 4 0
        5 1 6 2
    """))
    @assert_output([TriangularMatrix().CANNOT_BE_INVERTED])
    def test_cannot_be_inverted(self):
        TriangularMatrix().prompt_values().invert().print_values()