import pygame


class Paddle:
    def __init__(self, screen, pos_x, pos_y, width, height, speed, color):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.Rect)

    def update_position(self, key_up, key_down):
        keys = pygame.key.get_pressed()
        if keys[key_up]:
            self.Rect.y -= self.speed
        if keys[key_down]:
            self.Rect.y += self.speed

        if self.Rect.y <= 0:
            self.Rect.y = 0
        if self.Rect.y > self.screen.get_height() - self.Rect.height:
            self.Rect.y = self.screen.get_height() - self.Rect.height
