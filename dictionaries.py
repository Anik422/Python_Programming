point = {"x" : 1, "y" : 2}
point = dict(x=1, y=2)
print(point)
point["x"] = 10
print(point)
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key in point.items():
    print(key)