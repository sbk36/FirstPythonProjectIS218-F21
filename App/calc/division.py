"""This is the Division calculation that is being inherits
the value A and value B from the calculation class"""
#this is called a namespace it is like files and folders the
# classes are files and the folders organize the classes
#It looks like a folder and file path but it is
# sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#This is how you extend the Division class with the Calculation
class Division(Calculation):
    """The Division class has one method to get the
    result of the the calculation A and B come from
    the calculation parent class"""
    def getresult(self):
        """get result"""
        return self.value_a / self.value_b
