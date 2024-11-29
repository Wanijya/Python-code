# 1) Accept two numbers and print the greater between them.
def greater_number():
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter a Number: "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are equal")
# greater_number()
        
# 2) Accept the gender from the user as char and print the respective greeting message
        #Ex- Good Morning Sir (on the basic of gender)
def Greeting_message():
    gender = input("Enter your gender: ")
    if (gender == "M" or gender == "m"):
        print("Good Morning Sir")
    elif(gender == "F" or gender == "f"):
        print("Good Morning Mam")
    else:
        print("Invalid gender")
Greeting_message()
