"""This is the Subtraction calculation that is being inherits
the value A and value B from the calculation class"""

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The Subtraction class has one method to get the
    result of the the calculation A and B come from
    the calculation parent class"""
    def getresult(self):
        """get result"""
        return self.value_a - self.value_b
