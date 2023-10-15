#Dictionary items are the key value pair that are sperated by commas and encloses with curle braket{}
#dictionary are ordered collection of data items
# dic={
#     "Momin":"Taufeeq",
#     "Uzair":"pagal"
# }
# dic={
#     568:"Momin",
#     65:"Taufeeq",
#     23:"Uzair"
# }
# print(dic[23])
info={'name':'Taufeeq','age':19,'eligible':True}
print(info["name"])
# print(info['name2'])#It show an error
print(info.get("name2"))#It show the output is None
print(info.keys())
print(info.values())
for key in info.keys():#Keys ko iterate karke value ko le shakte hai
    print(info[key])
print(info.items())#It will show the key value pairs
for key,value in info.items():
    print(f"This is corresponding key {key} and {value}")