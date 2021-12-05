"""Subtraction Class"""

from App.calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        difference = self.values[0]
        for value in self.values[1:]:
            difference -= value
        return difference
