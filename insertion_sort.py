def insertion_sort(number_of_array,size_of_array):
    for j in range(1,size_of_array):
        item = number_of_array[j]
        k = j - 1
        while k >= 0 and number_of_array[k] > item:
            number_of_array[k+1] = number_of_array[k]
            k = k -1
        number_of_array[k+1] = item


Array_size = int(input("Enter array size :"))
number_list = []
for i in range(0,Array_size):
    number_list.append(int(input(f"Element # {i+1} :")))
insertion_sort(number_list,Array_size)
print("\n")
for i in range(0,Array_size):
    print(f"{i} index value : {number_list[i]}")