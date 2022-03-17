items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 33),
]
price = list(map(lambda item : item[1], items))
print("Use lambda = ",price)
price1 = [item[1] for item in items]
print("Use for loop =", price1)

filtered = list(filter(lambda item1 : item1[1] >= 10, items))
print("Use filter = ",filtered)
filtered1 = [item for item in items if item[1] >= 10]
print("use for loop =",filtered1)
