# Mikael's Rocket Space - MOD SELECTOR EDITION
import pygame
import random
import math

pygame.init()

# Screen setup
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mikael's Rocket Space - MOD SELECTOR")
clock = pygame.time.Clock()

# Load images
rocket_img = pygame.transform.scale(pygame.image.load(r"Game\\RocketSpace\\images\\rocket.png"), (100, 100))
enemy_img = pygame.transform.scale(pygame.image.load(r"Game\\RocketSpace\\images\\enemy.png"), (50, 50))
bullet_img = pygame.transform.scale(pygame.image.load(r"Game\\RocketSpace\\images\\bullet.png"), (20, 50))

# Fonts
font = pygame.font.SysFont(None, 40)
menu_font = pygame.font.SysFont("arialblack", 60)

def show_mode_menu():
    screen.fill((0, 0, 0))
    title = menu_font.render("Select Difficulty Mode", True, (255, 255, 255))
    screen.blit(title, (WIDTH//2 - 250, 100))

    modes = ["1 - EASY", "2 - MEDIUM", "3 - HARD", "4 - NIGHTMARE", "5 - HELLFIRE", "6 - DON'T EVEN TRY"]
    for i, mode in enumerate(modes):
        text = font.render(mode, True, (200, 200, 200))
        screen.blit(text, (WIDTH//2 - 100, 200 + i * 60))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_6:
                    return event.key - pygame.K_1

# Difficulty settings per mode
MODES = [
    {"name": "Easy", "enemies": 10, "homing": False, "lives": 3, "power_interval": 8000, "enemy_fire": 2},
    {"name": "Medium", "enemies": 20, "homing": False, "lives": 3, "power_interval": 6000, "enemy_fire": 4},
    {"name": "Hard", "enemies": 30, "homing": True, "lives": 2, "power_interval": 5000, "enemy_fire": 6},
    {"name": "Nightmare", "enemies": 40, "homing": True, "lives": 1, "power_interval": 4000, "enemy_fire": 10},
    {"name": "Hellfire", "enemies": 40, "homing": True, "lives": 1, "power_interval": 2000, "enemy_fire": 20},
    {"name": "DontEvenTry", "enemies": 50, "homing": True, "lives": 0, "power_interval": 10000, "enemy_fire": 30},
]

# Run game with selected mode
def run_game(config):
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = rocket_img
            self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
            self.speed = 8
            self.lives = config['lives']
            self.shield = False
            self.rapid_fire = False
            self.rapid_timer = 0

        def update(self, keys):
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.speed
            if self.rapid_fire and pygame.time.get_ticks() > self.rapid_timer:
                self.rapid_fire = False

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = enemy_img
            self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 50), random.randint(-300, -50)))
            self.speedx = random.choice([-1, 1]) * random.uniform(3, 6)
            self.speedy = random.uniform(1.5, 3.5)

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.right >= WIDTH or self.rect.left <= 0:
                self.speedx *= -1
            if self.rect.top > HEIGHT:
                self.rect.y = random.randint(-300, -50)
                self.rect.x = random.randint(0, WIDTH - self.rect.width)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, angle=None):
            super().__init__()
            self.image = pygame.Surface((10, 25))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = 12
            self.angle = angle

        def update(self):
            if self.angle is not None:
                self.rect.x += math.cos(self.angle) * self.speed
                self.rect.y += math.sin(self.angle) * self.speed
            else:
                self.rect.y -= self.speed
            if not screen.get_rect().colliderect(self.rect):
                self.kill()

    class PowerUp(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.type = random.choice(['shield', 'heal', 'rapid'])
            self.image = pygame.Surface((30, 30))
            self.image.fill({"shield": (0, 255, 255), "heal": (0, 255, 0), "rapid": (255, 255, 0)}[self.type])
            self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -30))
            self.speed = 3

        def update(self):
            self.rect.y += self.speed
            if self.rect.top > HEIGHT:
                self.kill()

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    enemies = pygame.sprite.Group([Enemy() for _ in range(config['enemies'])])
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    running = True
    game_over = False
    last_power_time = 0
    last_shot_time = 0

    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if not game_over and keys[pygame.K_SPACE]:
            if now - last_shot_time > (150 if player.rapid_fire else 400):
                bullet = Bullet(player.rect.centerx, player.rect.top)
                player_bullets.add(bullet)
                last_shot_time = now

        if now - last_power_time > config['power_interval']:
            powerups.add(PowerUp())
            last_power_time = now

        if random.randint(1, 100) <= config['enemy_fire']:
            shooter = random.choice(enemies.sprites())
            dx = player.rect.centerx - shooter.rect.centerx
            dy = player.rect.centery - shooter.rect.centery
            angle = math.atan2(dy, dx) if config['homing'] else None
            enemy_bullets.add(Bullet(shooter.rect.centerx, shooter.rect.bottom, angle))

        if not game_over:
            player.update(keys)
            enemies.update()
            player_bullets.update()
            enemy_bullets.update()
            powerups.update()

            for hit in pygame.sprite.groupcollide(enemies, player_bullets, False, True):
                hit.rect.y = random.randint(-300, -50)
                hit.rect.x = random.randint(0, WIDTH - hit.rect.width)

            if pygame.sprite.spritecollide(player, enemy_bullets, True):
                if player.shield:
                    player.shield = False
                else:
                    player.lives -= 1
                    game_over = player.lives < 1

            for power in pygame.sprite.spritecollide(player, powerups, True):
                if power.type == "shield":
                    player.shield = True
                elif power.type == "heal" and player.lives < 3:
                    player.lives += 1
                elif power.type == "rapid":
                    player.rapid_fire = True
                    player.rapid_timer = now + 5000

        player_group.draw(screen)
        enemies.draw(screen)
        player_bullets.draw(screen)
        enemy_bullets.draw(screen)
        powerups.draw(screen)

        lives_text = font.render(f"Lives: {player.lives}", True, (0, 255, 255) if player.shield else (255, 255, 255))
        screen.blit(lives_text, (10, 10))
        if player.rapid_fire:
            screen.blit(font.render("RAPID FIRE!", True, (255, 255, 0)), (10, 50))
        if game_over:
            screen.blit(menu_font.render("YOU DIED", True, (255, 0, 0)), (WIDTH // 2 - 200, HEIGHT // 2 - 60))

        pygame.display.flip()
        clock.tick(60)

# ----- RUN -----
selected_mode = show_mode_menu()
run_game(MODES[selected_mode])
