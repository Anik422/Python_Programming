list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7, 4]
list1.extend(list2)
print(list1)
print("List1 id number :",id(list1))
print(type(list1))
print(list1)
print ("list1[0]: ", list1[0])
print(type(list))
print("List2 id number :",id(list2))
print(list2)
print ("list2[1:5]: ", list2[1:5])
n = int(input("Enter  count value :"))
print(list2.count(n))
m = int(input("Enter remove List index Number :"))
list2.remove(list2[m])
print(list2)