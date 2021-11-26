"""This is the multiplication calculation that is being inherits
the value A and value B from the calculation class"""

from calc.calculation import Calculation

#This is how you extend the multiplication class with the Calculation
class Multiplication(Calculation):
    """The multiplication class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getresult(self):
        """get result"""
        return self.value_a * self.value_b
