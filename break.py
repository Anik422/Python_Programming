available = 4
n = int(input("How many iphone do you need?\n "))
i=1
while i<=n:
    if i>available:
        print("Sorry ! out of stock.")
        break
    print("Iphone",i)
    i+=1
print("Thank you.")