# Additional concepts of python:




# File I/O: file  input and output

# In python, we have different different file formats like .txt files, .csv files etc.
# Whenever we want to read or write the data so we use file I/O concepts.

# Use of file I/O:  It is used in training the machine learning and deep learning models.

 

# Operations on files: Open, read and close

# example: we are opeaning a book and reading the content and then we will close it after reading.


# To open a file: f = open("data.txt", "r")
# here data.txt is file name or path and r is the mode. (r = read mode)    

# Example: Suppose here we have the sample.txt file in the same folder and now we want to read that txt file.

f = open("sample.txt", "r")  # file object
data = f.read()

print(data)
print(type(data))

f.close()

# another function to read line by line

f = open("sample.txt", "r")  # file object 

data = f.readline()  # Here it will print one line. To print next line we need to use this line again.
print(data)
print(type(data))      

data = f.readline() 
print(data)

f.close()


# We can write also in our txt file by using the write()

f1 = open("sample.txt", "w")

# Here we have to make sure that when we use this write() then our previous written data will be cleared and we can add new data from scratch.
data_txt = f1.write("Hey \nmy self sarthak ")
print(data_txt)

f1.close()


# ____________________________________________________________________________________________________________________________________

# Modes in file operation: we use modes to open the different different type of files.



# 1. [ r ]: reading (default)

#    In the read mode we can read the data of the file and the pointer moves from left to right just like we read normally.

# 2. [ w ]: writing, truncates file first

#   In the write mode we can write in the file but the file will get empty first.

# 3. [ a ]: writing, appends at end

#   In the append mode we can write the new things which we wants to append in the file, the pointer starts at last.

# 4. [ x ]: creates new & open for writing 

#   In the x mode it creates the new file and open for writing.




# WE HAVE THE MODES FOR THE DATA FORAMT ALSO: like binary and text 


# 5. [ b ]: binary mode 

#   In the binary mode we can access the data stored in the file in the video or audio so we can access by binary mode.

# 6. [ t ]: text mode (default)

# NOTE: We can also comebine the modes like ( rt, wt, rb , wb ). 

# exapmle:
 
f2  = open("sample.txt", "wb")
data = f2.write("whatever we want to overwrite")

print(data)

f2.close()

# 7. [ + ]: opens disk file for update(r & w).

#   In [ + ] we can update disk file. 
# for r+: here we can read and as well as write also we have to make sure of the pointer here the pointer is on stating.
# for w+: here we can write and read also and the the pointer stats from the begining because we are overwriting.
# for a+: here we can add content in the file and read also, the pointer starts from the end where we ended last
 
#  example 1: 

f3 = open("sample file", "r+")
data = f3.write("Whatever we want to write")
# Here the data will update from the begining because of the pointer
print(f3.read())

f3.close


# example 2: 

f3 = open("sample file", "a+")
data = f3.write("Whatever we want to write")
# Here the data will update from the last because of the pointer
print(f3.read())

f3.close

# NOTE: we have to understand the pointer to do the operation at any file.



# ______________________________________________________________________________________________________________________



# with keyword: we use with keyword because if we use with so we do not need to close() our file, we use this because we do not want any errors.

# The syntax to open and close the file is:

with open("sample.txt", "r") as f4:
    data = f4.read()
    print(data)
    print(len(data))



# ________________________________________________________________________________________________________________



# Delete files: We can delete the files by os. os is the build in module where os stands for operating system 
#  syntax to delete file:

import os

os.remove("sample.txt")



# __________________________________________________________________________________________________________________________


# Practice problem: Word search in a text file


data = True
word = "python"
line = 1

with open("sample.txt", "r") as f:

    while data:
        data = f.readline()
        if (word in data):
            print(f"{word} found at line {line}")
            break


        line+=1


# _____________________________________________________________________________________________________________________






# Exception handling: In exception handling we try to predict the error in the code and try to manage or handle them.

# There are 4 keywords we use in exception handling;


# "try", "except", "else", finally:

# we use this keywords when we know that the code can throw errors that's why we use exception handling
 
# Example:

# In try we write the code that we know that it can give the errors

try:
    x = int(input("enter x:"))
    ans = 10/x

# In except, when we want to perform a particular task when a type of error occur. Here we know that we cannot divide 0 by 10 so here is ZeroDivisionError
# We can use multiple except
# These are build in exception like ZeroDivisionError, IndentationError, ValueError etc. We can made our user defined exception also.

except ZeroDivisionError:
    print("zero cannot allow")

# Here it will print this invalid input when we write a different datatypes except integer

except ValueError:
    print("Invalid input")

# In else we write the final thing which we want to perform like here we want to print the final answer

else:
    print(f"The answer is {ans}")

# if we want to explore the other build in exceptions so we can explore on the link ( w3schools.com).


# we use finally keyword when we want to perform a task, suppose if our code give the exception or not the code will always run which is written in the finally keyword.

finally:
    print("End of the program") # here the "End of the program" will always print, if the exception will come still the program will work.




# _________________________________________________________________________________________________________________________________________________________________________



# List Comprehensions: List Comprehensions are the way to write a code in a simple way for list.

# exapmle:  Normal code to print the square roots of the numbers from 0 to 5


squares = []

for i in range(6):
    print(squares.append(i*i))


# Here is a better and short way:


sq = [i*i for i in range(6)]
print(sq)  

# now the code for only squares of odd number by using conditions

sq = [i*i for i in range(6) if i%2 !=0]
print(sq)


# another example:

nums = [-2, -3, 3, 4, -1, 7]

nums = [0 if val < 0 else val for val in nums]
print(nums)

# another example: here we need to uppercase all the words

words = ["hello", "python", "interpreter"]
words = [val.upper() for val in words]
print(words)


# __________________________________________________________________________________________________________________


# JSON Module: JavaScript Object Notation

# JSON is a build in module, it is a format used to store or exchange the data between programers.
# It is used in web development like for exchanging the data of a website or app.
# It is written like dictionary.


import json

# we have to build a file ( .json )

# we have two important functions of json:

# 1. json.loads(): used for json string and dictionary data to convert into the python object
# 2. json.dumps(): used for python object string and dictionary data to convert into json format

# Example: using json.loads

json_str = '{"name": "Krishna", "isStudent": true}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)

# now using json.dumps()

import json

py_obj = {
    "name": "Ram",
    "isStudent": "True"
}

json_str = json.dumps(py_obj)

print(type(json_str), json_str)



# Again here we have:

# 1. json.load(): json.load() used to read the data of the json file.
# 2. json.dump(): json.dump() used to write the data in the json file.
# ( We can combine the concepts of file I/O and json module )

# Example:

import json

# here make sure that the file is in the same folder if it is in another folder so we have to give the absolute address of the file
with open("data.json", "r") as f:
    py_obj = json.load(f)  
    print(py_obj)


# overrighting the data in the json file

import json

data = {
    "name": "Sarthak",
    "age": 19,
    "College": "VIT Bhopal",
    "isStudent": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent = 4, sort_keys = True)

   




