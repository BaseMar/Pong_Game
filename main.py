import pygame

WINDOW_SIZE = (800, 600)
GAME_SPEED = 60

# setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill("black")
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

game_is_on = True

while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_on = False
            raise SystemExit

    pygame.display.update()
    clock.tick(GAME_SPEED)

pygame.quit()

