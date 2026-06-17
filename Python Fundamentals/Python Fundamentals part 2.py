# CONDITIONAL STATEMENTS 
# LOOPS 
# FUNCTIONS



# CONDITIONAL STATEMENTS





username=input("enter the username")
passward=input("enter the passward")
if username=="sarthak":
    print( "user name is correct")
else:
    print("username is incorrect")
if passward=="sarthakbirari":
    print("passward is correcnt")
else:
    print("passward is incorrect")

#      or 

username = input("Enter the username:")
passward = input("Enter the passward:")

if (username == "sarthak" and passward == "pass"):
    print("login successful")

elif (passward == "sarthak"):
    print("wrong username")

else:
    print("wrong passward")



# number is odd or even


number=int(input("enter the number"))
if number%2==0:
    print("number is even")
else:
    print("number is odd")


# another  way nesting

username=input("enter the username")
passward=input("enter the passward")
if username == "sarthak" and passward=="birari":
    print("login successful")
else:
    if username != "sarthak":
        print("wrong username")
    else:
        print("wrong passward")


# age detecter:

age = int(input("enter teh age:"))

if age<13:
    print("child")
elif age>=13 and age<18:
    print("teenager")
else:
    print("adult") 




# ______________________________________________________________________________________________________________



# LOOPS: WHILE LOOP


# finite loop

count=1
while count<=5:
    print("hello world",count)
    count+=1



# example: print number 1 to 5


i=1
while (i<=5):
    print(i)
    i+=1


k=5
while (k>=1):
    print (k)
    k-=1


# PRINT MULTIPLICATION TABLE OF ANY NUMBER 'N'

i=1
while (i<=10):
    print (6*i)
    i+=1

n=int (input("enter the number:"))
i=1
while(i<=10):
    print(n*i)
    i+=1



# BREAK AND CONTINUE:

# PRINT ALL THE ODD NUMBERS FROM 1 TO 10:
# using continue 
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


# using break

# if we want to stop the loop then we use break 

i=1
while(i<=10):
    if(i==6):
        break
    print(i)
    i+=1



# FOR LOOP:

# PRINT VOWEL COUNT OF A GIVEN STRING:

word="artificial"
count=0
for ch in word:
    if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        count+=1
        print(count)

    


# USING RANGE FUNCTION

# print all odd number between 1 to 10:

for i in range(1,10,2):
    print(i)


# PRINT SUM OF FIRST 'N' NATURAL NUMBERS:


n=int(input("enter the number"))
sum=0
for i in range(1,n+1 ):
    sum+=i
print(sum)


# _________________________________________________________________________________________________________________________________________________


# FUNCTIONS:

def hello():
    print("hello world")
    print("how are you")

hello()
hello()


# ADDITION OF TWO NUMBERS:

# function defination
def sum(a,b):
    s=a+b
    return s


 # function call
ans=(1+2)
print(ans)


# PRINT THE AVERAGE OF THREE NUMBERS:

# function defination

def average(a,b,c):
    a=a+b+c/3
    return

# # function call 

answer=(2+2+2)
print(answer)

# THERE ARE TWO TYPES OF FUNCTIONS:
# 1. build in function
# 2. user defined functions




# LAMBDA FUNCTIONS:

average=lambda a,b,c: (a+b+c)/3
print(average(2,2,2))


# WAF TO PRINT FACTORIAL OF 'N


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i

        return fact
    
n=int(input("enter number")) 
print(factorial(n))














