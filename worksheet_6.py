# WORKSHEET 6
#
# For each of the first two questions, write out your best guess as to what the code will print.
# Clearly label this as your guess. Then run the code and look at the output. Write if your guess was correct.
# If it was not, briefly describe what was different and why.
#
# Predicting what the code will do is important in writing programs, and figuring out why programs don't run the way expected.

# What does this program print out? (Remember: TWO answers. Your guess and the actual result. Label both.)
# x = 0
# while x < 10:
#     print(x)
#     x = x + 2
# My guess was correct:
# Vertical thread of the following numbers: 0, 2, 4, 6, 8


# What does this program print out?
# x = 1
# while x < 64:
#    print(x)
#    x = x * 2
# My guess was correct.
# Vertical print out of te following numbers: 1, 2, 4, 8, 16 and 64


# Why is the ``and x >= 0'' not needed?
# x = 0
# while x < 10 and x >= 0:
#     print(x)
#     x = x + 2
# Answer: Because we set 0 as an initial value of 0 and we set it so that it increases value by two every time. Therefore, the value of x is always growing and it will never be lower than zero.


# What does this program print out? (0 pts) Explain. (1 pt)
# x = 5
# while x >= 0:
#     print(x)
#     if x == "1":
#         print("Blast off!")
#     x = x - 1
# Answer: It prints out a vertical thread of the following numbers and text: 5, 4, 3, 2, 1, and 0.
# To start with, x is 5, therefore that number is printed. Then x dimisnes by 1 every time until x=0, so we get the numbers 5 to 0 printed in a decreasing order.
# "Blast off" would only be printed if x was ever equal to the string of text "1". That doesn't happen, because x is always an integer that changes its value. It is was text, it wouldnt change value.


# Fix the following code so it doesn't repeat forever, and keeps asking the user until he or she enters a number greater than zero: (2 pts)
# x = float(input("Enter a number greater than zero: "))
# while x <= 0:
#    print("Too small. Enter a number greater than zero: ")
# My answer:
# x = float(input("Enter a number greater than zero: "))
# while x <= 0:
#    print("Too small. Enter a number greater than zero: ")
#    x = float(input("Enter a number greater than zero: "))


# Fix the following code:
# x = 10
# while x < 0:
#     print(x)
#     x - 1
# print("Blast-off")
# My answer: change the < signal to >, add "x=" to the last line of code
# x = 10
# while x > 0:
#     print(x)
#     x = x - 1
# print("Blast-off")


# What is wrong with this code? It runs but it has unnecessary code. Find all the unneeded code. Also, answer why it is not needed. (1 pt)
# i = 0
# for i in range(10):
#     print(i)
#     i += 1
# Answer: A simplified code would be:
# for i in range(10):
#     print(i)
# The first line of code is not necessary, because when we define the range, we are already setting i to an initial value of 0.
# Also the last line of code is not necessary because when we define the range, we are already setting i to increase by an incremental value of 1.


# Explain why the values printed for x are so different. (2 pts)
# # Sample 1
# x = 0
# for i in range(10):
#     x += 1
# for j in range(10):
#     x += 1
# print(x)
#
# # Sample 2
# x = 0
# for i in range(10):
#     x += 1
#     for j in range(10):
#         x += 1
# print(x)
# Answer: the reason for tht is that in sample 1, x increases by a value of one, 2 x 10 = 20 times. In sample 2, x increases by a value of 1, 10 + 10 x 10 = 110 times.