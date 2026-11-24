'''INTRODUCTION TO DICTIONORIES AND FUNCTION

Dictioniries-> it is a built in type function that stores data in the form of key-value pairs
-Store data in key value pairs
-Mutable
-keys must be unique
-value can be duplicated
-value can be of diffrent data type

created using curly brackets {}
'''

student ={
    "name":"Sankalp",
    "age": 22,
    "Course":"Mca",
    "Marks":85
}

print(student["name"]) #accesing dic value 
print(student)  #{'name': 'Sankalp', 'age': 22, 'Course': 'Mca', 'Marks': 85}
print(type(student)) # <class 'dict'>

#adding,updating and deleteing

student["city"] = "Delhi"
print(student)
#add {'name': 'Sankalp', 'age': 22, 'Course': 'Mca', 'Marks': 85, 'city': 'Delhi'}

#update
student["age"]  = 21
print(student) #{'name': 'Sankalp', 'age': 21, 'Course': 'Mca', 'Marks': 85, 'city': 'Delhi'}


#delete
student.pop("age")
print(student)#{'name': 'Sankalp', 'Course': 'Mca', 'Marks': 85, 'city': 'Delhi'}

print(student.keys()) #dict_keys(['name', 'Course', 'Marks', 'city'])
print(student.values()) #dict_values(['Sankalp', 'Mca', 85, 'Delhi'])
print(student.items())# dict_items([('name', 'Sankalp'), ('Course', 'Mca'), ('Marks', 85), ('city', 'Delhi')])
print(len(student))


#using loop
for key, value in student.items():
    print(key,":",value)
    '''name : Sankalp
Course : Mca
Marks : 85
city : Delhi '''


students ={
    "student1":{
    "name":"Sankalp",
    "age": 22,
    "Course":"Mca",
    "Marks":85
},

    "student2":{
    "name":"Dwarika",
    "age": 22,
    "Course":"Mca",
    "Marks":85
}
}
print(students)
print(students.items())
'''
{'student1': {'name': 'Sankalp', 'age': 22, 'Course': 'Mca', 'Marks': 85}, 'student2': {'name': 'Dwarika', 'age': 22, 'Course': 'Mca', 'Marks': 85}}
dict_items([('student1', {'name': 'Sankalp', 'age': 22, 'Course': 'Mca', 'Marks': 85}), ('student2', {'name': 'Dwarika', 'age': 22, 'Course': 'Mca', 'Marks': 85})])'''
