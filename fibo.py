n = int(input("Enter any integer number :"))
a = 0
b = 1
for i in range(0,n):
    print(a)
    temp = a + b
    a = b
    b =temp
    