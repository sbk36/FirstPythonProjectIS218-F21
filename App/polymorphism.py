"""This shows example polymorphism"""

from calc.addition import Addition
from calc.subtraction import Subtraction

obj_add = Addition(1.0,2.0)
obj_sub = Subtraction(2.0,1.0)

for obj_calc in (obj_add, obj_sub):
    """This shows how we can use same obj_calc object to call two different methods"""
    print(obj_calc.getresult())
