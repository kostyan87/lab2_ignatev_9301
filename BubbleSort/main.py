# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

def BubbleSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('"array" is not array')
   if type(typeOfSort) is not int: raise Exception('"item" is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")

   if typeOfSort == 0:
      for i in range(0, len(array) - 1):
         for i in range(0, len(array) - 1):
            if array[i] < array[i + 1]:
               array[i], array[i + 1] = array[i + 1], array[i]
   else:
      for i in range(0, len(array) - 1):
         for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
               array[i], array[i + 1] = array[i + 1], array[i]
   
   return array

print(BubbleSort([1, 3, 0, 7, 5, 3, 88, 14, 12], 1))