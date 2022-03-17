


number = [1,2,3,4,5]
print("unpacking : ",*number)
values = [*range(7), *"hello"]
print(values)
values1 = [*number, "a", *values, *"hello"]
print("two list unpack =",values1)
# print(type(values))
# dict unpacking
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 5}
print(combined)