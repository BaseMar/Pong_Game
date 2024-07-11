import pygame
from paddle import Paddle
from ball import Ball

WINDOW_SIZE = (800, 600)
GAME_SPEED = 30
OBJECT_SPEED = 10
SLOW_DOWN_OBJECT = 3
BALL_RADIUS = 10


# setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Objects
r_paddle = Paddle(screen, pos_x=750, pos_y=230, width=20, height=120, speed=OBJECT_SPEED, color="red")
l_paddle = Paddle(screen, pos_x=50, pos_y=230, width=20, height=120, speed=OBJECT_SPEED, color="blue")
ball = Ball(screen, pos_x=390, pos_y=290, radius=BALL_RADIUS, speed=OBJECT_SPEED-SLOW_DOWN_OBJECT, color="white")

game_is_on = True

while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_on = False
            raise SystemExit

    # Clear previous frame
    screen.fill("black")

    # Update paddles position
    r_paddle.update_position(pygame.K_UP, pygame.K_DOWN)
    l_paddle.update_position(pygame.K_w, pygame.K_s)
    ball.update_position()

    # Draw paddles
    r_paddle.draw_paddle()
    l_paddle.draw_paddle()
    ball.draw_ball()

    pygame.display.update()
    clock.tick(GAME_SPEED)

pygame.quit()
