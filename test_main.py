import unittest
import logging
import inspect

from main import part_one
from main import part_two
from main import dive
from main import dive_aim
from main import power_consumption


class TestDay01(unittest.TestCase):
    def log_testcase_name(self, param_name):
        logging.info("****** TC: " + param_name + " ******")

    # unit tests
    def test_part_one(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(part_one("data/day01/test.txt"), 7)

    def test_part_two(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(part_two("data/day01/test.txt"), 5)

    def test_dive(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(dive("data/day02/test.txt"), 150)

    def test_dive_aim(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(dive_aim("data/day02/test.txt"), 900)

    def test_power_consumption(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(power_consumption("data/day03/test.txt"), 198)


if __name__ == 'test_main':
    logging.basicConfig(filename='./test_main.log', format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filemode='w', level=logging.INFO)

    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay01)
    unittest.TextTestRunner(verbosity=2).run(suite)
