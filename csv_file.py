import  csv
# with open("data.csv", 'w') as file:
with open("data.csv") as file:
        Reader = csv.reader(file)
        # writer = csv.writer(file)
        # writer.writerow(['Transaction_id', 'product_id', "price"])
        # writer.writerow([1000, 1, 5])
        # writer.writerow([1001, 2, 15])
        print(list(Reader))
