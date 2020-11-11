# typeOfSort = 1 to sort in ascending order
# typeOfSort = 0 to sort in descending order

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
      
      if typeOfSort: return QuickSort(lessArr, 1) + [mid] + QuickSort(moreArr, 1)
      else: return QuickSort(lessArr, 0) + [mid] + QuickSort(moreArr, 0)

print(QuickSort([9, 7, 5, 8], 0))

# Какого то хрена не могу сделать сортировку по убыванию