s1={5,6,8,3,9}
s2={2,4,10,8,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
s3={"saudi","turkey","India","china"}
s4={"Pakistan","saudi","America","turkey"}
# print(s3.intersection(s4))
# s3.intersection_update(s4)#In this s3 is update the value is common of both object
# print(s3)
# s5=s3.symmetric_difference(s4)
# print(s5)

# s5=s3.difference(s4)#In this it will only check in s3 and if the value is common in both set it will not .print the value which is not comman
# print(s5)
# s5=s3.isdisjoint(s4)#in s3 is common with another set than it will return tha false.If there is common in both the set it will return true
# print(s5)
# s5=s3.issuperset(s4)
city={"saudi","turkey","India"}
# print(s3.issuperset(city))#if the set value is same to another set value it will return true
# print(s5)
# print(city.issubset(s3))
# city.add("England")
# print(city)
# city.update(s3)
# print(city)
# city.remove("England")#If the value is not there it show an error
# print(city)
# city.discard("England4")#If the value is not there it does not show an error
# print(city)
# item=city.pop()
# print(city)
# print(item)
# del city#It will delete set 
# city.clear()#It will clear the set and it become an emty set
# print(city)
info={"Momin",1,True,4.9}
if "Momin1" in info:
    print("Momin is preasent")
else:
    print("Momin is not preasent")


