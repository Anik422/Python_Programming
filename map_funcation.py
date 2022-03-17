items = [
    (12,"Product1"),
    (78,"Product2"),
    (45,"Product4"),
    (89,"Product5"),
    (64,"Product6"),
    (10,"Product7")
]
price = list(map(lambda item : item[0], items))
price.sort()
price.reverse()
print(price)
