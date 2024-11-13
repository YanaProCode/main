from typing import Union
import math

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
  return round(result, 2)
