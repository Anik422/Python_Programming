# any_str = 'Hello python'
# print(any_str[:])
l1 = [2,4,3]
l2 = [5,6,4]

st1 = ''
st2 = ''
li1 = []
for i in l1:
    st1 = st1 + str(l1[i])
# print(st1)
for i in l2:
    st2 = st2 + str(l2[i])
# print(st2)
conv_st1 = int(st1)
conv_st2 = int(st2)
sum_num = conv_st1+conv_st2
str_sum = str(sum_num)
for i in range(len(str_sum)):
    li1.append(int(str_sum[i]))
# print(li1)
li1.reverse()
print(li1)