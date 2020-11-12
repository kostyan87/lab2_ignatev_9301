import timeit

fullTime = 0

for i in range(10):
   code_to_test = """

from main import BubbleSort
import random

# To change the number of elements in the array, change the number in range ()
array = [random.randint(-100000, 100000) for i in range(100000)]

BubbleSort(array, 1)

   """

   time = timeit.timeit(code_to_test, number=1)/1
   fullTime = fullTime + time
   print("run time:", time)

print("middle time:", fullTime / 10)