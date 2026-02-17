#loops in python
#loops are used to repeat instructions 
#while loop is we are studying
count = 1
while count<=5:
    print("sindh")
    count+=1
    print(count)

number = 7
while number >=1:
    print("hello world")
    number-=1
    print(number)
    print("loop end")
    #we can also write
    print("hello world",number)
#syntax 
#while condition :
#same work
#while is a keyword
#variables are iteration in a program and teration used are called iteration process
#if we write 
#while true:
#condition then it will print infinite times  in aprogram
y = 100
while y>=1:
    print("umer",y)
    y-=1

x = 1 
while x<=1000:
    print("punjab",x)
    x+=1
    print(x)

#print numbers from 1 to 10
a = 1 
while a<=10:
    print(a)
    a+=1

 #print numbers from 10 to 1
b = 10
while b >=1:
    b-=1
    print(b)

#infinite print program
#l= 5
#while l<6
#print(l)
#i-=1
#the loop will print the result infinite times
    
#now we are practicing some programs 
o = 1
while o<=100:
    print(o)
    o+=1

#print numbers from 100 to 1
r = 100
while r>=1:
    print(r)
    r-=1  #while condition is a stopping condition


#print multiplication table of number n
i = 1 
while i <=10:
    print(3*i)
    i+=1

p =1
while p<=10:
    print(7*p)
    p+=1

#we are taking input from user and printing any number of table
n = int(input("enter number:"))
i = 1
while i <=10:
    print(n*i)
    i+=1


m = int (input("enter number :"))
i = 1
while i <=10:
    print("m *i")
    i+=1
#print the elements of a list following using a loop
nums = [1,4,9,16,25,36,49,64,81,100]
while idx < len(nums):
    print(nums(idx))
    idx+=1

# #WE ARE PRACTING PROGRAM NO 4 WHICH IS 
# #print the element of a following list using  a loop 
# #[1,4,9,16,25,36,49,64,81,100]
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx<len(num):
#     print(num[idx])
#     idx+=1

# num1 =[1,2,8,90,67,89,80,87,89,85]
# idx = 0 
# while idx <len(num1):
#     print(num1[idx])
#     idx+=1

# num2 = [1,2,3,4,5,67,8,9,90]
# idx = 0 
# while idx <len(num2):
#     print(num2[idx])
#     idx+=1

# heroes = ["ironman","thor","superman","batman"]
# idx = 0
# while idx <len(heroes):
#     print(heroes[idx])
#     idx+=1

# n= 2#we can also write(int(input("enter numbers:"))
# i = 1
# while(i<=10):
#     print(n*i)
#     i+=1

#search for a number x in this tuple using loop

#numbers = [1,4,9,16,25,36,49,64,81,100]
#x = 36
#idx = 0
#while idx < len(numbers):
#    if (numbers[idx]==x):
#        print ("found at idx ",idx)
#    idx+=1


#numbers = [1,2,3,4,5,78,98,90,780]
#x = 90
#i = 0
#while i <len(numbers):
#    if (numbers[i]==x):
#        print("found at i",i)
#    i+=1


#numbers = [1,45,67,89,90,98,87,83,79]
#x = 87
#i = 0 
#while i <len(numbers):
#    if(numbers[i]==x):
#        print("found at i",i)
#    i+=1

#nums = [1,56,67,78,89,90,54,45]
#x = 89
#i = 0
#while i <len(nums):
#    if(nums[i]==x):
#       print("found at i: ",i)#if we use break after this statement then the loop end 
#    else:
#        print("finding....")   
#    i+=1  


#n = [1,2,34,56,78,98,90]
#x = 90
#i = 0
#while i<len(n):
#    if(n[i]==x):
#        print("found at i",i)
#    else:
#        print("finding.....")
#    i+=1

#break statement
#break is used to terminate the loop when encountered 
#i = 1 
#while i <=5:
#    print(i)
#    if(i==3):
#        break
#    i+=1

#j = 1
#while j<=45:
#    print(j)
#    if(j==23):
#        break
#    j+=1



#p = 1 
#while p <=24:
#    print(p)
#    if(p==10):
#        break
#    p+=1
#print("end of loop")


#continue :
#continue is used to terminate the loop when encountered
#i = 0 
#while i<=5:
    
#    if(i==3):
#        i+=1
#        continue
#    print(i)
#    i+=1

#j = 0 
#while j <=6:
#    if (j==5):
#        j+=1
#        continue
#    print(j)
#    j+=1




#k = 1
#while k<=5:
#    if(k==4):
#        k+=1
#        continue
#    print(k)
#    k+=1


#again practice
#u = 0
#while u <=7:
#    if (u==5):
#        u+=1
#        continue
#    print(u)
#    u+=1

#y = 0 
#while y<=9:
#    if(y==8):
#        y+=1
#        continue
#    print(y)
#    y+=1

#in order to print odd numbers 
#d = 0
#while(d<=9):
#    if(d%2==0):
#        d+=1
#        continue
#    print(d)
#    d+=1

#if we print even numbers
#f = 0
#while f<=10:
#    if(f%2!=0):
#        f+=1
#        continue
#    print(f)
#    f+=1


#for loops :
#for loops are used for sequencial traversal.for traversing list ,string,tuples etc
#veggies = [ "potatoes","carrrots","brinjal","ladyfinger"]
#for val in veggies:
#    print(val)


#fruits = ["apple","mango","banana","pineapple"]
#for val in fruits:
#    print(val)

#for loos on tuples
#tup = {1,2,3,4,5,6,7,8,9}
#for num in tup:
#    print(num)

#name = "apna college"
#for char in name:
#    print(char)

#for loops          list = [1,2,3]
#for elm list:for el in list:
#some work      print (el)


#for loop with else   for el in list :
#for el in list:          print(el)
#some work           else:
#else:                    print("end")
#work when loop ends
#str = "apna college"
#for char in str:
#    if (char =='o'):
#        print("o found")
#        break
#    print(char)
#else:
#    print("END")



#str = "punjab college"
#for char in str:
#    if(char =='e'):
#        print("e found")
#        break
#    print(str)
#else:
#    print("end")
#else will not execte in the presence of break statement

#print the elements of a following list using a for loop
nums = [1,4,6,8,9,45,89,90]
for el in nums:
    print(nums)

num = {1,2,3,4,5,67,78}
x = 67
i = 0
for el in num:
    if (el ==x):
        print("number is found at idx",i)
    i+=1

nums = (1,2,3,4,5,6,7,8,9,98,87,86,85,84)
x = 85
idx = 0
for el in nums:
    if(el ==x):
        print("found at idx",idx)
    idx+=1

#search for a number x in this tuple using loop
numbers = [1000,456,678,789,987,876,654,543]
x = 789
idx = 0
for el in numbers:
    if(el ==x):
        print("found at idx",idx)
    idx+=1

#range functions 
#range functions return a sequence of numbers starting from 0 by default and increments by 1 by default and stops before a specified number
#range(start?,stop,step?)
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
#it was a type of manually printing anything
#if we print it in once
seq = range(8)
for el in seq:
    print(el)


rom = range(10)
for el in rom:
    print(el)
#summarize again
for el in range(101):
    print(el)

for i in  range (156):
    print(i)
#it is a way of writing a range function to print many numbers in a range 
#there are three ways of writing a range functions 
for i in range(10):
    print(i)        #it is number 1 way

for i in range(2,34):
    print(i)    #it is a second way in which first value is a starting second is a ending



for i in range(2,45,5):
    print(i)#3rd way in which 3rd number defines the difference of numbers from starting to ending
for i in range(2,101,1):
    print(i)

#matching numbers by any list to know at which idx the number is at is called linear search
#print numbers from 1 to 100 by using for loop and range functions
for i in range (0,101):
    print(i)

#again
for i in range(0,101):
    print(i)

#print numbers from 100 to 1
for j in range(100,0,-1):#-1 should be used at the third one
    print(j)

#print a multiplication table of number n
#n = int(input("enter number:"))

#for i in range(1,11):
 #   print(n*i)

#again 
#n = int(input("enter number:"))

#for i in range(1,11):
#    print(n*i)

#pass statement 
#pass statement is a null statement that does nothing.it is used aa a place holder in future code
#for i in range (5):
    #empty

#print("some useful work")
#so it will create an error 
for i in range(7):
    pass
print("some useful work")

#again
for i in range(9):
    pass #pass is a skip function in which loop does not execute
print("what's going on?")

#write a program to find the sum of first n numbers(using while)
n = 6 
sum = 0
for i in range(1,n+1):
    sum+=i
print("total_sum=",sum)

#again
n = 67
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum =",sum)

#again 
m = 69
sum = 0 
for i in range(1,1+m):
    sum+=i
print("total sum=",sum)

#again
j = 78987
sum = 0
for i in range(1,1+j):
    sum+=i
print("total sum=",sum)

#again
j = 7898
sum = 0
for i in range(1,1+j):
    sum+=i
print("total sum=",sum)

#by using while loop
n = 7
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("total sum:",sum)
    

#by using while loop 
n = 76
sum = 0 
i = 1
while i<=n:
    sum+=i
    i+=1
print("total sum is:",sum)


#again
n = 49
sum = 0
i = 1
while i <=n:
    sum+=i
    i+=1
print("total sum is=",sum)

#write a program to find the factorial of first numbers .(using for)
n= 6
fact = 1
i = 1
while i<=n:
    fact*=i
    i+=1
print("factorial is :",fact)

#again 
n = 5
fact = 1 
i = 1
while i <=n:
    fact*=i
    i+=1
print("your factoraial is:",fact)


#same this work by using a for loop 
n = 14
fact = 1
for i in range(1,1+n):
    fact*=i
    print("factorial is:",fact)