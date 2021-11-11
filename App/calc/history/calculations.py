"""Calculation history Class"""
class Calculations:
    """ Calculations"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """ clear_history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """ count_history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """get_last_calculation """
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """ get_first_calculation"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)