n,m = map(int , input().split(' '))

for i in range(1, n, 2):
    print(str('.|.' * i).center(m, '-'))
print('Welcome'.center(m,'-'))
for j in range(n-2, -1, -2):
    print(('.|.'*j).center(m,'-'))



    # print("\n")