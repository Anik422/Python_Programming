invaied_id = [1001,1002,1003,1004,1005,1006,1007,1008]
search_id = int(input("Enter search id number :"))
arry_length = len(invaied_id)
count = 0
for i in range(0, arry_length):
    if invaied_id[i]==search_id:
        count = invaied_id[i]
if count == search_id:
    print(f"{search_id} You are Welcome.")
else:
    print(f"{search_id} You are not Welcome.")

