list_number = [5,4,9,7,2,13,4,56,87,99,32]
largest_number = list_number[0]

for item in list_number:
    if largest_number < item:
        largest_number = item
print(largest_number)