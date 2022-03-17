weight = int(input("Weight :"))
kye = input("(L)bs or (K)g :")
if kye.lower() == 'l':
    print(f"You are {weight *0.45} pounds")
elif kye.upper() == 'K':
    print(f"You are {weight / 0.45} kilogram.")