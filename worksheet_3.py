# WORKSHEET 3


# What is missing from this code? (1 pt)
# temperature = float(input("Temperature: ")
# if temperature > 90:
#     print("It is hot outside.")
# else:
#     print("It is not hot out.")
#
# It is missing a parenthesis in the first line. Correct code:
temperature = float(input("Temperature: "))
if temperature > 90:
    print("It is hot outside.")
else:
    print("It is not hot out.")


# Write a Python program that will take in a number from the user and print if it is positive, negative, or zero. Use a proper if/elif/else chain, don't just use three if statements.
userinput = float(input("Please enter a number:"))
if userinput > 0:
    print("That number is positive.")
elif userinput < 0:
    print("That number is negative.")
else:
    print("The number entered is zero.")


# Write a Python program that will take in a number from a user and print out ``Success'' if it is greater than -10 and less than 10, inclusive. (1 pt)
#
number = float(input("Please enter a number betwen -10 and 10."))
if number >= -10 and number <= 10:
    print("SUCCESS")
else:
    print("Autch... no, try again.")


# This runs, but there is something wrong. What is it? (1 pt)
# user_input = input("A cherry is a: ")
# print("A. Dessert topping")
# print("B. Desert topping")
# if user_input.upper() == "A":
#     print("Correct!")
# else:
#     print("Incorrect.")
#
# The program is asking for an input before the alternatives are layed out. A better code would be to ask the question first and then ask for the input:
print("A cherry is a: ")
print("   A. Dessert topping")
print("   B. Desert topping")
user_input = input("Please insert your answer: ")
if user_input.upper() == "A":
    print("Correct!")
else:
    print("Incorrect.")


# There are two things wrong with this code that tests if x is set to a positive value. One prevents it from running, and the other is subtle.
# Make sure the if statement works no matter what x is set to. Identify both issues. (2 pts)
# x == 4
# if x >= 0:
#     print("x is positive.")
# else:
#     print("x is not positive.")
# 1- In the first line, we are defining a variable, therefore we should use a single equal sign not double.
# 2- I can't find the issue... what is it?
x = 4
if x >= 0:
    print("x is positive.")
else:
    print("x is not positive.")

# What three things are wrong with the following code? (3 pts)
# x = input("Enter a number: ")
# if x = 3
#     print("You entered 3")
#
# 1- It has been defined that x must be a float
# 2- In an if statement, we must use a double equal sign
# 3- The if statement is missing the colon
# The correct code would be:
x = float(input("Enter a number: "))
if x == 3:
    print("You entered 3")


# There are four things wrong with this code. Identify all four issues. (4 pts)
# answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
# if a = "Beaker":
#     print("Correct!")
#     else
#     print("Incorrect! It is Beaker.")
#
# 1- The program is looking at a variable a, which has not been defined. It should look at variable answer.
# 2- In an if statement, we must use a double equal sign.
# 3- else should not be indented
# 4- it would be important to take into consideration case sensitivity
#
# The corrected code is:
answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
if answer.lower() == "beaker":
    print("Correct!")
else:
    print("Incorrect! It is Beaker.")


# This program doesn't work correctly. What is wrong? (1 pt)
# x = input("How are you today?")
# if x == "Happy" or "Glad":
#     print("That is good to hear!")
#
# The second condition is not properly defined in terms of x. Plus, it would be a good idea to account for case sensitivity. The correct code would be:
x = input("How are you today?")
if x.lower() == "happy" or x.lower() == "glad":
    print("That is good to hear!")


# Look at the code below. Write your best guess here on what it will print. Next, run the code and see if you are correct.
# Clearly label your guess and the actual answer. Also, if this or any other example results in an error, make sure to state that an error occurred.
# While you don't need to write an explanation, make sure you understand why the computer prints what it does. Don't get caught flat-footed when you need to know later. (2 pts)
# x = 5
# y = x == 6
# z = x == 5
# print("x=", x)
# print("y=", y)
# print("z=", z)
# if y:
#     print("Fizz")
# if z:
#     print("Buzz")
#
# My first guess:
# x = 5
# y = y
# z = 5
# Buzz
#
# Correct answer:
# x = 5
# y = False
# z = True
# Buzz
# I totally get how these statements are printed now. ;)


# Look at the code below. Write you best guess on what it will print. Next, run the code and see if you are correct. (2 pts)
# x = 5
# y = 10
# z = 10
# print(x < y)
# print(y < z)
# print(x == 5)
# print(not x == 5)
# print(x != 5)
# print(not x != 5)
# print(x == "5")
# print(5 == x + 0.00000000001)
# print(x == 5 and y == 10)
# print(x == 5 and y == 5)
# print(x == 5 or y == 5)
#
# my guess:
# True
# False
# True
# False
# False
# True
# False
# 0.00000000001 - correct answer is False.
# True
# False
# True
#
# I got it all right but the 4th last. I thought it would add zero + the number (because False is zero), so the result would be the actual number.
# Why does it skip the number completely?


# Look at the code below. Write you best guess on what it will print. Next, run the code and see if you are correct. (2 pts)
# print("3" == "3")
# print(" 3" == "3")
# print(3 < 4)
# print(3 < 10)
# print("3" < "4")
# print("3" < "10")
# print( (2 == 2) == "True" )
# print( (2 == 2) == True )
# print(3 < "3")
#
# my guess:
# True
# False
# True
# True
# error - correct answer was "True". Why is that? I thought we were comparing two strings of text, and so Python wouldn't be able to calculate > or <.
# error - correct answer was "False". I became even more confused when I realized that this one was false... is it because when comparing strings, it compares the first character first? And in this case 3 is not smaller than 1...
# False
# True
# False - correct answer was "ërror"


# What things are wrong with this section of code? The programmer wants to set the money variable according to the initial occupation the user selects. (1 pt)
# print("Welcome to Oregon Trail!")
# print("A. Banker")
# print("B. Carpenter")
# print("C. Farmer")
# user_input = input("What is your occupation? ")
# if user_input = A:
#     money = 100
# else if user_input = B:
#     money = 70
# else if user_input = C:
#     money = 50
# print("Great! you will start the game with", money, "dollars.")
#
# The answers need to be placed in quotation marks, the if statement should use double equal operator, the else if statement should be typed in as elif and the code should also account for case sensitivity.
# A better code would be:
print("Welcome to Oregon Trail!")

print("A. Banker")
print("B. Carpenter")
print("C. Farmer")

user_input = input("What is your occupation? ")

if user_input.lower() == "a":
    money = 100
elif user_input.lower() == "b":
    money = 70
elif user_input.lower() == "c":
    money = 50
print("Great! you will start the game with", money, "dollars.")