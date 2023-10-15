# Given two integer numbers,
# return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1=int(input("Enter the number 1 :"))
num2=int(input("Enter the number 2 :"))

if (num1 *num2) <=1000:
    print("The result is :",num1 *num2)
else:
    print("The result is :",num1+num2)