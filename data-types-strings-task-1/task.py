from fractions import Fraction
def get_fractions(a_b: str, c_b: str) -> str:

    a_b = Fraction(a_b)
    c_b = Fraction(c_b)
    result = Fraction(a_b + c_b)
    final_result = "{} + {} = {}".format(a_b, c_b, result)
    return final_result

