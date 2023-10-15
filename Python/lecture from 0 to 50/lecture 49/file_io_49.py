'''Before we can perform any operations on a file, we must first open it.
 Python provides the open() function to open a file. 
 It takes two arguments: the name of the file and the mode in which the file should be opened.
 The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.'''
#Reading File 
# f= open('myfile249.txt','w')
# # print(f)
# text=f.read()
# print(text)
# f.close()

'''There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).'''

# f= open('myfile49.txt','rb')
# text=f.read()
# print(text)
# f.close()

# Wrinting File
f=open('myfile249.txt','a')#If we use a it will append it add text in file
f.write("Hello World ")
f.close()

#If we use 'with' it will automatically close the file.
with open('myfile249.txt','a') as f:
    f.write("Hey I am inside the file")