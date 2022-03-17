from unicodedata import numeric


number = [1,1,2,3,4,5]
first = set(number)
second = {1,6}


print(first | second)
print(first & second)
print(first - second)
print(first ^ second)