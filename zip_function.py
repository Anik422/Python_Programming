parson_name = ['Anik','Onmpy','Apon','Durjoy']
parson_age = [20,25,23,13]

parson_all_info = list(zip('1234',parson_name, parson_age))
print("Parson all info convert list :",parson_all_info)
print(type(parson_all_info))
parson_all_info_unzip = list(zip(*parson_all_info))
print("all parson info unzip list :",parson_all_info_unzip)
print(f"all parson info unzip :\n{parson_all_info_unzip[0]}\n{parson_all_info_unzip[1]}\n{parson_all_info_unzip[2]}")