import unittest
import lib.vector as v

class TestVectorLibrary(unittest.TestCase):
  def test_add(self):
    self.assertEqual(v.add([1, 2, 3], [4, 5, 6]), [5, 7, 9])

  def test_add_assertion(self):
    with self.assertRaises(AssertionError) as context:
      v.add([1, 2], [4, 5, 6]), [1]
    self.assertEqual(str(context.exception), v.ERROR_LENGTH)
  
  def test_subtract(self):
    self.assertEqual(v.subtract([5, 7, 9], [4, 5, 6]), [1, 2, 3])

  def test_subtract_assertion(self):
    with self.assertRaises(AssertionError) as context:
      v.subtract([4, 5, 6], [1, 2])

    self.assertEqual(str(context.exception), v.ERROR_LENGTH)

  def test_sum(self):
    self.assertEqual(v.vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]), [16, 20])

  def test_sum_empty(self):
    with self.assertRaises(AssertionError) as con:
      v.vector_sum([])
    self.assertEqual(str(con.exception), v.ERROR_NO_VECTORS)
    with self.assertRaises(AssertionError) as con:
      v.vector_sum(None)
    self.assertEqual(str(con.exception), v.ERROR_NO_VECTORS)

  def test_sum_size(self):
    with self.assertRaises(AssertionError) as con:
      v.vector_sum([[1, 2], [3]])
    self.assertEqual(str(con.exception), v.ERROR_LENGTH)

  def test_multiply(self):
    self.assertEqual(v.scalar_multiply(2, [1, 2, 3]), [2, 4, 6])

  def test_mean(self):
    self.assertEqual(v.vector_mean([[1, 2], [3, 4], [5, 6]]), [3, 4])

  def test_dot(self):
    self.assertEqual(v.dot([1, 2, 3], [4, 5, 6]), 32)

  def test_dot_assert(self):
    with self.assertRaises(AssertionError) as con:
      v.dot([1, 2, 3], [4, 5])

    self.assertEqual(str(con.exception), v.ERROR_LENGTH)

  def test_sum_of_squares(self):
    self.assertEqual(v.sum_of_squares([1, 2, 3]), 14)

  def test_magnitude(self):
    self.assertEqual(v.magnitude([3, 4]), 5)
