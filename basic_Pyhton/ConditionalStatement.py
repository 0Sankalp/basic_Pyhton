'''
1 if
2 if-else
3 elif
4 Nested if
'''
#if
age = 20
if age >=18:
    print("Eligble ")


# if else
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")    

if num <= 10:
    print("ok")
else:
    print("not ok")

#elif - use  to check multiple condition

marks = 70

if marks>=90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("grade C")
else:
    print("fail")            
     

# nested if 
value = 14
if num > 0:
    if num % 2 == 0:
        print("Even")
    else:
         print("odd")
else:
    print("zero")        