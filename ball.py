import pygame

class Ball:
    def __init__(self, screen, pos_x, pos_y, radius, speed, color):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.x_bounce = -1
        self.y_bounce = -1
        self.update_rect()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius)

    def update_position(self):
        screen_height = self.screen.get_height()
        self.pos_x += self.speed * self.x_bounce
        self.pos_y += self.speed * self.y_bounce

        # Collision with top or bottom of the screen
        if self.pos_y <= 0 + self.radius or self.pos_y >= screen_height - self.radius:
            self.y_bounce *= -1

        # Check if score
        if self.pos_x <= 0 or self.pos_x >= self.screen.get_width():
            self.reset()

        self.update_rect()

    def reset(self):
        self.pos_x = self.screen.get_width() // 2
        self.pos_y = self.screen.get_height() // 2
        self.x_bounce *= -1
        self.update_rect()

    def handle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.x_bounce *= -1

    def update_rect(self):
        self.rect = pygame.Rect(self.pos_x - self.radius, self.pos_y - self.radius, self.radius * 2, self.radius * 2)
