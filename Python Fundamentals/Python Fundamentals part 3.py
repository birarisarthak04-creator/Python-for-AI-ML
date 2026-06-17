# STRING: strings are immutable
word="python"
print(len(word))

word1 = "i love"
word2 ="cars"
concatenate= (word1 + " " + word2)
print(concatenate)

# indexing:
sen="artificial"
print(len(sen))
print(sen[2])
print(sen[9])

# using a for loop:
for ch in sen:
    print(ch)



# SLICING IN STRING:

name= "sarthak birari"
print(len(name))
print(name[8:14])
print(name[0:7])
print(name[3:11])

# NEGATIVE SLICING:

print(name[-11:-4])

print(name[-6::2])


# ______________________________________________________________________________________________________


# STRING FORMATING:

# 1. FORMAT()
# 2. F-STRING 
 
# 1. format()
# normal formating
a = 20
b = 10
sum = a+b 
print("the sum of a and b is {}".format(sum))
print("the sum of {} & {} is {}".format(a,b,sum))

# index based formating:
print("the sum of {1} & {0} is {2}".format(a,b,sum))
# value based formating:
print("the value of a={a} and b={b}".format(a=11, b=15))



# 2. f-string:

num1=50
num2=30 
print(f"the sum of {num1} & {num2} is {num1+num2}")
print("The sum of", num1, "and", num2, "is", num1+num2)

# ___________________________________________________________________________________________________________________________

# LISTS: lists are mutable 
# we can save multiple type of data in lists 

marks=[50, 75, 85, 90, 77, 95]
print(marks)

# mutable:
marks[0]=65
print(marks)

# list slicing:
print(len(marks))
print(marks[1:6])
print(marks[-4:-1])

# list methods:

# list5=[2,5,7,1,4]
# list5.append(10) #adds one element at the end 
# print(list5)

# list5.sort() #sorts in ascending order  
# print(list5)

# list5.sort(reverse=True) #sorts in descending order 
# print(list5)

# list5.reverse() #reverses list  
# print(list5)

# list5.insert(1,3) #insert element at index
# print(list5)

# list6=[2,4,7,2,5]
# list6.remove(2) #removes first occurrence of element 
# print(list6)

# list7=[1,3,1,4,8,10]
# list7.pop(0) #removes element at index 
# print(list7)







# LOOPS USING LISTS

numbers = [10, 29, 28, 92, 77]
for val in numbers:
    print(val)

# linear search: we will a val at every index 
x=28 
i=0
for val in numbers:
    if (val==x):
        print(f"x found at index {i}")
        break 
    i+=1

# _____________________________________________________________________________________________________________________________________________________________________________________________

# TUPLES: tuples are immutable 
# we can save multaple type of data in tuple


# tuple1=(1,3,7,9,10)
# print(tuple1)
# print(type(tuple1))
# print(len(tuple1))
# # indexing
# print(tuple1[1])

# if we have to to print a single element in tuple so give coma ( , ) in last for e.g.,
# tuple1=(1,) 

# TUPLE SLICING:

# tuple2=(1,5,7,10,11,15)
# print(tuple2[0:4])
# print(tuple2[0:6:2])

# # negative slicing

# tuple3=("a","b","r","v","t","e")
# print(tuple3[-6:-4])
# print(tuple3[-4:-1])

# # TUPLE METHODS:

# tuple4=(1,3,6,2,6,3)
# print(tuple4.index(6)) #returns index of first occurence
# print(tuple4.index(2))

# tuple5=(2,5,2,6,7,6,8,6)
# print(tuple5.count(6)) #counts total occurance



# loops using tuple:
tup=(1,5,3,76,4)
for val in tup:
    print(val)

# adding the values using loops:
sum = 0
for i in tup:
    sum+=i
print(f"the sum of all the values is {sum} ")


# ________________________________________________________________________________________________________________________________________


# DICTIONARY:
# dictonaries are used to store data values in key:value pairs
# they are unordered, mutable(changeable) and dont allow duplicate keys 

# dict={"key" : "value",
#       "name" : "sarthak",
#       "subjects" : ["python","java","cpp"],
#       "age" : 18,
#       }
# print(dict["key"])
# print(dict["age"])
# print(dict["name"])

# dict["age"]=19
# dict["address"]="barwani"
# print(dict)

# NESTED DICTONARY

# dict1={"players" : ["virat kohli","rohit sharma","hardik pandya"],
#       "runs" : {
#           "virat kohli" : 100,
#            "rohit sharma" : 101,
#             "hardik pandya" : 51,
#             }
#  }
# print(dict1)
# print(dict1["runs"]["virat kohli"])
# print(len(dict1))
# print(list(dict1))



# # DICTONARY METHODS:

# dict2={"family_members" : ["sarthak","ritika","poonam","ganesh"],
#       "sarthak" : "student",
#       "ritika" : "student",
#       "poonam" : "nurse",
#       "ganesh" : "barber",
#       }

# print(dict2.keys()) #returns all keys
# print(list(dict2.keys()))


# print(dict2.values()) #returns all values 
# print(list(dict2.values()))


# print(dict1.items()) #returns all key value pairs as tuple
# pairs=list(dict1.items())
# print(pairs[0])


# print(dict1.get("players")) #returns the key according to value


# dict3={"city" : "niwali"}
# dict1.update(dict3) #insert the specified items to the dictionaries 
# print(dict3) 


# ____________________________________________________________________________________________________________________________________________________


# SETS:
# set is the collection of the unordered items 
# each element in the set must be unique and immutable
#repeated elements stored only once, so it resolved to {1,2}


# collection={1,2,3,10,1,10,"hello","hi"}
# print(collection)
# print(len(collection)) 
# print(8type(collection))

# for empty set: collection = set() 


# SET METHODS:

# set1={1,2,"indore",10,"indore",12}
# set1.add(5) #adds an element
# print(set1)


# set1.remove(1) #removes an element
# print(set1)

# set1.clear() #empities the set
# print(set1)
# print(len(set1))

# set2={1, 3, 4, 5, 3}
# set2.pop() # removes a random values 
# print(set2)

# set3={1,2,3}
# set4={3,4,5}
# print(set3.union(set4)) #combines both set values and returns new 

# print(set3.intersection(set4)) #combines common values and returns new 

# __________________________________________________________________________________________________________________________________________________________________________

# QUESTION PRACTICE:

# Q1. Given a list of tuples with info(name, subject):

# list all unique course 
# list students enrolled in english 
# create dictionary (student, set of courses)
 
info= [ 
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "math"),
    ("bob", "math"),
    ("alice", "english"),
    ("charlie", "english")
]
# list all unique course 
unique_set= set()

for tup in info:
    unique_set.add(tup[1])
print(unique_set)


# list students enrolled in english 
for name,course in info:
    if (course=="english"):
        print(name)


# create dictionary (student, set of courses)

dict = {}

for name,course in info:
    if (dict.get(name)==None):
        dict.update({name: set()})
        dict(name).add(course)
    else:
        dict(name).add(course)

print(dict)







































