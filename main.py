import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WINDOW_SIZE = (800, 600)
GAME_SPEED = 30
OBJECT_SPEED = 10
SLOW_DOWN_OBJECT = 3
BALL_RADIUS = 10
GAME_OVER_MAX_POINTS = 1


# setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Objects
r_paddle = Paddle(screen, pos_x=750, pos_y=230, width=20, height=120, speed=OBJECT_SPEED, color="red")
l_paddle = Paddle(screen, pos_x=50, pos_y=230, width=20, height=120, speed=OBJECT_SPEED, color="blue")
score = Scoreboard(max_points=GAME_OVER_MAX_POINTS)
ball = Ball(screen, pos_x=screen.get_width()//2, pos_y=screen.get_height()//2, radius=BALL_RADIUS, speed=OBJECT_SPEED-SLOW_DOWN_OBJECT, color="white", scoreboard=score)


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

    # Check for collisions with paddles
    ball.handle_collision(r_paddle)
    ball.handle_collision(l_paddle)

    score.show_score_l(screen)
    score.show_score_r(screen)

    if score.l_score == GAME_OVER_MAX_POINTS or score.r_score == GAME_OVER_MAX_POINTS:
        score.game_over(screen)

    ball.update_position()

    # Draw paddles
    r_paddle.draw_paddle()
    l_paddle.draw_paddle()
    ball.draw()

    pygame.display.update()
    clock.tick(GAME_SPEED)

pygame.quit()
