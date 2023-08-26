import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set window caption
pygame.display.set_caption("Shreyansh Singh - CodeGrah - Game")

# Define the flags for the window (including resizable and minimized)
window_flags = pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF

# Create the window with the defined flags
screen = pygame.display.set_mode(window_size, window_flags)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            

    # Update game logic and draw here

    # Update the display
    pygame.display.flip()

    screen.fill("purple")

# Quit Pygame
pygame.quit()
sys.exit()