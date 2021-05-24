import unittest

# import your test modules
import test_ComplexMatrixWithOps
import test_ReducedRowEchelonForm
import test_TriangularMatrix
import test_SquareMatrix

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_ComplexMatrixWithOps))
suite.addTests(loader.loadTestsFromModule(test_ReducedRowEchelonForm))
suite.addTests(loader.loadTestsFromModule(test_TriangularMatrix))
suite.addTests(loader.loadTestsFromModule(test_SquareMatrix))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)