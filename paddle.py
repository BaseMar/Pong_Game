import pygame

class Paddle:
    def __init__(self, screen, pos_x, pos_y, width, height, speed, color):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_position(self, key_up, key_down):
        keys = pygame.key.get_pressed()
        if keys[key_up]:
            self.rect.y -= self.speed
        if keys[key_down]:
            self.rect.y += self.speed

        # Block moving out of screen
        screen_height = self.screen.get_height()
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
