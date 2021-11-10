""" calculation division class"""
from calc.calculations.calculation import Calculation
class Division(Calculation):
    """ calculation division class"""
    def get_result(self):
        """returns  division results"""
        value_quotient = self.values[0]
        for value in self.values[1:]:
            value_quotient  /= value
        return value_quotient
