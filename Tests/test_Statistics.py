import unittest
from Statistics.Statistics import Statistics
import random
import statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(5)
        self.testData = []
        for i in range(0, 10):
            num = random.randint(0, 15)
            self.testData.append(num)

        self.mean_value = statistics.mean(self.testData)
        self.median_value = statistics.median(self.testData)
        self.mode_value = statistics.mode(self.testData)
        self.variance_value = statistics.variance(self.testData)
        self.standard_deviation_value = statistics.stdev(self.testData)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.stats_mean(self.testData)
        self.assertEqual(mean, self.mean_value)

    def test_median_calculator(self):
        median = self.statistics.stats_median(self.testData)
        self.assertEqual(median, self.median_value)

    def test_mode_calculator(self):
        mode = self.statistics.stats_mode(self.testData)
        self.assertEqual(mode, self.mode_value)

    def test_median_calculator(self):
        median = self.statistics.stats_median(self.testData)
        self.assertEqual(median, self.median_value)

    def test_mode_calculator(self):
        mode = self.statistics.stats_mode(self.testData)
        self.assertEqual(mode, self.mode_value)

    def test_variance_calculator(self):
        variance = self.statistics.stats_variance(self.testData)
        self.assertEqual(variance, round((self.variance_value), 1))

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.stats_standard_deviation(self.testData)
        self.assertEqual(standard_deviation, round((self.standard_deviation_value), 1))


if __name__ == '__main__':
    unittest.main()
