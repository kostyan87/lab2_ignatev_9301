def BinarySearch(array, item):

   if type(array) is not list: raise Exception('"array" is not array')
   if type(item) is not int: raise Exception('"item" is not integer')

   low = 0
   high = len(array) - 1
   while low <= high:
      mid = int((high + low) / 2)
      guess = array[mid]
      if guess == item:
         return mid
      if guess > item:
         high = mid - 1
      else:
         low = mid + 1
   return None