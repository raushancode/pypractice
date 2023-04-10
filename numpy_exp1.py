import numpy
x, y = input().split(" ")
m = int(x)
n = int(y)
arr = numpy.empty((m, n), dtype=int)
for i in range(m):
  a = input().split(" ")
  for j in range(n):
    arr[i, j] = int(a[j])

my_array = numpy.sum(arr, axis = 0)
print(numpy.prod(my_array, axis = 0))