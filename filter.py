number = [1,2,3,4,5,6,8,7,9,5,4,1,12,54,-8,-87,-54,6]
filter_number = list(filter(lambda n : n%2!=0, number))
print(filter_number)