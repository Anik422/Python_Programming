def number_sum(*num):
    initial = 1
    for i in num:
        initial *= i
    return initial
    # print(initial)




print(number_sum(5,8,4,5,4,5,6,5))
