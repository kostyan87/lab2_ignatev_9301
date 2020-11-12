# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

def check(array):
   for i in array:
      if i < 0:
         return True
   return False

def CountingSort(array, typeOfSort):
   
   if type(array) is not list: raise Exception('Array is not array')
   if type(typeOfSort) is not int: raise Exception('Type of sort is not integer')
   if (typeOfSort < 0) or (typeOfSort > 1): raise Exception("Incorrect type of sort")
   if check(array): raise Exception("Negative number in array")

   resultArr = []
   count = []
   if len(array) > 0:
      maxElem = max(array)
   else:
      return array

   for i in range(0 , maxElem + 1):
      count.append(0)

   for i in array:
      count[i] = count[i] + 1

   for i in range(0, len(count)):
      while count[i] > 0:
         resultArr.append(i)
         count[i] -= 1

   if typeOfSort: return resultArr
   return resultArr[::-1]