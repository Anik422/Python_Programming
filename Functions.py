num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

def number_of_sum(x, y):
    return x+y
def number_of_sub(x,y):
    return x-y
def number_of_mul(x,y):
    return x*y
def number_of_div(x, y):
    return x/y
result1 = number_of_sum(num1, num2)
print(f"The result is sum {result1}")

result4 = number_of_sub(num1, num2)
print(f"The result is sub :{result4}")

result2 = number_of_mul(num1, num2)
print(f"The result is sub :{result2}")

result3 = number_of_div(num1, num2)
print(f"The result is Div :{result3}")

result5 = number_of_sum(result1, result4)
print(f"result1 and result2 sum is :{result5}")



# # import only system from os
# from os import system, name
#
# # import sleep to show output for some time period
# from time import sleep
#
#
# # define our clear function
# def clear():
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')
#
#
# # print out some text
# print('hello geeks\n' * 10)
#
# # sleep for 2 seconds after printing output
# sleep(10)
#
# # now call function we defined above
# clear()