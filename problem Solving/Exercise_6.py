# Iterate the given list of numbers and print only those numbers which are divisible by 5
ls=[20,33,65,90,48]
for i in range(0,len(ls)):
     if(ls[i]%5==0):
      print(ls[i])
     else:
      print("Not Divisible")