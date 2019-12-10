# Chapter 01 Worksheet
# Return to worksheet index.

# When writing answers to questions, please use proper grammar, capitalization, and punctuation. Please limit the length of each line to 80 characters.

# Write a line of code that will print your name.
print("Diana")

# How do you enter a comment in a program?
# You do it like this

# What do the following lines of code output? ALSO: Why do they give a different answer?
# print(2 / 3) - this makes the calculation and prints out the actual number
# print(2 // 3) - this makes the calculation and prints out the integer of that value (rounded down)

# Write a line of code that creates a variable called pi and sets it to an appropriate value.
pi=3.14159

# Why does this code not work?
# A = 22
# print(a)
# because variables are case sensitive

# All of the variable names below can be used. But which ONE of these is the better variable name to use?
# a
# A
# Area
# AREA
# area
# area_of_rectangle - this one, because it starts with lower case and it is self-explanatory
# Area_Of_Rectangle

# Which of these variables names are not allowed in Python? (More than one might be wrong. Also, this question is not asking about improper names, just names that aren't allowed. Test them if you aren't sure.)
# apple
# Apple
# APPLE - this is a constant, not a variable
# Apple2
# 1Apple - not allowed, as it starts with a number
# account number not allowed, as it has a space
# account_number
# account.number - not allowed because it has a dot
# accountNumber
# account# - not allowed as it as a special character
# pi
# PI
# fred
# Fred
# GreatBigVariable
# greatBigVariable
# great_big_variable
# great.big.variable - not allowed because it has a dot
# 2x - not allowed, as it starts with a number
# x2x
# total% - not allowed as it as a special character
# #left - not allowed, this is a comment


# Why does this code not work?
# print(a)
# a = 45
# because we are asking to print a variable that has not yet been defined, it is only defined in the second line

# Explain the mistake in this code:
# pi = float(3.14)
# I dont see a mistake, I just see a redundancy. 3.14 is already a float, there is no need to convert it into a float again

# This program runs, but the code still could be better. Explain what is wrong with the code.
# radius = float(input("Radius:"))
# x = 3.14
# pi = x
# area = pi  * radius ** 2
# print(area)
# we could just define pi as 3.14 instead of adding complexity by creating a new variale x and then assign that value to pi. In the current code we end up having two variables with the same value, x and pi, however x is never used.

# Explain the mistake in the following code:
x = 4
y = 5
a = ((x)*(y))
print(a)
#I dont see a mistake in the code, the code runs, I just dont see the need for all the parenthesis when defining the variable a, the code would run smoothly without them

# Explain the mistake in the following code:
# x = 4
# y = 5
# a = 3(x + y)
# print(a)
#Python doesnt read mathematical equiations as we learned in school. In this case, when defining a,  we still need to add the multiplied * between 3 and the parenthesis:
x = 4
y = 5
a = 3*(x + y)
print(a)

# Explain the mistake in the following code:
# radius = input(float("Enter the radius:"))
# It seems like we want to define the input to be converted into a float, but instead, the coder is coding it the otherway around. In other words, we would have to code it like this, instead:
radius = float(input("Enter the radius:"))

# Do all these print the same value? Which one is better to use and why?
# print(2/3+4)
# print(2 / 3 + 4)
# print(   2 /    3+    4  )
# Yes, they all print the same, but it is much better to use the second one because it is much easier to read

# What is a constant?
# it is a variable that doesnt vary throughout the code.

# How are variable names for constants different than other variable names?
# They start with a capital letter

# What is a single quote and what is a double quote? Give and label an example of both.
# 'This is a single quote and "This is a double quote.

# Write a Python program that will use escape codes to print a double-quote and a new line using the Window's standard. (Note: I'm asking for the Window's standard here. Look it up out of Chapter 1.)
print ("This is how\r\nyou spell\r\n\"this\".")

# Can a Python program print text to the screen using single quotes instead of double quotes?
# Yes

# Why does this code not calculate the average?
# print(3 + 4 + 5 / 3)
# Because Python uses the standards of conventional math, where the division is done prior to the rest of the equation. If we want to calculate an average, we need to use parenthesis, like below
print((3+4+5)/3)

# What is an ``operator'' in Python?
# It is a character that defines a mathematical operation. Eg * is the operator for multiplication.

# What does the following program print out?
# x = 3
# x + 1
# print(x)
# It prints 3, because in the second line, we didn't make any changes to the variable, we simple made a statement. If we wanted to change x, we would have to code it as follows:
x=3
x=x+1
print(x)

# Correct the following code:
# user_name = input("Enter your name: )"
user_name = input("Enter your name: ")

# Correct the following code:
# value = int(input(print("Enter your age")))
value = int(input("Enter your age: "))
print(value)
