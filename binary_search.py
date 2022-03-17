def binary_search(array_num, size_of_array, find_number):
    index_first = 0
    index_last = size_of_array - 1
    while index_first <= index_last:
        index_mid = (index_first + index_last) // 2
        if array_num[index_mid] == find_number:
            return index_mid
        if array_num[index_mid] < find_number:
            index_first = index_mid + 1
        else:
            index_last = index_mid - 1
    return -1
def selection_sort(array_number, size_of_array):
    for j in range(0, size_of_array):
        index_min = j
        for k in range(j+1, size_of_array):
            if array_number[k] < number_array[index_min]:
                index_min = k
        if index_min != j:
            temp = array_number[j]
            array_number[j] = array_number[index_min]
            array_number[index_min] = temp

array_size = int(input("Enter array size :"))
number_array = []
for i in range(array_size):
    number_array.append(int(input(f"Element # {i+1} : ")))

selection_sort(number_array, array_size)
# print(number_array)
search_number = int(input("Enter search number :"))
search_number_index = binary_search(number_array, array_size, search_number)
if search_number_index == -1:
    print(f"{search_number} is not find array.")
else:
    print(f"{search_number} index number {search_number_index}")