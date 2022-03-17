import functools
def add_list(num1, num2):
    return num1 + num2
list1 = [1,2,3,4,5,6,7,8,9,10]
result = functools.reduce(add_list, list1)
print(result)