def mul_number(number):
    return number * 5

list1 =[2,8,7,9,7,6]
result = list(map(mul_number,list1))
sorted(result)
print(result)