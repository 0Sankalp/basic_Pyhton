'''List
It is an ordered and  mutable  collection of elements, it can store elment of diffrent data types
list are created using square bracket [ ]
'''

numbers = [10,20,30,40,50]
mixed = [10, "python", 5.5,True]

print(type(numbers))
print(type(mixed))

#<class 'list'>
#<class 'list'>

#Accessing list 

number = [80,20,10,40]

print(number[0])
print(number[3])

number[3] = 50#updation

print(number)

#list slicing
print(number[1:3])
#[20, 30]

number.sort()#Sorting

print(number)

#Traversing a list  - accessing each element of list one by one

for num in number:
    print(num)


#nested list

matrix = [
    [1,2],[3,4]
]

print(matrix)