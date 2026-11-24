''' basic Operation on String'''
# concatenation and repetition
First_name = "Sankalp"
Last_name = "Dubey"

full_name = First_name + Last_name
print(full_name*3)

print("D" in "Dubey") # membership

print(len("full_name"))#length


text = "    sankalp dubey"

print(text.upper())
#SANKALP DUBEY

print(text.lower())
#sankalp dubey

print(text.replace("sankalp","Dwarika Dhish"))
# Dwarika Dhish Dubey

print(text.split())
#['Sankalp', 'Dubey']

print(text.title())
#Sankalp Dubey

print(text.find("d"))

print(text.count("sankalp"))

print(text.strip())