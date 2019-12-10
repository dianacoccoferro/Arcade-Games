# Worksheet 5

# Reminder: Please use full sentences, capital letters, and proper grammar where appropriate.
# Reminder: Please use full sentences, capital letters, and proper grammar where appropriate.
#
# Explain how the computer coordinate system differs from the standard Cartesian coordinate system. There are two main differences. List both.
# 1 - The y coordinates are reversed, they go up as we move down the screen
# 2 - The screen covers the lower right quadrant, whereas the cartesian coordinate system usually focuses on the upper right quadrant.

# Before a Python Pygame program can use any functions like pygame.display.set_mode(), what two lines of code must occur first?
import pygame
pygame.init()

# Explain how WHITE = (255, 255, 255) represents a color.
# The code is essentially telling the screen to show as much red, green and blue as possible, when that happens, the computer shows white.

# When do we use variable names for colors in all upper-case, and when do we use variable names for colors in all lower-case? (This applies to all variables, not just colors.)
# We use all upper case when the color is intended to remain the same throughout the code. We tend to do that for solid colours.\
# If we want the color to change, we use all lower-case. Eg. the sky color throughout the day.

# What does the pygame.display.set_mode() function do?
# It can open a window, create games that run in a full-screen mode, remove the start menu, the title bars, give control to the game of everything on the screen.

# What does this for event in pygame.event.get() loop do?
# It sets the event processing loop, allowing the programer to establish a way for the user the interact with the program.

# What is pygame.time.Clock used for?
# It is used to create a clock. Later in the code we may want to use that clock to limit the number of frames per second.

# For this line of code: (3 pts)
#         pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
# What does screen do?
# It sets the location of where the line should be drawn

# What does [0, 0] do?
# It sets the coordinates for the origin of the line.

# What does [100, 100] do?
# It sets the coordinates for the end of the line.

# What does 5 do?
# Sets the thickness (no of pixels) of the line.

# What is the best way to repeat something over and over in a drawing?
# Using a looped offset rule to change the coordinates.

# When drawing a rectangle, what happens if the specified line width is zero?
# The rectangle is not drawn.

# Describe the ellipse drawn in the code below.
# pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
# What is the x, y of the origin coordinate?
# x = 20 and y = 20

# What does the origin coordinate specify? The center of the circle?
# No, the upper left corner of the rectangle where the ellopse would be contained in.

# What is the length and the width of the ellipse?
# widht = 250 - 20 = 230
# lenght = 100 - 20 = 80

# When drawing an arc, what additional information is needed over drawing an ellipse?
# The range of angles we want to draw

# Describe, in general, what are the three steps needed when printing text to the screen using graphics?
# we need to select the font, create and render the text, and finally print it on the screen.

# When drawing text, the first line of the three lines needed to draw text should actually be outside the main program loop.
# It should only run once at the start of the program. Why is this? You may need to ask.
# Because it is defining a variable, so we can set it up in the beginning, when we define other variables such as size or screen.

# What are the coordinates of the polygon that the code below draws?
# pygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)
# The coordinates are the ones set in squared parenthesis.

# What does pygame.display.flip() do?
# It updates the screen with whatever drawings have been done and it should be placed after all the drawings commands.

# What does pygame.quit() do?
# Closes the window and quits.

# Look up on-line how the pygame.draw.circle works. Get it working and paste a working sample here.
# I only need the one line of code that draws the circle, but make sure it is working by trying it out in a full working program.
pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)