from unittest import TestCase
from matrix.operations import ReducedRowEchelonForm
from helpers.utils import make_list, mock_input, assert_output


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