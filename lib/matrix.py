from typing import List, Tuple, Callable
from .vector import Vector

Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0

  return num_rows, num_cols

def get_row(A: Matrix, i: int) -> Vector:
  return A[i]

def get_column(A: Matrix, j: int) -> Vector:
  return [row[j] for row in A]

def make_matrix(num_rows: int, num_cols: int, fn: Callable[[int, int], float]) -> Matrix:
  return [[fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
  return make_matrix(n, n, lambda i,j: 1 if i==j else 0)
