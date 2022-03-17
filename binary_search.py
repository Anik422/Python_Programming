#binary search function
def binary_search(li, n, x):
    first = 0
    lest = n-1
    #while loop condition setup
    while first <= lest:
        middle = (first + lest) // 2
        if li[middle] == x:
            return middle
        if li[middle] < x:
            first = middle+1    #first new value defiant
        else:
            lest = middle-1     #lest new value defiant
    return -1 #defualt return value
# input array size
num = int(input("Enter list elements number :"))
list1 = [] #defianed array
# input array element
for i in range(0,num):
    list1.append(int(input(f"Enter {i} index input number :")))
# input search element
search_element_value = int(input("Enter search value : "))
# function call
result = binary_search(list1,len(list1),search_element_value)
# condition check and index number print
if result == -1:
    print("Element is not present in list :",search_element_value)
else:
    print("Element is present at index =",result)