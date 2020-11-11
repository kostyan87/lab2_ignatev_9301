# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

def BubbleSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('Array is not array')
   if type(typeOfSort) is not int: raise Exception('Type of sort is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")

   border = len(array) - 1
   if typeOfSort == 0:
      for i in range(0, len(array) - 1):
         for i in range(0, border):
            if array[i] < array[i + 1]:
               array[i], array[i + 1] = array[i + 1], array[i]
         border -= 1
   else:
      for i in range(0, len(array) - 1):
         for i in range(0, border):
            if array[i] > array[i + 1]:
               array[i], array[i + 1] = array[i + 1], array[i]
         border -= 1
   
   return array