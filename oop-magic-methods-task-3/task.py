from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    value_in_euro = None
    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        exchange_rate = cls.value_in_euro / other_cls.value_in_euro
        return "{} {} for 1 {}".format(exchange_rate, other_cls.abbreviation, cls.abbreviation)

    def to_currency(self, other_cls: Type[Currency]):
        exchange_rate = self.value_in_euro / other_cls.value_in_euro
        converted_value = self.value * exchange_rate
        return other_cls(converted_value)

    def __add__(self, other_cls: Type[Currency]):
        other_value_in_self_currency = other_cls.value * other_cls.value_in_euro / self.value_in_euro
        new_value = self.value + other_value_in_self_currency
        return self.__class__(new_value)

    def __eq__(self, other_cls: Type[Currency]) -> bool:
        return self.value * self.value_in_euro == other_cls.value * other_cls.value_in_euro

    def __lt__(self, other_cls: Type[Currency]) -> bool:
        return self.value * self.value_in_euro < other_cls.value * other_cls.value_in_euro

    def __gt__(self, other_cls: Type[Currency]) -> bool:
        return self.value * self.value_in_euro > other_cls.value * other_cls.value_in_euro


class Euro(Currency):
    value_in_euro = 1
    abbreviation = "EUR"
    def __str__(self):
        return "{} {}".format(self.value, self.abbreviation)


class Dollar(Currency):
    value_in_euro = 0.5
    abbreviation = "USD"
    def __str__(self):
        return "{} {}".format(self.value, self.abbreviation)


class Pound(Currency):
    value_in_euro = 0.01
    abbreviation = "GBP"
    def __str__(self):
        return "{} {}".format(self.value, self.abbreviation)


print(
      f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
      f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
      f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
)

e = Euro(100)
r = Pound(100)
d = Dollar(200)
print(
      f"e = {e}\n"
      f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
      f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
      f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
  )
print(
      f"r = {r}\n"
      f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
      f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
      f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
  )

print(
      f"e + r  =>  {e + r}\n"
      f"r + d  =>  {r + d}\n"
      f"d + e  =>  {d + e}\n"
  )