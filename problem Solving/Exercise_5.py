# Write a function to return True if the first and last number of a given list is same.
#  If numbers are different then return False.


def lf(l1):
    if l1[0] == l1[-1]:
        return True
    else:
        return False
    
l2=[50,60,30,90,70,50]
l3=[50,60,30,90,70,90]

print(lf(l2))
print(lf(l3))

    