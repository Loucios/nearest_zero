import unittest

from solution.solution import NearestZero


class Test(unittest.TestCase):
    def test_nearest_zero(self):
        tests_map = (
            {'count': 5, 'cells': [0, 1, 4, 9, 0], 'result': [0, 1, 2, 1, 0]},
            {'count': 6, 'cells': [0, 7, 9, 4, 4, 8, 20],
             'result': [0, 1, 2, 3, 4, 5]},
        )
        for case in tests_map:
            n, c, r = case.values()
            with self.subTest('test_nearest_zero'):
                self.assertEqual(r, NearestZero(n, c).get_result())
