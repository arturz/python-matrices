from unittest import TestCase
from matrix.operations import ComplexMatrixWithOps, ReducedRowEchelonForm, TriangularMatrix
from helpers.utils import make_list, mock_input, assert_output


class TestComplexMatrixWithOps(TestCase):
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
        m1 = ComplexMatrixWithOps().prompt_values()
        m2 = ComplexMatrixWithOps().prompt_values()
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
        m1 = ComplexMatrixWithOps().prompt_values()
        m2 = ComplexMatrixWithOps().prompt_values()
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
        m1 = ComplexMatrixWithOps().prompt_values()
        m2 = ComplexMatrixWithOps().prompt_values()
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
        m1 = ComplexMatrixWithOps().prompt_values()
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
        m1 = ComplexMatrixWithOps().prompt_values()
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
        m1 = ComplexMatrixWithOps().prompt_values()
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
    @assert_output([ComplexMatrixWithOps.WRONG_OPERATION])
    def test_matrix_multiplication_wrong_operation(self):
        m1 = ComplexMatrixWithOps().prompt_values()
        m2 = ComplexMatrixWithOps().prompt_values()
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

    @mock_input(make_list("""
        3 3
        -1 2 3
        4 1 6
        3 1 2
    """))
    @assert_output(make_list("""
        1.0 0.0 0.0
        0.0 1.0 0.0
        0.0 0.0 1.0
    """))
    def test_reduced_row_echelon_form_2(self):
        ReducedRowEchelonForm().prompt_values().make().print_values()

    @mock_input(make_list("""
        3 3
        -1 2 3
        4 1 6
        3 1 2
    """))
    @assert_output(["3"])
    def test_reduced_row_echelon_form_rank_2(self):
        ReducedRowEchelonForm().prompt_values().make().print_rank()

    @mock_input(make_list("""
        3 4
        0 -1 4 3
        2 -2 4 6
        3 -4 3 2
    """))
    @assert_output(make_list("""
        1.0 0.0 0.0 2.86
        0.0 1.0 0.0 2.71
        0.0 0.0 1.0 1.43
    """))
    def test_reduced_row_echelon_form_3(self):
        ReducedRowEchelonForm().prompt_values().make().print_values()

    @mock_input(make_list("""
        3 4
        0 -1 4 3
        2 -2 4 6
        3 -4 3 2
    """))
    @assert_output(["3"])
    def test_reduced_row_echelon_form_rank_3(self):
        ReducedRowEchelonForm().prompt_values().make().print_rank()

    @mock_input(make_list("""
        1 1
        0
    """))
    @assert_output(["0.0"])
    def test_reduced_row_echelon_form_4(self):
        ReducedRowEchelonForm().prompt_values().make().print_values()

    @mock_input(make_list("""
        1 1
        0
    """))
    @assert_output(["0"])
    def test_reduced_row_echelon_form_rank_4(self):
        ReducedRowEchelonForm().prompt_values().make().print_rank()


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