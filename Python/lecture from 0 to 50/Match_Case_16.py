x=int(input("Enter the value :"))
match x:
    case 0:
        print("It is zero")
    case 4:
        print("It is equal to four")
    case _ if x != 90:
        print("Not equal to ninty")
    case _ if x !=80:
        print("Not equal to Eighty")
    
    case _:
        print("It is not equal ")
