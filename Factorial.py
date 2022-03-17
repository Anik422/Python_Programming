def factorial(n):
    initial =1

    for i in range(1,num+1): #use  for loop
        initial*=i
    return initial

# def factorial(n):
#     initial =1
#     i =1
#     while i<=n: #use while loop
#         initial*=i
#         i +=1
#     return initial


# def factorial(n):
#     initial =1
#
#     for i in range(num,0,-1): #use decrement for loop
#         initial*=i
#     return initial



#import math

num = int(input("Enter any integer number :"))
result = factorial(num) #use function
# result = 1
# for i in range(1,num+1):
#     result *= i
# result = math.factorial(num) #factroil() function use
print(f"{num} number of factorial = {result}")