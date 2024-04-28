import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 400, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_color = (255, 255, 0)
gravity = 0.25
jump = -5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird_y += jump
                
    # Apply gravity
    bird_y += gravity

    # Clear the screen
    WINDOW.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    
    
    
    
    
    
    ((0, 0, 0))

    # Draw the bird
    pygame.draw.circle(WINDOW, bird_color, (bird_x, int(bird_y)), bird_radius)

    # Update the display
    pygame.display.update()

    # Set the frames per second
    pygame.time.Clock().tick(60)

pygame.quit()
