# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

def CountingSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('Array is not array')
   if type(typeOfSort) is not int: raise Exception('Type of sort is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")

   count = []
   maxElem = max(array)

   for i in range(0 , maxElem + 1):
      count.append(0)

   for i in array:
      count[i] = count[i] + i

   

   return array