'''Recusrion
it is programing technique where function call itself

it contain two imp parts
1 Base condition - stop the recursion
2 Recusrsive call - call the function again
'''

#factorial
def factorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n*factorial(n-1)

num = 5
print(factorial(num))       



'''Scope of vcariable
scope refers to the area of a program where a variable can vbe asccessed
'''

#local variable - variable decalred inside a function

def show():
    x=10
    print(x)

show()    #10


#global variable - variable decalred outside the function

x =100

def row():
    print(x)

row()
print(x)    


#global keyword - it allow a function to reassing a global variable 

x = 100

def change():
    global x
    x = 50

change()
print(x)

