print("Hello", end=" ")
print("World")

print("python", "is", "fun", sep="-", end="!\n")
print("Python", "is", "fun")

if 5 > 2:
    print("No is greater")

    # 1. Integer
    a = 10
    print(a)

    # 2. Float
    b = 10.5
    print(b)

    # 3. String
    c = "Python"
    print(c)

    # 4. Boolean
    d = True
    print(d)

    # 5. List
    e = [10, 20, 30]
    print(e)

    # 6. Tuple
    f = (10, 20, 30)
    print(f)

    # 7. Set
    g = {10, 20, 30}
    print(g)

    # 8. Dictionary
    h = {"name": "Sarthak", "age": 21}
    print(h)

age = 21
print(age)


name = "Sarthak"
age = 21

print(name)
print(age)

a,b,c=1,2,3
print(a,b,c)

a,b=b,a
print(a,b)



name = "Sarthak"
age = 21


print(name, type(name))
print(age, type(age))



text = "Python"

print(text.find("o"))





text = "Python Is Fun"

print(text.upper())
print(text.lower())


print(text*2)
print(text+"AI")



a = 25

print(a)
print(type(a))

b = float(a)
c = str(a)

print(b, type(b))
print(c, type(c))




a = "25"

print(int(a) + 25)



username = input("Enter username: ")
print("Hello", username)




age = int(input("Enter age: "))
print("Next year:", age + 1)




age = int(input("Enter age: "))

print(f"Next year: {age + 1}")






name="Sarthak"
marks=87.5
print(f"{name} scored {marks}")
print(f"Double: {marks*2}")
print(f"Rounded:{marks:.0f}")




a = 17
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)




a = 10

a += 5
print(a)   # 15

a -= 3
print(a)   # 12

a *= 2
print(a)   # 24

a /= 4
print(a)   # 6.0

a //= 2
print(a)   # 3.0

a %= 2
print(a)   # 1.0

a **= 3
print(a)   # 1.0





age =20

has_id= True
print(age>18 and has_id)    #True
print(age<18 or has_id)     #True
print(not has_id)           #False






print(2+3*4) #14
print((2+3)*4)   #20


print("Sarthak")
print("CSMSS Chhatrapati Shahu College of Engineering")
print("Chhatrapati Sambhajinagar")

name = "Sarthak"
age = 21
city = "Chhatrapati Sambhajinagar"

print(f"My name is {name}")
print(f"My age is {age}")
print(f"My city is {city}")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")



#cube
num = int(input("Enter a number: "))

print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}")







#convert  150minutes into hours  and minutes using \\  and %
minutes = 150

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Hours: {hours}")
print(f"Minutes: {remaining_minutes}")




celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"Temperature in Fahrenheit: {fahrenheit}°F")








#check  if a number enntered by the user is greater than 50 and print true or false
num = int(input("Enter a number: "))

print(num > 50)






# Student Profile Card

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nEnter marks of 3 subjects:")
subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))

total = subject1 + subject2 + subject3
percentage = total / 3

print("\n========== STUDENT PROFILE CARD ==========")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"City       : {city}")
print(f"Subject 1  : {subject1}")
print(f"Subject 2  : {subject2}")
print(f"Subject 3  : {subject3}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print("==========================================")




