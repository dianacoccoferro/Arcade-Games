# LAB 4

# instructions
print()
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert. It is a 200 mile journey.")
print("The natives want their camel back, and are chasing you down. They are currently 20 miles behind you.")
print("Survive your trek and outrun the natives.")
print("Note that your status checks and drinks from the canteen are immediate, so they won't make your camel tired.")
print()

# variables
done = False
distance = 0
distance_last_trip = 0
thirst = 0
tiredness = 0
natives_distance = -20
drinks = 3

# user moves
import random
while done != True:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    user_move = input("Your move? ")
    print()
    if "a" in user_move.lower() or "drink" in user_move.lower() and tiredness <= 8 and thirst <= 6 and distance < 200 and natives_distance <0 and not done:
        if drinks > 0:
            drinks = drinks -1
            thirst = 0
            print("Oh yeah, that was a good sip. You are hydrated again.")
            print()
        else:
            print("Sorry, but you have no more drinks left in the canteen.")
            print()
    elif "b" in user_move.lower() or "moderate" in user_move.lower() and tiredness <= 8 and thirst <= 6 and distance < 200 and natives_distance <0 and not done:
        distance_last_trip = random.randrange(5, 12)
        distance = distance + distance_last_trip
        print("You traveled", distance_last_trip, "miles.")
        print()
        thirst = thirst + 1
        tiredness = tiredness + 1
        natives_distance = natives_distance + random.randrange(7, 15) - distance_last_trip
    elif "c" in user_move.lower() or "full" in user_move.lower() and tiredness <= 8 and thirst <= 6 and distance < 200 and natives_distance <0 and not done:
        distance_last_trip = random.randrange(10,18)
        distance = distance + distance_last_trip
        print("You traveled", distance_last_trip, "miles.")
        print()
        thirst = thirst + 1
        tiredness = tiredness + random.randrange(1,4)
        natives_distance = natives_distance + random.randrange(7,15) - distance_last_trip
    elif "d" in user_move.lower() or "stop" in user_move.lower() and tiredness <= 8 and thirst <= 6 and distance < 200 and natives_distance <0 and not done:
        tiredness = 0
        print("The camel is now happy and well rested.")
        print()
        natives_distance = natives_distance + random.randrange(7,15)
    elif "e" in user_move.lower() or "status" in user_move.lower():
        print("Miles Traveled:", distance)
        print("Drinks left in the canteen:", drinks)
        print("The natives are", natives_distance*-1, "miles behind you.")
        print()
    elif "q" in user_move.lower() or "quit" in user_move.lower():
        done = True

# thirst level
    if thirst > 4 and thirst <= 6 and tiredness <= 8 and distance < 200 and natives_distance <0 and not done:
        print("Your are thirsty.")
        print()
    elif thirst > 6:
        print("You died of thirst. The natives got their camel back.")
        print()
        done = True

# tiredness level
    if tiredness > 5 and tiredness <= 8 and thirst <=6 and distance < 200 and natives_distance <0 and not done:
        print("Your camel is getting tired.")
        print()
    elif tiredness > 8:
        print("Your camel died of tiredness. The natives caught you and killed you. It was ugly.")
        print()
        done = True

# natives distance
    if natives_distance >= 0:
        print("Oh no! The natives caught you and killed you. It was ugly.")
        print()
        done = True
    elif natives_distance < 0 and natives_distance >= -15 and thirst <=6 and distance < 200 and not done:
        print("The natives are getting close.")
        print()

# total distance
    if distance >= 200 and not done:
        print("Congratulations! You made it accross the desert! You won!")
        done = True
        print()

# finding an oasis
    if random.randrange(1,21) == 20 and tiredness <= 8 and thirst <=6 and distance < 200 and natives_distance <0 and not done:
        print("Congratulations! You found an osasis. Your canteen has been refilled and your camel got instantly well rested.")
        drinks = 3
        tiredness = 0