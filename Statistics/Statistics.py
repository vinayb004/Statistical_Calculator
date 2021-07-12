from Calculator.Calculator import Calculator
from Statistics.Mean import get_mean
from Statistics.Median import get_median
from Statistics.Mode import get_mode

class Statistics(Calculator):

    def __init__(self):
        pass

    def stats_mean(self, data):
        self.result = get_mean(data)
        return self.result

    def stats_median(self, data):
        data.sort()
        self.result = get_median(data)
        return self.result

    def stats_mode(self, data):
        self.result = get_mode(data)
        return self.result