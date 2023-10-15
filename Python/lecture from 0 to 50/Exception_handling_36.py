# n=input("ENter the number :")
# print(f"Multiplecation of {n} is :")
# try:
#   for i in range(1,11):
#      print(f"{int(n)} X {i} = {int(n)*i}")
# # except Exception as e:
# #     print(e)
# except:#We can use like this also
#    print("Invalid output")
   
# print("Momin Taufeeq")
# print("Something error")   
try:
   num=int(input("Enter the number "))
   a=[6,4]
   print(a[num])
except ValueError:
   print("This error is value error")
except IndexError:
   print("This error is Index error")

   


