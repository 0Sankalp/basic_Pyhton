'''Introduction to Function
 a fucntion is a block of code that perform resuable task . it execute when it is called

 '''
def greet():
    print("welcome to Python")

greet()     

#function with parameter
def add(a,b):
    print("Sum:",a+b)

add(10,20)    


#Function with return statement 
def add(a,b):
    return a+b 

result = add(10,20)

print(result)

#Arguments 

def stud(name,age):
    print(name,age)

stud(name = "Dwarika",age = 23)    

def greet(name="student"):
    print("hello",name)

greet("Sankalp")    