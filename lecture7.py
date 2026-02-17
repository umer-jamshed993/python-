#lecture no 7 is file input output
#python can be used to perform operations on a file (read and write)
#types of all files 
#1 text files :.txt,.docx,.log
#binary files:. .mp4,.mov,.png,.jpeg etc
#we have to open a file before read it or write it
#f=open("demo.txt","r")
#data = f.read()
#print(data)
#print(type(data))
#f.close()


#f = open("iii.py","r")
#data = f.read()
#print(data)
#print(type(data))
#f.close()



#we can specify the number of charecters to be printed on a screen
#f = open("demo.txt","r")
#data = f.read(5)
#print(data)
#print(type(data))
#f.close()



#we can read one line at a time 
#data = f.readline()
#f = open("demo.txt","r")
#line1 = f.readline()
#print(line1)
#line2 = f.readline()
#print(line2)
#line3 = f.readline()
#print(line3)


#f = open("demo.txt","r")
#data = f.read()
#print(data)
#print(type(data))
#f.close()


#f = open("demo.txt","r")
#data = f.read(6)
#print(data)
#print(type(data))
#f.close()



#f = open("demo.txt","r")
#line1 = f.readline()
#print(line1)
#line2 = f.readline()
#print(line2)
#line3 = f.readline()
#print(line3)
#line4 = f.readline()
#print(line4)
#f.close()



#w is used to write a data in a file 
#writing to a file
#f = open("demo.txt","r")
#data = f.read()
#print(data)
#print(type(data))
#f.close()


#f = open("demo.txt","r")
#data = f.read()
#print(data)
#print(type(data))
#f.close()


#f = open("demo.txt","w")
#f.write("i want to be succesful")
#f.close()


#f = open("demo.txt","w")
#f.write("i wil go to python documentary after shradha lectures")
#f.close()

#f= open("demo.txt","a")
#f.write("\n i will do it anyway")
#f.write("\nmy name is umer jamshed")
#f.close()

#in file w is a function that overwrite in a file in a place of older one 
#but a is an append function that is used to add a text in a file 
#r is used to only read a code and print it

#if we want to create any file by using a code in python
#then we can use both w and a

#f = open("sample.txt","w")
#f.close()



#f = open("sampl.txt","a")
#f.close()


#if we want to read and write simultaneously :
#f = open("demo.txt","r+")
#f.write("abc")
#print(f.read())
#f.close()

#the r + is used to read and write simultaneously but the words we write will replace with characters  that were written  in same numbers
#the w+ mode we se that when we read anything in w+ the whole file is truncated and in write mode we can write anything
#f = open("demo.txt","w+")
#print(f.read())
#f.write("my name is umer jamshed ")
#f.close()

#a+ is used to read a code same as it and also used to write another thing in it
#f = open("demo.txt","a+")
#print(f.read())
#f.write("my name is malik umer")
#f.close()


#with syntax in python 
#with open ("demo.txt","r")as f:
#    data = f.read()
#    print(data)

#with open("demo.txt","w") as f:
#    f.write("new data")

#f = open("demo.txt","w")
#data =f.write("i am umer jamshaid")
#print(data)
#f.close()


#f = open("demo.txt","r")
#data = f.read(8)
#print(data)
#f.close()



#f = open("demo.txt","a")
#data = f.write("\n i am a programmer")
#print(data)
#f.close()


#f = open("demo.txt","r+")
#data = f.read()
#f.write("\n i am umer")
#f.close()


#f = open("demo.txt","w+")
#data = f.read()
#data = f.write("\n i will be successful one day")
#f.close()


#f = open("demo.txt","a+")
#data =f.read()
#print(data)
#f.write("\n i am learning python from sharadha didi")
#f.close()

#with open("demo.txt","w")as f:
#    data = f.write("\n i will be sucessful onr day")
#    print(data)
#    f.close()


#with open("demo.txt","a")as f:
#    f.write("\n i am umer jamshaid")
#    f.close()



#now we are discussing about deleting a file in python
#by using an os  module  
#module(like a code library)is a file written by another programmer that generally has a functions we have use


#import os 
#os.remove(file name)
#import os
#pip install tensor flow
#pip3 install tensor flow
#import os


#os.remove("iii.py")
#a program used to delete a file

#practice a program 
#create a new fie "practice.txt"using python.add a folowing data in it
#hi everyone
#we are learning file i /o
#using java
#i like programming in java


with open("simple.txt","w")as f:
    f.write("i am umer\n i am learning java\nfrom apna college\ni am busy in java")
    
