# WORKSHEET 4

import random

# Write a Python program that will use a for loop to print your name 10 times, and then the word ``Done'' at the end.
for i in range (10):
    print("Diana")
print("Done")
print()


# Write a Python program that will use a for loop to print ``Red'' and then ``Gold'' 20 times. (Red Gold Red Gold Red Gold... all on separate lines. Don't use \n.)
for i in range (20):
    print("Red")
    print("Gold")
print()


# Write a Python program that will use a for loop to print the even numbers from 2 to 100, inclusive.
for i in range (2,102,2):
    print(i)
print()


# Write a Python program that will use a while loop to count from 10 down to, and including, 0. Then print the words ``Blast off!'' Remember, use a WHILE loop, don't use a FOR loop.
i=10
while i >= 0:
    print(i)
    i = i - 1
print("Blast off!")
print()

# There are three things wrong with this program. List each. (3 pts)
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = input("Enter a number: ")
#     total = total + i
# print("The total is:", x)
# 1- The first mistake is not really a mistake, but it would be easier to understand the code if the variable x was more descriptive of what it actually represents. Let's call it input_number.
# 2- The next actual mistake is that x (the input) is currently not being used in the sum. It should be total = total + x , or , total = total + input_number. It doesn't make sense to add total to i.
# 3- The next mistake is that the format for the input has not been defined. It should be defined as a float or an int, so that the sum can happen in the next line of code.
# 4- The last mistake is to say that the total is x. x is an input. The total is the same as the value of the variable total. Here is the corrected code:
total = 0
for i in range(3):
    input_number = float(input("Enter a number: "))
    total = total + input_number
print("The total is:", total)
print()

# Write a program that prints a random integer from 1 to 10 (inclusive).
import random
random_int = random.randrange(1, 11)
print(random_int)
print()

# Write a program that prints a random floating point number somewhere between 1 and 10 (inclusive). Do not make the mistake of generating a random number from 0 to 10 instead of 1 to 10.
random_float = 1 + random.random()*9
print(random_float)
print()

# or maybe I can also do the below
random_float = random.random() + random.randrange(1, 10)
print(random_float)
print()

# Write a Python program that will: (3 pts)
# Ask the user for seven numbers
# Print the total sum of the numbers
# Print the count of the positive entries, the number entries equal to zero, and the number of negative entries. Use an if, elif, else chain, not just three if statements.
total = 0
positive_entries = 0
zero_entries = 0
negative_entries = 0
for i in range (7):
    input_number = float(input("Please enter a number:"))
    total = total + input_number
    if input_number > 0:
        positive_entries = positive_entries + 1
    elif input_number == 0:
        zero_entries = zero_entries + 1
    else:
        negative_entries = negative_entries + 1
print()
print("The sum of all entries is", total)
print("The number of positive entries is", positive_entries)
print("THe number of entries equal to zero is", zero_entries)
print("The number of negative entries is", negative_entries)
print()

# Coin flip tosser: (4 pts)
# Create a program that will print a random 0 or 1.
# Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list, as shown in the chapter.
# Add a loop so that the program does this 50 times.
# Create a running total for the number of heads flipped, and the number of tails.
total_heads = 0
total_tails = 0
for i in range (50):
    coin_flip = random.randrange(2)
    if coin_flip == 0:
        print("Heads")
        total_heads = total_heads + 1
    else:
        print("Tails")
        total_tails = total_tails + 1
print()
print("The total number of \"Heads\" was", total_heads)
print("The total number of \"Tails\" was", total_tails)
print()

# Write a program that plays rock, paper, scissors: (4 pts)
# Create a program that randomly prints 0, 1, or 2.
# Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list, as shown in the chapter.
# Add to the program so it first asks the user their choice.
# (It will be easier if you have them enter 1, 2, or 3.)
# Add conditional statement to figure out who wins.

# user input
i = 0
while i != 1:
    user_input = input("If you want to quit, write \"quit\", otherwise, chose between rock, paper or scissors: ")
    if "rock" in user_input.lower() or user_input.lower() == "r":
        print("user input:", "rock")
    elif "paper" in user_input.lower() or user_input.lower() == "p":
        print("user input:", "paper")
    elif "scissors" in user_input.lower() or user_input.lower() == "s" or "scisors" in user_input.lower() or "scisor" in user_input.lower() or "scissor" in user_input.lower():
        print("user input:", "scissors")
    elif user_input.lower() == "quit" or user_input.lower() == "q":
        i = 1
# program input
    if i != 1:
        program_input = random.randrange(3)
        if program_input == 0:
            print("program input:", "rock")
        elif program_input == 1:
            print("program input:", "paper")
        elif program_input == 2:
            print("program input:", "scissors")
# who wins?
    if ("rock" in user_input.lower() or user_input.lower() == "r") and program_input == 0:
        print("It is a draw.")
    elif ("rock" in user_input.lower() or user_input.lower() == "r") and program_input == 1:
        print("Too bad, you lose.")
    elif ("rock" in user_input.lower() or user_input.lower() == "r") and program_input == 2:
        print("Congratulations, you win!")
    elif ("paper" in user_input.lower() or user_input.lower() == "p") and program_input == 0:
        print("Congratulations, you win!")
    elif ("paper" in user_input.lower() or user_input.lower() == "p") and program_input == 1:
        print("It is a draw.")
    elif ("paper" in user_input.lower() or user_input.lower() == "p") and program_input == 2:
        print("Too bad, you lose.")
    elif ("scissors" in user_input.lower() or user_input.lower() == "s" or "scisors" in user_input.lower() or "scisor" in user_input.lower() or "scissor" in user_input.lower()) and program_input == 0:
        print("Too bad, you lose.")
    elif ("scissors" in user_input.lower() or user_input.lower() == "s" or "scisors" in user_input.lower() or "scisor" in user_input.lower() or "scissor" in user_input.lower()) and program_input == 1:
        print("Congratulations, you win!")
    elif ("scissors" in user_input.lower() or user_input.lower() == "s" or "scisors" in user_input.lower() or "scisor" in user_input.lower() or "scissor" in user_input.lower()) and program_input == 2:
        print("It is a draw.")
