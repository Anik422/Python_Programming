d1={'anik':'saha',(1,3):'tapol','tapol1': (1,3),'age': 14,1:'anik saha'}
print("\nPrint Dictionary : ",d1,"\n")
d2 = d1.copy()
print("Copy D1 value :",d2,"\n")
print("Print dictionary tapol1 value :",d1['tapol1'],"\n")
d1['appol']='Iphone'
print("D1 a add appol value :",d1,"\n")

d1.pop('anik')
print("D1 pop \"Anik\": ",d1,"\n")
d1.clear()
print(f"d1 value clear :{d1}\n")
print(f"D1 item print :{d1.items()}\n")
print(f"D1 keys print :{d1.keys()}")


print(f"gat function use:{d1.get(1)}")

del d1
#print("delete d1 :",d1)
print("Delete done D1")