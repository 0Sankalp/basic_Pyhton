'''
int - 10 , float 10.5, complex(like algebra it contain both number and alpahabet)- 2+3j
,boolean- true or false,
List - it is an order and mutalble collection (mutable are changable after the creation ) ex- [1,2,3] ,

tuple - it is an order and imutable collection ex =  (1,2,3),
string - repsresented as str,
set = unorderd collection of unique values {1,2,3},
dict = {"name":"Ram"}
'''
a= 10
b = 10.5
c = "hello"
d  = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

type()function 
The type() function is used to identify the data type of an object or variable.

'''
x = 100
print(type(x))

t= [1,2,3]
print(type(t))

y = (1,2,3)
print(type(y))

#id()

D= 50
print(id(D))