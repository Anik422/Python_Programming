# def DecimalToBinary(num):
#         if num >= 1:
#             DecimalToBinary(num//2)
#             print (num % 2,end='')
# DecimalToBinary(10)

def ChangeHex(n):
    if n<0:
        return 0
    elif n<=1:
        return n
    else:
        # ChangeHex(n/16)
        x = n%16
        if x<10:
            return x
        elif x==10:
            return 'A'
        elif x==11:
            return 'B'
        elif x==12:
            return 'C'
        elif x==13:
            return 'D'
        elif x==14:
            return 'E'
        elif x==15:
            return 'F'

print(ChangeHex(16))