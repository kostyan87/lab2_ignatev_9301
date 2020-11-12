from main import CountingSort
import unittest

class BubbleSortTests(unittest.TestCase):
   
   def test_fullArray_ascending(self):
      self.assertEqual(CountingSort([9, 7, 5, 8], 1), [5, 7, 8, 9])
      self.assertEqual(CountingSort([1, 3, 5, 8], 1), [1, 3, 5, 8])
      self.assertEqual(CountingSort([1, 3, 3, 8, 4, 78, 66, 10, 10], 1), [1, 3, 3, 4, 8, 10, 10, 66, 78])
      self.assertEqual(CountingSort([1, 2, 3, 4, 5, 6, 7], 1), [1, 2, 3, 4, 5, 6, 7])
      self.assertEqual(CountingSort([7, 6, 5, 4, 3, 2, 1], 1), [1, 2, 3, 4, 5, 6, 7])
   
   def test_fullArray_descending(self):
      self.assertEqual(CountingSort([9, 7, 5, 8], 0), [9, 8, 7, 5])
      self.assertEqual(CountingSort([1, 3, 5, 8], 0), [8, 5, 3, 1])
      self.assertEqual(CountingSort([1, 3, 3, 8, 4, 78, 66, 10, 10], 0), [78, 66, 10, 10, 8, 4, 3, 3, 1])
      self.assertEqual(CountingSort([1, 2, 3, 4, 5, 6, 7], 0), [7, 6, 5, 4, 3, 2, 1])
      self.assertEqual(CountingSort([7, 6, 5, 4, 3, 2, 1], 0), [7, 6, 5, 4, 3, 2, 1])

   def test_emptyArray(self):
      self.assertEqual(CountingSort([], 0), [])
      self.assertEqual(CountingSort([], 1), [])

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v tests.py