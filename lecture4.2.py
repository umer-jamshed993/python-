file= {
    "name":"umer",
    "class" : 12,
    "roll no":134,
    "city":"ape",   
    }
print(file)


newdict = {
    "name":"umer",
    "class":13,
    "subjects":{
        "maths":68,
        "phy":90,
        "bio":98,
    }
}
print(newdict)
newdict["city"]= "ape",
print(newdict)
print(newdict["subjects"]["maths"])
#dictionary methods #dictionary keys can print all the keys
#return all keys function
print(newdict.keys())
print(file.keys())
#we can get all the keys by using this
student = {
    "name": "umer",
    "subjects":{
        "phy":78,
        "chemistry":78,
        "biology":79,
    }
}
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(student.keys()))#both upper and lower results are same 
print(len(list(student.keys())))
#all results will be same 


#return all values function
print(student.values())
print(list(student.values()))

#next method is called .items method that return all key values pairs as tuples 
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
print(pairs[1])
#now we are studying another key is called get that returns function according to value
print(student["name"])
print(student.get("name"))


print(student["name"])
print(student.get("name"))#if we write name 2 that does not exist then error will we get

#write many print statements if there is an error in mid of the statements and there are many lines below the code that are tru will not execute 
#print("BEFORE")
#print("AFTER")
#THESE ARE THE TWO STATEMENTS THAT ARE USED UP AND LOW ANY CODE ONLY TO RUN IT LIKE TO RUN ONLY A MID OF A PROGRAM TO EXECUTE ONLY THAT CODE WE CHOOSE



#next method is called an update method that insert an specified items in the dictionary
student.update({"city":"dehli"})
print(student)
#or
student = {"city":"dehli"}#both are same 
#we can store multiple values in a dictionary like
student = {"city":"dehli","country":"india"}
student.update({"city":"dehli","country":"india"})
print(student)
#both are same statements means their work is same

#the values in a dictionary can change and update 


#now we are discussing another topic in python which is called set in python
#set is a collection of the unordered items
#each element in a set must be unique and immutable
nums = {1,2,3,4}
set2 = {1,2,2,2}
#we cant store list and dictionary in the sets because they are mutable and it is immutable 
#we can only store int float string and tuple and any other thing but not list and dictionary.
collection = {1,2,3,4,"umer","jamshed"}
print(collection)
print(type(collection))

collection = {1,2,3,4,"umer","umer","jamshed","jamshed"}
print(collection)#if we write multiple things in a set then multiple items are ignored by python and only the single values are printed
#the order of printed values is different
print(len(collection))#the length of a collection is 6 because duplicate length in an items is not allowed 
#if we wanna write empty set then we will write 
collection2 = set()#empty set ;syntax
print(collection2)
print(type(collection2))

#now we are disscussing about methods of sets 
#new elements can be added in a set but the elements that are automatically is in a set can not be changed
#so we can pass only tuple after .add not list and dictionary
collection3 = set()
collection3.add(1)
collection3.add(2)
collection3.add(2)
print(collection3)
collection3.remove(1)
print(collection3)
collection3.add("umer jamshed")
collection3.add("13th class")
print(collection3)
#but we cannot add any list and dictionary in it
collection3.add(4)
print(collection3)
#because list is an un hashable type because they are mutable
#the next method is called clear method used to empty the set (set.clear)
print(len(collection3))
collection3.clear()
print(collection3)
print(len(collection3))
#another method is called pop method which is used to remove any random values 
collection4 = {"coding","apna college","iub","bahawalpur"}
collection4.pop()
print(collection4)
collection.pop()
print(collection4)
print(collection4.pop())


#next two another important methods are union and intersection methods 
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1)
print(set2)#they will both same as before

#next is intersection method 
print(set1.intersection(set2))#answer is 2 ,3 

#now we are going to solve our some practice questions 
#store folowing words meanings in a python dictionary
#table:a piece of furniture,list of facts and figures 
#cat:a small animal 
dictionary10 = {
    "cat": "a small animal",
    "table":["a piece of furniture","lists of facts and figures"]
}
print(dictionary10)


#2nd program is you are given a list of number of students .assume one classroom is required for 1 subject.how many classrooms are needed by all students 
subjects = { "python","java","c++","python","javascript","java","python","java","c"}
print(len(subjects))


subjects2 = {"python","java","c++","java","python","java","c","python","java"}
print(len(subjects2))
print(subjects)
print(len(subjects))
print(subjects2)
print(len(subjects2))

marks = {}
x = int(input("enter phy:"))
marks.update({"phy":x})
x = int(input("enter math:"))
marks.update({"math":x})
x = int(input("enter chem:"))
marks.update({"chem":x})
print(marks)


marks2= {}
x = int(input("enter eng:"))
marks.update({"eng":x})
x = int(input("enter maths:"))
marks.update({"maths":x})
x = int(input("enter pak study:"))
marks.update({"pak study":x})

print(marks2)
#find out a way to store 9 and 9.0as seperate values in a set 
values = {9,"9.0"}
print(values)#THE OUT PUT WILL BE 9 and 9.0


#2nd possible way
values= {
    ("float",9.0),
    ("int",9)
}
print(values)#the output will be printed on screen same in both ways