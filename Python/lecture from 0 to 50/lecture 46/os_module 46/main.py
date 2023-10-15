import os
#  os.mkdir("lecture 46")#This will create folder  
# if (not os.path.exists("lecture 46")):#If the file not created than create file
#   os.mkdir("lecture 46")#This will create folder  

# for i in range(0,10):#This will create folder from 0 or 1 to any range which use will enter.
    #It will create multiple folders in a second
    # os.mkdir(f"lecture 46/Day{i+1}")#lecture 46 is folder name .In lecture 46 create  ten folders
# for i in range(0,10):
#     # os.rename(f"lecture 46/Day{i+1}",f"lecture 46/Tutorial{i+1}")#This module will rename the folder
#     os.rename(f"lecture 46/Tutorial{1+i}",f"lecture 46/Tutorial {1+i}")

#If we want to print folder
# folders=os.listdir("lecture 46")
# print(folders)

# for folder in folders:
#     print(folder)#It will show folder in single single line
#     print(os.listdir(f"lecture 46/{folder}"))#If we want to see in which folder file is there use this .

#If we want to see the directory in which folder is there
print(os.getcwd())

#If we want to change directory than use this.
os.chdir("change directory name")
print(os.getcwd())#If we want to see the directory in which folder is there
