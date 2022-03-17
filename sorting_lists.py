# items = [
#     ("Product1", 9),
#     ("Product2", 12),
#     ("Product4", 87),
#     ("Product5", 45),
#     ("Product6", 48),
#     ("Product7", 55),
# ]
#use user functuin
# def sort_item(item):
#     return item[1]
# items.sort(key=sort_item)


#use lambda function
# items.sort(key=lambda item : item[1])
# print(items)
items = [
    (12,"Product1"),
    (78,"Product2"),
    (45,"Product4"),
    (89,"Product5"),
    (64,"Product6"),
    (10,"Product7")
]

items.sort(key=lambda item : item[0])
print(items)