import numpy as np

#  3 Dimensional Array

arr3 = np.array([[[8,6],[7,4]],[[9,3],[10,8]]])

# no.sort()
print(np.sort(arr3))

#np.where()
arr3_nn = np.array([[[8,4],[7,4]],[[9,4],[4,8]]])

x = np.where(arr3_nn == 4)

print(x)