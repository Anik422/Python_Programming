s1 = {1,2,3,4,5,6,6}
print(type(s1))
print("S1 =",s1)
s1.update([8,8,9,10])
s2 = {11,12,13,8}
print("s1 update =",s1)
s1.update(s2)
print("New Update =",s1)
#remove & discard same work but unknown value remove korar jono "remove" use korle program error dekhai
#Kintu 'discard' use a program error dekhai nah
s1.discard(20)
print("S1 remove Number 10 :",s1)