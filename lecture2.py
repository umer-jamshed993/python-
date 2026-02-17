#strings and conditional statements in this lecture 
#string is a data type that store a sequence of charecters 
str1 = "this is a string "
str2 = "food club"
str3 = """this is the world"""

str1 = "this is a string .we are creating it in python"
print(str1)

#now we are using backslash \n 
str1 = "this is a string .\nwe are creating it in python "
print(str1)
#now writin \t 
str1 = "this is a string .\twe are creating it in python"
print(str1)

#now discussing basic operations 
# no 1 is concatenation 
str1= "punjab"
str2= "college"
final_str = str1 + str2
print(final_str)

#no 2 is length of a string 
str1 = "punjab"
len1 = len(str1)
str2 = "college"
len2 = len(str2)
print(len1,len2)


str1 = "punjab"
str2 = "college"
final_str = str1 + str2 
print(len(final_str))

#indexing 
#indexing 
#indexing 
#indexing 
str = "apna college"
ch = str[8]
print(ch)
str = "apna college"
print(str[8])


#slicing concept in python 
#accessing parts of a string 
#str[starting_idx:ending_idx]#ending index is not included 
str = "punjab college"
print(str[5:8])
print(str[7:14])

str = "apna college "
print(str[4:])   #it means we are goin from a selecting starting character to the end character

str = "apna college "
print(str[:4]) # when we are not selecting a starting character it means we already selested the peice of string if we dont write any number before ratio sign and write a sign after ratio sign 
  



#negative index in slicing 
#it means we can get a piece of string through negative index
#it will start from less numbers to a greater numbers like from -3 to -1
str = "apple"
print(str[-5:-3])
print(str[-5:-1])

# now we are discussing string functions
#like str = "i am a coder"
#str.capitalize() #capitalizes first character
#str.endwith("er.")#returns true if string ends with substr
#str.replace(old,new)#replaces all occurences of old with new
#str.find(word)#returns 1st index of 1 st occurences 
#str.count("am")#counts the occurence of substr in string

#1st string is #str.endwith("er.")
str = "i am studying python"
print(str.endswith("hon"))
#if we write pyt it willshow false as  result

#2nd function is capitalize function
str = "punjab college"
print(str.capitalize())#this function capitalizes the first character of a word in string

#3 rd is replace function str.repplace(old,new)#replaces all occurences of old with new
str = "python language"
print(str.replace("o","a"))

#4th one is str.find(word)to search for a word in a string where there this is exists 1 st time its starting index print to us 
str = "punjab college"
print(str.find("o"))

str = "panaversity"
print(str.find("y"))#if we write an unknown character in a string then the index print is -1 unknown character for

#5th funcion that we are discussing is str.count("am")#counts the occurences of substr
str = "i am studying python"
print(str.count("from"))#it counts how much time we are writing a single word multiple times
print(str.count("o"))
print(str.count("y"))


#write my program for practice
#1 wap to input user's first name and print its length 
name = input("enter your name:")
print("length of your name is :",len(name))

#wap to find the occurences of '$' in  a string 
str = "hi,$ i am a $ symbol 99$"
print(str.count("$"))


#a concept of conditional statements 
#if elif statement syntax
#if(condition):
#   statement 1
#elif (condition):
#   statement 2 
#else:
#   statementN 
#FOR EXAMPLE 
age = 21 
if(age>=18):
    print("can vote and apply for a license ")
    print("can drie a car")
    print("can study in usa")


light = "green"
if (light == "red" ):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
print("end of a code")#we can write many if and many elif in our code

#actually if statements always execute but elif execute only when if condition is false

#program 

num = 5 
if (num>2):
    print("number is greater than 2")
if(num>3):
    print("greater than 3")#if we write at 2nd if as elif then only first if will execute only 
#the last condition which is left is called else condition and we will apply it only when both if and elif are false and are not able to apply in a code 

light = "pink" 
if (light == "red"):
    print("stop")
elif (light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")

#2nd program 
age = 14 
if(age>=18):
    print("you can vote")
else:
    print("you cannot vote")
    #the space in the above print statements is called indentation which os called a proper space 

#example to understand the conditional statements
#grade students based on their marks 
marks = 78 
if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks <80):
    grade = "C"
else:
    grade = "D"
                        
print("grade of the student:",grade)  



#again practice 
marks = 89
if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("grade of the student is :",grade) 


#now we are going to understand nested statements
#an if statement in another if statement is called nested if statement
age = 95
if (age>=18):
    if(age>=80):
        print("you can not drive")
    else:
        print("you can drive") 

else:
    print("you can not drive")

#practice questions
#wap to input if the number entered by a user is odd or even
num = (input("enter number:"))
rem= num %2
if(rem ==0):
    print("Even")
else:
    print("Odd")

#Again
num = (input("enter number"))
rem = num % 2
if(rem==0):
    print("Even")
else:
    print("Odd")

#write a program  to find a gretest of three numbers entered by the user
a = (input("enter first number"))
b = (ipnut("enter second number:"))
c = (input("enter third number:"))
if(a>=b and a>=c):
    print("first number is laresrt")
elif(b>=c and b>=a):
    print("second number is largest")
else:
    print("third number is largest")

print("hello world")
