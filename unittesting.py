import unittest
from recur_sum import recur_sum


class RecurSum(unittest.TestCase):
    def test_recur_sum_works_successfully(self):
        self.assertEqual(recur_sum([1, 2, 3, 4]), 10)
        self.assertEqual(recur_sum([1, 2, [3, 4]]), 10)
        self.assertEqual(recur_sum([1, 2, [3, 4, [5, 6]]]), 21)

    # def test_recur_sum_works_successfully(self):
        # self.assertEqual(recur_sum([1,2,3,-4]),-10)
        #self.assertEqual(recur_sum([1, -2, [3, 4]]), 6)
        #self.assertEqual(recur_sum([1, 2, [3, -4,[5,-6]]]), 1)


      if __name__ == "__main__":
 unittest.main()