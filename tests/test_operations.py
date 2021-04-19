from unittest import TestCase
from matrix.operations import BasicOperations, ReducedRowEchelonForm
from helpers.utils import make_list, mock_input, assert_output


class TestBasicOperations(TestCase):
    @mock_input(make_list("""
        2 3
        1 3 -2
        2 -4 5
        2 3
        -1 8 3
        -6 3 2
    """))
    @assert_output(make_list("""
        0j (11+0j) (1+0j)
        (-4+0j) (-1+0j) (7+0j)
    """))
    def test_matrix_addition(self):
        m1 = BasicOperations().prompt_values()
        m2 = BasicOperations().prompt_values()
        m1.sum(m2).print_values()

    @mock_input(make_list("""
        2 2
        1 2
        -2 0
         2 4
        1 -2 -1 3
        0 -1 2 -2
    """))
    @assert_output(make_list("""
        (1+0j) (-4+0j) (3+0j) (-1+0j)
        (-2+0j) (4+0j) (2+0j) (-6+0j)
    """))
    def test_matrix_multiplication(self):
        m1 = BasicOperations().prompt_values()
        m2 = BasicOperations().prompt_values()
        m1.mulmat(m2).print_values()

    @mock_input(make_list("""
        3 2
        1j 1-1j
        2-3j 4
        1-3j 4+2j
        2 2
        1 -1j
        1+1j 4-1j
    """))
    @assert_output(make_list("""
        (2+1j) (4-5j)
        (6+1j) (13-6j)
        (3+3j) (15+3j)
    """))
    def test_matrix_multiplication_2(self):
        m1 = BasicOperations().prompt_values()
        m2 = BasicOperations().prompt_values()
        m1.mulmat(m2).print_values()

    @mock_input(make_list("""
        4
        4 2
        2 -3
        3 5
        0.5 -2
        -1 0
    """))
    @assert_output(make_list("""
        (8+0j) (-12+0j)
        (12+0j) (20+0j)
        (2+0j) (-8+0j)
        (-4+0j) 0j
    """))
    def test_scalar_multiplication(self):
        scalar = int(input())
        m1 = BasicOperations().prompt_values()
        m1.mulsca(scalar).print_values()

    @mock_input(make_list("""
        2 5
        3 4 -2 -4 1
        6 -2 -1 6 9
    """))
    @assert_output(make_list("""
        (3+0j) (6+0j)
        (4+0j) (-2+0j)
        (-2+0j) (-1+0j)
        (-4+0j) (6+0j)
        (1+0j) (9+0j)
    """))
    def test_transpose(self):
        m1 = BasicOperations().prompt_values()
        m1.tran().print_values()

    @mock_input(make_list("""
        2 3
        1j 2 3
        2+3j 5 -1j
    """))
    @assert_output(make_list("""
        -1j (2-3j)
        (2-0j) (5-0j)
        (3-0j) 1j
    """))
    def test_conjugate_transpose(self):
        m1 = BasicOperations().prompt_values()
        m1.herm().print_values()

    @mock_input(make_list("""
        3 2
        2 6
        3 7
        4 8
        3 2
        3 2
        9 5
        1 8
    """))
    @assert_output([BasicOperations.WRONG_OPERATION])
    def test_matrix_multiplication_wrong_operation(self):
        m1 = BasicOperations().prompt_values()
        m2 = BasicOperations().prompt_values()
        m1.mulmat(m2).print_values()


class TestReducedRowEchelonForm(TestCase):
    @mock_input(make_list("""
        3 4
        4 2 4 12
        2 1 4 7
        2 1 0 5
    """))
    @assert_output(make_list("""
        1.0 0.5 0.0 2.5
        0.0 0.0 1.0 0.5
        0.0 0.0 0.0 0.0
    """))
    def test_reduced_row_echelon_form(self):
        ReducedRowEchelonForm().prompt_values().make().print_values()

    @mock_input(make_list("""
        3 4
        4 2 4 12
        2 1 4 7
        2 1 0 5
    """))
    @assert_output(["2"])
    def test_reduced_row_echelon_form_rank(self):
        ReducedRowEchelonForm().prompt_values().make().print_rank()
