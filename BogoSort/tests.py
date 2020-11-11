from main import BogoSort
import unittest

class BubbleSortTests(unittest.TestCase):
   
   def test_fullArray_ascending(self):
      self.assertEqual(BogoSort([9, 7, 5, 8], 1), [5, 7, 8, 9])
      self.assertEqual(BogoSort([1, 3, 5, 8], 1), [1, 3, 5, 8])
      self.assertEqual(BogoSort([1, 3, 3, 8, 4], 1), [1, 3, 3, 4, 8])
      self.assertEqual(BogoSort([1, 2, 3], 1), [1, 2, 3])
      self.assertEqual(BogoSort([7, 6, 5, 4], 1), [4, 5, 6, 7])
   
   def test_fullArray_descending(self):
      self.assertEqual(BogoSort([9, 7, 5, 8], 0), [9, 8, 7, 5])
      self.assertEqual(BogoSort([1, 3, 5, 8], 0), [8, 5, 3, 1])
      self.assertEqual(BogoSort([1, 3, 3, 8, 4], 0), [8, 4, 3, 3, 1])
      self.assertEqual(BogoSort([1, 2, 3], 0), [3, 2, 1])
      self.assertEqual(BogoSort([7, 6, 5], 0), [7, 6, 5])

   def test_emptyArray(self):
      self.assertEqual(BogoSort([], 0), [])
      self.assertEqual(BogoSort([], 1), [])

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v tests.py