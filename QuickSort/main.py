# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

import time

start_time = time.time()

def QuickSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('Array is not array')
   if type(typeOfSort) is not int: raise Exception('Type of sort is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")

   if len(array) < 2:
      return array
   elif len(array) == 2: 
      if array[0] <= array[1]: return array
      else:
         array[0], array[1] = array[1], array[0]
         return array
      if array[0] >= array[1]: return array
      else:
         array[0], array[1] = array[1], array[0]
         return array
   else:
      mid = array[0]
      lessArr = []
      moreArr = []

      for i in array[1:]:
         if i <= array[0]: lessArr.append(i)
         else: moreArr.append(i)
      
      result = QuickSort(lessArr, 1) + [mid] + QuickSort(moreArr, 1)

      if typeOfSort: return result
      return result[::-1]