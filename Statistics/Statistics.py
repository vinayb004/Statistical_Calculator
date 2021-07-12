from Calculator.Calculator import Calculator
from Statistics.Mean import get_mean

class Statistics(Calculator):

    def __init__(self):
        pass

    def stats_mean(self, data):
        self.result = get_mean(data)
        return self.result