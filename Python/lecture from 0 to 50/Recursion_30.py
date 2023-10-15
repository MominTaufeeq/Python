def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
print(factorial(3))
print(factorial(5))

#Fabinacci Sequence
n=5
n1=0
n2=1
count=0
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1
    

    
 