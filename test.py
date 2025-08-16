import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Circle")

# pygame.display.set_icon(pygame.image.load("icon.png"))

pygame.display.set_caption("Hellooo, game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 123)

# Circle setup
x, y = WIDTH // 2, HEIGHT // 2
radius = 20
speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    # Fill background
    screen.fill(WHITE)

    # Draw circle
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
