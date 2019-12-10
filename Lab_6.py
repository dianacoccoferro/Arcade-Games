# LAB 6


# Each part of this lab is worth 5 points.
#
# 6.1 Part 1
# Write a Python program that will print the following:
#
# 10
# 11 12
# 13 14 15
# 16 17 18 19
# 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36 37
# 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54
#
#
x = 10
for i in range (10):
    for j in range (i):
        print(x, end = " ")
        x = x + 1
    print()

print()


# 6.2 Part 2
# Create a big box out of n rows of little o's for any desired size n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.
#
# E.g. n = 3
# oooooo
# o    o
# oooooo
#
# E.g. n = 8
# oooooooooooooooo
# o              o
# o              o
# o              o
# o              o
# o              o
# o              o
# oooooooooooooooo

n=int(input("Please introduce a value n: "))
print("o"*2*n)
for a in range (n):
    print("o", end = "")
    for b in range (n):
        print ("  ", end="")
    print("o", end = "")
    print()
print("o"*2*n)

print()



# 6.3 Part 3
# Print the following for any positive integer n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.
#
# E.g. n = 3
#
# 1 3 5 5 3 1
# 3 5     5 3
# 5         5
# 5         5
# 3 5     5 3
# 1 3 5 5 3 1
#
# E.g. n = 5
# 1 3 5 7 9 9 7 5 3 1
# 3 5 7 9     9 7 5 3
# 5 7 9         9 7 5
# 7 9             9 7
# 9                 9
# 9                 9
# 7 9             9 7
# 5 7 9         9 7 5
# 3 5 7 9     9 7 5 3
# 1 3 5 7 9 9 7 5 3 1
# Don't worry about handling the spacing for multi-digit numbers. Chapter 20 covers this if you want to look ahead, but it isn't needed.
#
# This part of the lab is difficult. Skip to part 4 if you aren't interested in the challenge.

n = int(input("Please insert a value of n: "))
a = 1
b = -1
for i in range (1,n+1):
    # counting up
    for j in range (1,n+1):
        if a <= 2*n-1:
            print(a, end = " ")
            a = a + 2
    # adding spaces
    print((b+1)*"  ", end = "")
    # counting down
    for j in range (n,2*n):
        if a >= 2*n-1:
            a = 2*n-1
        if a <= 2*n-1 and a > b:
            print(a, end = " ")
            a = a - 2
    b = b + 2
    a = b + 2
    print()
a = 2*n-3
b = 2*n-1
for i in range (1,n):
    # counting up
    for j in range (1,n+1):
        if a <= 2*n-1:
            print(a, end = " ")
            a = a + 2
    b = b - 2
    # adding spaces
    print((b-1)*"  ", end = "")
    # counting down
    a = 2*n-1
    for j in range (n+1, 2*n+1):
        if a >= b:
            print (a, end = " ")
            a = a - 2
    print()


# 6.4 Part 4
# Start with the pygame template code.
#
# Use nested for loops to draw small green rectangles. Make the image look like Figure 27.1.
# Do not create the grid by drawing lines, use a grid created by rectangles.

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (705, 505)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic

    # --- Screen-clearing
    screen.fill(BLACK)

    # --- Drawing code
    for i in range (0, 700, 10):
        for j in range (0,500, 10):
            pygame.draw.rect(screen, GREEN, [5 + i, 5+j, 5, 5], 2)
            pygame.draw.line(screen, GREEN, [6 + i, 7+j], [8 + i, 7+j], 2)
    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

