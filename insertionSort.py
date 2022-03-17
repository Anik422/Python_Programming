def insertion_sort(user_input_array,size_of_array):
    for k in range(1,size_of_array):
        item = user_input_array[k]
        j = k-1
        while j >= 0 and user_input_array[j] < item:
            user_input_array[j+1] = user_input_array[j]
            j = j- 1
        user_input_array[j+1] = item

array_size = int(input("Enter array size :"))
number_array = []
for i in range(0, array_size):
    number_array.append(int(input(f"Element # {i+1} :")))
insertion_sort(number_array,array_size)
for i in range(0,array_size):
    print(f"{i} index value : {number_array[i]}")