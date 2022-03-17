def silection_sort(a, n):
    for j in range(0, n):
        index_min = j
        for k in range(j+1, n):
            if a[k] < a[index_min]:
                index_min = k

        if index_min != j:
            temp = a[j]
            a[j] = a[index_min]
            a[index_min] = temp




array_size = int(input("Enter array size :"))
arry = []
for i in range(0,array_size):
    arry.append(int(input(f"Element number {i+1} = ")))


array_length = len(arry)

silection_sort(arry,array_size)


for i in range(0,array_length):
    print(f"{i} index in value = {arry[i]}")