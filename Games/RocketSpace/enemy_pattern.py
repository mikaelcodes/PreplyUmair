import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(r"Games\RocketSpace\images\enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize enemy image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.vertical_speed = 0.4  # Slow downward movement speed

    def update(self):
        self.rect.x += self.speed  # Move enemy horizontally
        self.rect.y += self.vertical_speed  # Slowly move enemy downward
        if self.rect.right > 800 or self.rect.left < 0:  # Screen width boundary check
            self.speed = -self.speed  # Reverse direction

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # Create a simple bullet
        self.image.fill((255, 0, 0))  # Red color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 5  # Move bullet downward
        if self.rect.top > 600:  # Remove bullets that go off-screen
            self.kill()

# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Enemy Movement and Attack")
    clock = pygame.time.Clock()

    # Create enemy instances in a row
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    for i in range(10):  # Create 10 enemies in a row
        enemy = Enemy(50 + i * 70, 50, 2)  # Adjust spacing between enemies
        enemies.add(enemy)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Randomly make enemies shoot bullets
        if random.randint(1, 100) <= 2:  # 2% chance per frame for an enemy to shoot
            shooting_enemy = random.choice(enemies.sprites())
            bullet = Bullet(shooting_enemy.rect.centerx, shooting_enemy.rect.bottom)
            bullets.add(bullet)

        # Update all sprites
        enemies.update()
        bullets.update()

        # Draw everything
        screen.fill((0, 0, 0))  # Clear screen with black
        enemies.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()