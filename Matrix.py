import numpy as np

m1 = ([2,5,8],
      [7,4,1],
      [9,6,3]
      )
m2 = ([7,8,9],
      [4,5,6],
      [3,2,1]
      )
print(f"Matrix 1 =\n{m1[0]}\n{m1[1]}\n{m1[2]}\n\n")
print(f"Matrix 2 =\n{m2[0]}\n{m2[1]}\n{m2[2]}\n\n")
result = np.add(m1, m2)
print("Matrix addition =\n",result,end="\n\n\n")
result1 = np.subtract(m1, m2)
print("Matrix subtract =\n",result1,end="\n\n\n")
result2 = np.dot(m1, m2)
print("Matrix multiply  =\n",result1,end="\n\n\n")


