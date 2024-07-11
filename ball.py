import pygame


class Ball:
    def __init__(self, screen, pos_x, pos_y, radius, speed, color):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.speed = speed
        self.color = color

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius)

    def update_position(self):
        self.pos_x += self.speed
        self.pos_y += self.speed
