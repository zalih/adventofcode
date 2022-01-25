import unittest
import logging
import inspect

from main import part_one
from main import part_two


class MediasortOutput(unittest.TestCase):
    def log_testcase_name(self, param_name):
        logging.info("****** TC: " + param_name + " ******")

    # unit tests
    def test_part_one(self):
        self.log_testcase_name(inspect.currentframe().f_code.co_name)
        self.assertEqual(part_one("test.txt"), 7)
        self.assertEqual(part_two("test.txt"), 5)


if __name__ == '__main__':
    logging.basicConfig(filename='./test_main.log', format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filemode='w', level=logging.INFO)

    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MediasortOutput)
    unittest.TextTestRunner(verbosity=2).run(suite)