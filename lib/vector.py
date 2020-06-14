from typing import List
import math

ERROR_LENGTH = "Vectors must be the same length"
ERROR_NO_VECTORS = "No Vectors Provided"

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
  assert len(v) == len(w), ERROR_LENGTH
  return [x+y for x,y in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
  assert len(v) == len(w), ERROR_LENGTH

  return [x-y for x,y in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
  assert vectors, ERROR_NO_VECTORS

  n = len(vectors[0])
  assert all(len(v) == n for v in vectors), ERROR_LENGTH

  return [sum(vector[i] for vector in vectors) for i in range(n)]

def scalar_multiply(c: float, vector: Vector) -> Vector:
  return [c*v for v in vector]

def vector_mean(vectors: List[Vector]) -> Vector:
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector):
  assert len(v) == len(w), ERROR_LENGTH

  return sum(x*y for x,y in zip(v, w))

def sum_of_squares(v: Vector) -> float:
  return dot(v, v)

def magnitude(v: Vector) -> float:
  return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
  return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
  # return math.sqrt(squared_distance(v, w))
  return magnitude(subtract(v, w))
