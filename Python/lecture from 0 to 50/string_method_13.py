#String are immmutable, It will create new String
a="!!!Momin !!!!!! Momin"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))# It will remove ! ,The ! is before the variable it will not remove
print(a.replace("Momin","Taufeeq"))
print(a.split(" "))#It will convert into a list
blog="introduction tO Python"
print(blog.capitalize())#it will convert the first letter capital and after the first letter itwill convert into lower
# str="welcoMe To vscodeHii !!!"
# print(len(str))
# print(str.center(21)) 
# print(a.count("Momin"))
# print(str.endswith("!!!"))
# print(str.endswith("to",4,10))
# print(str.find("to"))
# print(str.find("too"))#It will show output negative -1
# str1="WelcomeToVsCodeHii00"#In this the number,alphabet are there then show true else show false
# print(str1.isalnum())
# str2="WelcomeToVsCode"#In this only lower and upper are there the show true
# print(str2.isalpha())
# str3="welcome to vscode"
# print(str3.islower())
# str="welcom to vs code\n"#\n is not printable that why it show false
# print(str.isprintable())
# str="  "#using space bar or Tab
# print(str.isspace())
# str2="To Kil A Mocking Bird"
# print(str2.istitle())#Each character of first letter is capital it return True other wise it will show False
str="Python is a Interpreted language"
print(str.swapcase())#It will convert lower case into upper case and upper case into lower case
str="Python is a Interpreted language"
print(str.startswith("Python"))
str="He is Dan. Dan is honest man"
print(str.title())