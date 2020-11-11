from main import BinarySearch
import unittest

class BinarySearchTests(unittest.TestCase):
   
   def test_fullArray(self):
      self.assertEqual(BinarySearch([1, 3, 5, 8], 5), 2)
      self.assertEqual(BinarySearch([1, 3, 5, 8], 1), 0)
      self.assertEqual(BinarySearch([1, 3, 5, 8], 3), 1)
      self.assertEqual(BinarySearch([1, 3, 5, 8], 8), 3)

   def test_emptyArray(self):
      self.assertEqual(BinarySearch([], 5), None)

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v tests.py