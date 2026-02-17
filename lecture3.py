#lists in python 
#a list is A built in data type that stores a set of values 
#it can store elements of different types(integer ,float and string)
marks1 = 94.4
mark2 = 56 
marks3 = 90
marks4 = 78
marks5 = 76

#but in lists we simply write our students marks as 
marks = [94.4,56,90,78,76] 
#it is called a list in python 
#so we are printing this list 
print(marks)
#we are printing the type of data that is printed is 
print(type(marks))
#we are printing marks at index 0 
print(marks[0])
#and we can print any other marks by giving index
print(marks[1])
#we are printing length of a string now
print(len(marks))
#we can store ,multiple type of data in a single list 
#like int float char and string in a singlr list 
list = ["umer" ,45,45.78,'a']
print(len(list))
print(list[0])
print(list[1])
# we can store multiple type of data in a lists and can get access of list values and length of values
#difference between lists and a string 
#string is immutable because in string value access was alowed but changing of value was difficult
#but in list both tasks are possible whether these are accessing and changing 
#str = "hello"
#str[0] = "y"
#print(str(0))


# so the upper program is not supported because chANging of value is noy allowed
#but this thing both are possible in lists 
student = ["umer",78,89,"maaz"]
print(student[0])
student[0]= "kaleem"
print(student[0])
print(student)
#if lists have 4 values then we can not get access of 5th values 
#we studies slicing concept in string and the concept we are studying same concept in list which is called list slicing the part is the subset of a list 
#slicing is lists :
#list_name[starting_idx:ending_idx]#ending index is not included 
marks = [45,67,76,78]
print(marks[0:5])
print(marks[:4])
print(marks[0:])
print(marks[0:3])
#the negative indexig is from right to left
#-5,-4,-3,-2,-1
print(marks[-3:-1])
#now we are discussing list methods that are functions
list = [1,2,3]
#FIRST is list method
list = [1,2 ,3]
list.append(4)
print(list)
list.append(5)
print(list)
list.append(6)
list.append("umer")
print(list)
#element adding is also called mutating the list or adding element in a list
list = [2,4,3]
(list.append(6))
print(list)
list.sort()
print(list)
#we can sort our perevious list from high to low values by :
list.sort(reverse= True)
print(list)
list = [1,2,3,4,5,6,7,8,9,0]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
#sorting in  string is done by characters a,b,c which one is first or second and according to this sorting does in strings
list = ["bananas" ,"litchi" ,"apple"]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list = ['a','b','t','y','u','i','o']
list.sort()
print(list)
#reverse method we using 
list = ['a','e','r','y','i','o','l']
list.reverse()
print(list)
#now we are discussing list inserting concept
list = [1,2,3,4,5]
list.insert(1,6)
print(list)
#list insert(idx.el)#formula 
#we are discussing remove method
list = [1,2,3,4]
list.remove(2)#it will remove first 2 in the list
print(list)
list = [1,2,2,3,4]
list.remove(2)
print(list)
#in up the remove method remove only first 2 not second 2 
list = [1,2,3,4]
list.remove(1)
print(list)

#anothe rmethod is called a pop method
list = [1,2,3,4,5,6,7,8]
list.pop(2)
print(list) #it removes number according to index
#research of list objects ?
#i have to search ABOUT python documentation 


#now we are discussing tuples 
#A built in data type that let us create immutable sequence of values 
#a tuple working is same as a lists
#it is immutable just like strings and we can not change values in tuples and  we use parenthesis in tuples ()
tuple = (1,2,3,4)
print(type(tuple))
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
#empty tuple



tup = ()
print(tuple)
print(type(tuple))#out put is tuple and class is tuple

tup = (1,)#if comma doesnot with tuple value then python take it as a integer or float so comma is necessary .
print(tuple)
print(type(tuple))#output is 1 and class is tuple
# if thereare many values the last comma will be optional the python take it as a tuple.

#slicing in touple 
tup = (1,2,3,4)
print(tup[1:3])#the negative slicing will also be a same as in previous lists and strings options for touples were available 
#tuple methods 



tuple = (2,1,6,1)
#index of touple 
print(tup.index(2))#0 is index of 2 ,1 is index of 1,2 is index of 6 ,3 is index of 1


t = (1,1,1,1)
print(tup.count(1))#1 is 4 times 

#practice questions write a program to ask the user to enter names of their 3 favourite movies and store them in a list 
movies = []
mov1 = input("enter 1 st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3 rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)



movies = []
mov1 = input("enter 1st movie:")
movies.append(mov1)
mov2 = input("enter 2 nd movie" )
movies.append(mov2)
mov3 = input("enter 3rd movie")
movies.append(mov3)
print(movies)



#another method 
movies = []
movies.append(input("enter 1st movie"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3 rd movie:"))
print(movies)



list = (1,2,1)
copy_list = list.copy()
copy_list.reverse()
if(copy_list==list):
    print("palindrone")
else:
    print("not a palindrome")


list = [1,2,1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list==list):
    print("palindrome")
else:
    print("not a palindrome")


    #the output will be palindrome
#another list for practice 
#list = ["m","a","a","m"]
#write A program to count the number of students with the "A"grade in the following tuple
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


#store the above values in the list and sort them from "A "to "D".
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

