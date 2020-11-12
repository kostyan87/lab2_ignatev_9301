from main import BubbleSort
import unittest

class BubbleSortTests(unittest.TestCase):
   
   def test_fullArray_ascending(self):
      self.assertEqual(BubbleSort([9, 7, 5, 8], 1), [5, 7, 8, 9])
      self.assertEqual(BubbleSort([1, 3, 5, 8], 1), [1, 3, 5, 8])
      self.assertEqual(BubbleSort([1, 3, 3, 8, 4, 78, 66, 10, 10], 1), [1, 3, 3, 4, 8, 10, 10, 66, 78])
      self.assertEqual(BubbleSort([1, 2, 3, 4, 5, 6, 7], 1), [1, 2, 3, 4, 5, 6, 7])
      self.assertEqual(BubbleSort([7, 6, 5, 4, 3, 2, 1], 1), [1, 2, 3, 4, 5, 6, 7])
      self.assertEqual(BubbleSort([7, -8, 5, -894], 1), [-894, -8, 5, 7])
      self.assertEqual(BubbleSort([-7, -6, -5, -4], 1), [-7, -6, -5, -4])
      self.assertEqual(BubbleSort([7, -6], 1), [-6, 7])
   
   def test_fullArray_descending(self):
      self.assertEqual(BubbleSort([9, 7, 5, 8], 0), [9, 8, 7, 5])
      self.assertEqual(BubbleSort([1, 3, 5, 8], 0), [8, 5, 3, 1])
      self.assertEqual(BubbleSort([1, 3, 3, 8, 4, 78, 66, 10, 10], 0), [78, 66, 10, 10, 8, 4, 3, 3, 1])
      self.assertEqual(BubbleSort([1, 2, 3, 4, 5, 6, 7], 0), [7, 6, 5, 4, 3, 2, 1])
      self.assertEqual(BubbleSort([7, 6, 5, 4, 3, 2, 1], 0), [7, 6, 5, 4, 3, 2, 1])
      self.assertEqual(BubbleSort([7, -8, 5, -894], 0), [7, 5, -8, -894])
      self.assertEqual(BubbleSort([-7, -6, -5, -4], 0), [-4, -5, -6, -7])
      self.assertEqual(BubbleSort([7, -6], 0), [7, -6])

   def test_emptyArray(self):
      self.assertEqual(BubbleSort([], 0), [])
      self.assertEqual(BubbleSort([], 1), [])

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v tests.py