def fact(n):
    if n==1:
        return n
    else:
         return n * fact(n-1)

num1 = int(input("Enter any number :"))
result = fact(num1)
print(result)
