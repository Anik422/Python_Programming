student = {1:{'name':'Anik Saha','age': 25, 'sex':'male'},
           2:{'name':'apon Saha','age': 28, 'sex':'male'},
           3:{'name':'Durjoy Saha','age': 20, 'sex':'male'}
           }
print(f"\n\nFull student Nested Dictionary print : {student}\n")
print(f"One Studen Data print : {student[2]}\n")
print(f"number 3 student age print : {student[3]['age']}\n")
student[4]={}
student[4]['name'] ='Laxmi Saha'
student[4]['age'] = 5
student[4]['sex'] ='female'
print(f"New student data add student Dictionary :{student[4]}\n")
print(f"Check full student Dictionary : {student}\n")
del student[1]
print(f"Delete student data 1 check student all data : {student}\n")
del student[3]['name']
print(f"Delete 3 number student name check all new data : {student}\n")