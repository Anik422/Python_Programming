
#kono akti set ar modhe kono data besi bar
# thakle set sei data ke akti dore ney

s1 = {1,2,3,4,5}
s2 = {3,2,1,6,7}
s3 = {3,5,1,7,9}
'''
    three set common value !
'''
s4 = s1.intersection(s2,s3)
print("S1-S2-S3 intersection = ",s4)
'''
    s1 & s2 difference value ! 
'''
s5 = s1.difference(s2)
print("S1-S2-S3 difference value print :",s5)
#Two set union!
#common value and uncommon value print
result = s1.union(s3) # use union or |
#exm:  a|b = set a and set b ar value gulo ke union korbe
print("S1 - S2 union =",result)

#symmetric_difference holo duita set ar modhe jegula common value nai sei gula basai kore
s6 = s1.symmetric_difference(s2)
print("s1 & s2 symmetric_difference value print :",s6)

s7 = [2,3,4,5,6,8,2] #list
print(type(s7)) #data type
s8 = set(s7) #list convert to set
print("list convert to set =",s8)
