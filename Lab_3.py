print("THE BEST QUIZZ EVER")

print()
name = input("First things first: What is your name?")
print("Hi", name, ", welcome to the best quizz ever!")
right_answers = 0

# QUESTION 1
print()
print("Question 1. The heart of a blue whale is the size of...")
print(" A. a pillow \n B. an average human body \n C. a small car")
answer = input("Answer:")

if answer.lower() == "c" or "car" in answer.lower():
    print("Correct!")
    right_answers = right_answers + 1
else:
    print("nah... bigger, it is actually the size of a small car")

# QUESTION 2
print()
print("Question 2. Which month has 28 days?")

answer = input("Answer:")

if "all"in answer.lower() or "every" in answer.lower():
    print("Correct!")
    right_answers = right_answers + 1
elif answer.lower() == "feb" or answer.lower() == "february" or answer == "2" or answer == "02":
    print("February, really? Didn't that sound too easy? Actually, all months have 28 days, most of them have even more...")
else:
    print("I am not sure what you mean, but it is probably not right. All months do!")

# QUESTION 3
print()
print("Question 3. How fast can an elephant run?")

answer = int(input("Answer in km/h:"))

if answer < 40:
    print("Elephants are big, man... they can go faster than that! 40km/h is the right answer.")
elif answer == 40:
    print("Spot on, man! You know some weird shit...")
    right_answers = right_answers + 1
elif answer > 40 and answer < 50:
    print ("Ah, almost! It is actually 40km/h")
else:
    print("Well, it is an elephant, not a cheetah... They run at 40km/h")

# QUESTION 4
print()
print("Question 4: What does space smell like?")
print(" A. sulfur \n B. seared stake \n C. rubber")

answer = input("Answer:")

if answer.lower() == "b" or "steak" in answer.lower():
    print("Exactly! Either you really know some useless facts, or you are weirdly good at guessing!")
    right_answers = right_answers + 1
else:
    print("nah... according to some former astronauts, space does have a distinct odor that hangs around post-spacewalk. They've described it as \"hot metal\" or \"searing steak.\"")

# QUESTION 5
print()
print("Question 5: Myth or reality? Riding a roller coaster could help you pass a kidney stone?")

answer = input("Answer:")

if answer.lower() == "reality" or "true" in answer.lower() or answer.lower() == "right" or answer.lower() == "yes" or answer.lower() == "y" or answer.lower() == "truth":
    print("That's right, get yourself a flight to Disney World and make sure you get a back seat on the roller coaster!")
    right_answers = right_answers + 1
else:
    print("You actually can, especially if you go to Disney World and make sure you get a back seat on the roller coaster!")
print("After multiple people reported they had passed a kidney stone while riding Walt Disney World's Big Thunder Mountain Railroad ride,")
print("a research team from Michigan State University conducted tests with a model kidney")
print("and found that there was a 64% kidney stone pass rate for those seated in the rear of the Thunder Mountain ride.")
print("That number was just 16 percent for those seated in the front.")

# Calcuating the Final Score
print()
print()
print("The quizz is over")
number_of_questions = 5
score = (right_answers / number_of_questions)*100
if score >= 50:
    print("Congratulations, you got ", right_answers, "questions right.")
if score < 50:
    print("You will do better next time. Right now you got ", right_answers, "questions right.")
print("That is a score of", int(score), "%.")