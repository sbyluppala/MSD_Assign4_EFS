
from unittest import TestSuite, TestLoader, TextTestRunner

from TestCases.efs_admin import admin
from TestCases.efs_customer import customer
from TestCases.efs_investments import investment
from TestCases.efs_stocks import stocks


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(admin),
        loader.loadTestsFromTestCase(investment),
        loader.loadTestsFromTestCase(stocks),
        loader.loadTestsFromTestCase(customer),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

