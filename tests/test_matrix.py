import unittest
import lib.matrix as m

class TestMatrixLibrary(unittest.TestCase):
  def test_shape(self):
    self.assertEqual(m.shape([[1, 2, 3], [4, 5, 6]]), (2, 3))

  def test_shape_empty(self):
    self.assertEqual(m.shape([]), (0, 0))

  def test_get_row(self):
    self.assertEqual(m.get_row([[1, 2, 3], [4, 5, 6]], 0), [1, 2, 3])

  def test_get_column(self):
    self.assertEqual(m.get_column([[1, 2, 3], [4, 5, 6]], 1), [2, 5])

  def test_make_matrix(self):
    matrix = m.make_matrix(2, 3, lambda i, j: i*j)
    output = [[0, 0, 0],
              [0, 1, 2]]
    self.assertEqual(matrix, output)

  def test_identity_matrix(self):
    identity = [[1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]]
    self.assertEqual(m.identity_matrix(5), identity)
