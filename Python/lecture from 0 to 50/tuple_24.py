'''Tuple is not changeable.In tuple the value is only One then if we print tuple type it will print 
integer . '''
tup1=(1,)#Using comma is will print type tuple and without comma it will print type integer
tup=(5,6,9,True)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-1])
print(tup[:3])
print(tup[0:])
if 9 in tup:
    print("It is present in the tuple")