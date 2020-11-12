import random

def isDesSorted(array):
   """
   Проверяет убывающая ли последовательность
   """
   for i in range(0, len(array) - 1):
      if array[i] < array[i + 1]: return False
   
   return True

def isAscSorted(array):
   """
   Проверяет убывающая ли последовательность
   """
   for i in range(0, len(array) - 1):
      if array[i] > array[i + 1]: return False
   
   return True

# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

def BogoSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('Array is not array')
   if type(typeOfSort) is not int: raise Exception('Type of sort is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")

   if typeOfSort:
      while not isAscSorted(array):
         random.shuffle(array)
   else:
      while not isDesSorted(array):
         random.shuffle(array)
   
   return array