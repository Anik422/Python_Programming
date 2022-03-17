def bubble_sort(a, n):
    for j in range(0, n):
        for k in range(0, n-1-j):
            if a[k] > a[k+1]:
                temp = a[k]
                a[k] = a[k+1]
                a[k+1] = temp


num = int(input("Enter array size :"))
array = []
for i in range(0,num):
    array.append(int(input(f"{i+1} number value input :")))
array_length = len(array)
bubble_sort(array, array_length)
for i in range(0,array_length):
    print(f"{i} index for value :{array[i]}")