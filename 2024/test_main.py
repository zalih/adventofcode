import unittest
import logging
import inspect


from main import day01p1, day01p2, day02p1, day03p1, day03p2, day04p1, day04p2, day05p1, day05p2, day06p1, day06p2, \
    day07p1, operator_combinations


class TestDay01(unittest.TestCase):

    def log_testcase_name(self, param_name):
        logging.info("****** TC: " + param_name + " ******")

    # unit tests
    def test_func(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(day01p1("data/day01/test.txt"), 11)
        self.assertEqual(day01p2("data/day01/test.txt"), 31)
        self.assertEqual(day02p1("data/day02/test.txt"), 2)
        self.assertEqual(day02p1("data/day02/test.txt", True), 4)
        self.assertEqual(day03p1("data/day03/test.txt"), 161)
        self.assertEqual(day03p2("data/day03/test2.txt"), 48)
        self.assertEqual(day04p1("data/day04/test.txt"), 18)
        self.assertEqual(day04p2("data/day04/test2.txt"), 9)
        self.assertEqual(day05p1("data/day05/test.txt"), 143)
        # self.assertEqual(day05p1("data/day05/input.txt"), 6505)
        self.assertEqual(day05p2("data/day05/test.txt"), 123)
        # self.assertEqual(day05p2("data/day05/input.txt"), 6897)
        self.assertEqual(day06p1("data/day06/test.txt"), 41)
        # self.assertEqual(day06p1("data/day06/input.txt"), 5177)
        # self.assertEqual(day06p2("data/day06/test.txt"), 6)
        # self.assertEqual(day06p2("data/day06/input.txt"), 1686)
        self.assertEqual(day07p1("data/day07/test.txt", ['+', '*']), 3749)
        # self.assertEqual(day07p1("data/day07/input.txt", ['+', '*']), 7579994664753)
        # self.assertEqual(operator_combinations(['*', '+'], 4), 2**4)
        self.assertEqual(day07p1("data/day07/test.txt", ['+', '*', '#']), 11387)
        # self.assertEqual(day07p1("data/day07/input.txt", ['+', '*', '#']), 438027111276610)





if __name__ == 'test_main':
    logging.basicConfig(filename='./test_main.log', format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filemode='w', level=logging.INFO)

    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay01)
    # unittest.TextTestRunner(verbosity=2).run(suite)
