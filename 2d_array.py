import numpy
from numpy import *
ary1 = array([
    [2,5,8,3,6,8],
    [7,4,1,2,5,8]
])
# ary2 = array([])
# print(dir(ary1))
print(ary1.size)
print(numpy.sum(ary1))
# print(numpy.swapaxes(ary1, ary2))
print(ary1)
print("dimensional  array :",ary1.ndim)
print("array shape",ary1.shape)
print("data type :",ary1.dtype)
print(type(ary1))
array2 = ary1.flatten()
print("2D array convert to 1D array :",array2)
array3 = array2.reshape(2,6)
print("1D array convert to 2D array :",array3)
print("dimensional  array :",array3.ndim)
array4 = array2.reshape(2, 2, 3)
# assert isinstance(array4, object)
print("1D array convert to 3D array :",array4)
print("dimensional  array :",array4.ndim)