""" calculation division class"""
from App.calc.calculations.calculation import Calculation
class Division(Calculation):
    """ calculation division class"""
    def get_result(self):
        """returns  division results"""
        value_quotient = self.values[0]
        for value in self.values[1:]:
            try:
                value_quotient  /= value
            except ZeroDivisionError:
                value_quotient = "Not Divisible by Zero"
                print("Not Divisible by Zero")
        return value_quotient
