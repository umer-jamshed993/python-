#functions in python
#functions is a block of statements that perform  a specific task.
#a = 5
#b = 10
#sum = a+b
#print(sum)
#if there are many lines of code
#a = 12 
#b = 15
#sum = a+b
#print(sum)
#more lines of code
#a = 4
#b = 15
#sum = a+b
#print(sum)

#if we perform all these tasks by usng of functions then:

#function
#def calc_sum(a,b):
#    sum = a+b
#    print(sum)
#    return sum
#calc_sum(1,2)#the numbers 1 and 2 are the arguments that value stores in a function original
#calc_sum(23,56)
#calc_sum(45,98)


#again 
#def calc_sum(a,b):
#    return a +b
#sum = calc_sum(23,56)
#print(sum)

#again 
#def calc_sum(a,b):
#    return a +b 
#sum = calc_sum(12,56)
#print(sum)

##again
#def calc_difference(a,b):
#    return a -b
#difference = calc_difference(67,65)
#print(difference)

#again
#def calc_difference(a,b):
#    difference = a-b
#    print(difference)
#calc_difference(23,10)
#calc_difference(34,15)

#again
#def calc_sum(a,b,c):
#    return a+b+c
#sum = calc_sum(14,45,34)
#print(sum)


#preferable
#def calc_sum(a,b,c):           the word def is called function defination and the a,b in brackets are called parameters
#    sum = a+b+c
#    print(sum)
#    return sum
#calc_sum(34,56,67)  #it is called funtion call and the values 34,56,67 are called arguments
#calc_sum(90,98,65)
#calc_sum(34,56,65)

#def print_hello():
#    print("hello")

#print_hello()
#print_hello()




#def print_hello():
#    print("hello")

#n = 8
#i = 1
#while i <=8:
#    print_hello()
#    i+=1

#def print_hello():#tis is a function having no parameters and not returning a value is completely possible in python
#    print("hello")

#print_hello()
#print_hello()
#print_hello()



#now we are making functions that return no value
#def print_hello():
#    print("hello")

#output= print_hello()
#print(output)
#this function return no value because there are no parameters and arguments passed in a function
#so it is an empty function


#now we are going to calculate avg of three numbers by using this function
#def calc_avg(a,b,c):
#    sum = a+b+c
#    avg = sum/3
#    print(avg)
#    return avg
#calc_avg(2,5,7)


#again
#def calc_avg(a,b,c,d):
 #   sum = a+b+c+d
 #   avg = sum/4
 #print(avg)
  #  return avg
#calc_avg(1,2,67,87)

#it was a method to print an average

#now we are going to discuss types of functions
# there are two main types of functions
# these are user defined 
# and built in functions.
#  print(),len(),type(),range() are the examples of built in functions
#print("punjab college","ahmed pur east")
#print("punjab college",end = "")
#print("ahmed pur east")

#second type is called user defined functions that are used 

###########################
#default parameters 
#it is a process of assigning a value to a parameter ,which is used when no argument is passed
#def calc_prod(a,b):
#    print(a*b)
#    return a*b
#calc_prod()
#in up we face an error beacause arguments have no value in function call
#so we write
#def calc_prod(a=2,b=5):
#    print(a*b)
#    return a*b
#calc_prod()#in first we initialize the variables and did not give a value in function in function call

#so it is called default value initialization
#def calc_prod(a,b=5):#if we not assign a value in function and assign it in a function call then this logic is completely valid
#    print(a*b)
#    return a*b
#calc_prod(10)
#but this work when we give value after a ,
#def calc_prod(a=2,b):
#    print(a*b)
#    return a*b
#calc_prod(,10)so it does not work because we have to give a default value after a ,


#lets practice
#write a function to print a length of a list
#cities = ["karachi","lahore","islamabad","peshawar"]
#heroes = ["umer","shakeel","usman","maaz","yameen"]
#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(heroes)


#cities = ["lahore" ,"karachi","islamabad","bahawalpur","gujranwala","sialkot"]
#heroes = ["quaid e azam ","allama iqbal","liaqat ali khan","sir syed ahmed khan"]
#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(heroes)

#write a function to print the elements of a list in a single line(line is the parameter)
#cities = ["dehli", "peshawar", "islamabad", "karachi", "lahore"]
#heroes = ["thor","ironman","superman","shaktiman"]


#def print_list(list):
#    for item in list:
#        print(item,end = "")

#print_list(heroes)
#print_list(cities)


#write a function to find a factorial of n(n is the parameter)
#def calc_fact(n):
#    fact = 1
#    for i in range(1,n+1):
#        fact*=i
#    print(fact)

#calc_fact(6)


#again practice
#def calc_fact(n):
#    fact = 1
#    for i in range (1,1+n):
#        fact*=i
#        print(fact)
#calc_fact(16)

#convert i dollar into pkr
#def converter(usd_val):
#    pkr_val= usd_val*283
#    print(usd_val,"usd=",pkr_val,"pkr")
#converter(12)



#def converter(usd_value):
#    pkr_value = usd_value*285
#    print(usd_value,"usd=",pkr_value,"pkr")
#converter(34)


#def converter(pound_val):
#    pkr_val = pound_val*385
#    print(pound_val,"pound=",pkr_val,"pkr")
#converter(34)


#convert saudi riyal into pkr
#def converter(riyal_val):
#    pkr_val = riyal_val*85
#    print(riyal_val,"riyal=",pkr_val,"pkr")

#converter(10)


#convert kuwati dinar into pkr
#def converter(dinar_val):
#    pkr_val = dinar_val*900
#    print(dinar_val,"dinar=",pkr_val,"pkr")

#converter(14)

#another concept is called recursion
#when a function calls it self repeatedly is called recursion
 #recursion and loops are inter related with each other
#def show(n):
#    if(n==0):
#        return
#    print(n)
#    show(n-1)

#show(5)


#def show(n):
#    if n ==0:
#        return
#    print(n)
#    show(n-1)

#show(67)





#def show(n):
#    if (n==0):
#        return
#    print(n)
#    show(n-1)

#show(78)


#def show(n):
#    if (n==78):
#        return
#    print(n)
#    show(n+1)

#show(34)


#def show(n):
#    if (n==45):#this statement is called a base case
#        return
#    print(n)
 #   show(n+4)

#show(1)

#this is called recursion


#def show(n):
#    if (n ==0):
#        return
#    print(n)
#    show(n-1)
#    print("end")
#show(10)

#recursive relations 
#for example 5! = 4!*5 so it is called recursive relations
#def fact(n):
#    if(n==1 or n==0):  
#        return 1
#    return fact(n-1)*n
#print(fact(2))


#def fact(n):
#    if(n==1 or n==0):
#        return 1
#    return fact(n-1)*n
#print(fact(10))

#write a recursive function to calculate the sumof first n  numbers
#def calc_sum(n):
#    if (n==0):
#        return
#    return calc_sum(n-1)+n
#sum = calc_sum(10)
#print(sum)

#write a recursive function to print all elements in a list
#use list and index as parameters 
#def print_list(list,idx=0):
#    if(idx ==len(list)):
#        return
#        print(list[idx])
#    print_list(list,idx+1)

#fruits = ["mango","litchi","apple","banana"]
#print_list(fruits)

#this program will print all elements of numbers 

#print("hello world")
#print("hello wold i am python developer")
#print("my name is umar jamshaid")
#print