# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (0, 225, 255)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
OCEAN_GREEN = (11, 160, 89)
YELLOW = (250, 220, 8)
ORANGE = (250, 180, 8)

PI = 3.141592653

# Set the height and width of the screen
size = (700, 500)

# Create the screen
screen = pygame.display.set_mode(size)

# Name te screen
pygame.display.set_caption("Ocean's sunset")

# Loop until the user clicks the close button.
done = False

# Create a clock
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Sky
    pygame.draw.line(screen, SKY_BLUE, [0 ,0], [0,250], 1500)

    # Sun
    pygame.draw.circle(screen, YELLOW, (225, 250), 130, 130)

    # Ocean
    pygame.draw.line(screen, BLUE, [0,250], [0, 500], 1500)

    # Birds
    for offset in range(90, 0, -30):
        pygame.draw.arc(screen, BLACK, [365 + offset, 100+ offset, 110, 100], PI/6, PI / 2, 2)
        pygame.draw.arc(screen, BLACK, [455+ offset, 100+ offset, 110, 100],  PI/2, 5*PI/6, 2)

    # Sun's reflection on the ocean
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, ORANGE, [100 + y_offset, 260 + y_offset], [350 - y_offset, 260 + y_offset], 5)

    # Sailing Boat
    pygame.draw.polygon(screen, WHITE, [[350, 300], [360, 300], [360, 280], [365, 300], [375, 300], [370, 303], [355, 303]], 5)

    # Clouds
    for offset in range (0,390,130):
        pygame.draw.ellipse(screen, WHITE, [250 + offset, 70, 50, 25], 10)
        pygame.draw.circle(screen, WHITE, (270 + offset, 80), 10, 10)
        pygame.draw.circle(screen, WHITE, (295 + offset, 80), 20, 20)
        pygame.draw.circle(screen, WHITE, (320 + offset, 80), 10, 10)
        pygame.draw.ellipse(screen, WHITE, [290 + offset, 70, 50, 25], 10)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Sunset", True, BLACK)

    # Put the image of the text on the screen at 300x250
    screen.blit(text, [600, 400])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()