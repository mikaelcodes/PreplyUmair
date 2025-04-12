import pygame as pg

# Initialize Pygame
pg.init()

# Set up the display
screen_width = 1200
screen_height = 800
root = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Mikael's Rocket Space")

# Load and resize the rocket image Game\RocketSpace\images\bullet.png
rocket = pg.image.load(r"Game\RocketSpace\images\rocket.png")
rocket = pg.transform.scale(rocket, (100, 100))

# Load and resize the bullet image
bullet_image = pg.image.load(r"Game\RocketSpace\images\bullet.png")
bullet_image = pg.transform.scale(bullet_image, (20, 50))

# Game variables
running = True
rocket_x = 350
rocket_y = screen_height -100 # Start position of the rocket
rocket_width = 100
bullet_speed = 5
bullets = []


# Main game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Create a new bullet at the top of the rocket
                bullet_x = rocket_x + rocket_width // 2 - 10  # Center the bullet
                bullet_y = rocket_y
                bullets.append([bullet_x, bullet_y])

    # Continuous key press for rocket movement
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and rocket_x > 0:
        rocket_x -= 5
    if keys[pg.K_RIGHT] and rocket_x < screen_width - rocket_width:
        rocket_x += 5

    # Update bullet positions
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed  # Move the bullet upward
        if bullet[1] < 0:  # Remove bullets that go off-screen
            bullets.remove(bullet)

    # Draw everything
    root.fill((0, 255, 0))  # Background color
    root.blit(rocket, (rocket_x, rocket_y))  # Draw the rocket
    for bullet in bullets:
        root.blit(bullet_image, (bullet[0], bullet[1]))  # Draw bullets

    pg.display.update()

# Quit Pygame
pg.quit()