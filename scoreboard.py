import time
import pygame


class Scoreboard:
    def __init__(self, max_points):
        self.color = "white"
        self.font = pygame.font.SysFont('times new roman', 30)
        self.r_score = 0
        self.l_score = 0
        self.max_points = max_points

    def show_score_l(self, surface):
        score_surface_l = self.font.render(f'{self.l_score}', True, self.color)
        score_rect = score_surface_l.get_rect(center=((surface.get_width()//2)-100, 30))
        surface.blit(score_surface_l, score_rect)

    def show_score_r(self, surface):
        score_surface_r = self.font.render(f'{self.r_score}', True, self.color)
        score_rect = score_surface_r.get_rect(center=((surface.get_width()//2)+100, 30))
        surface.blit(score_surface_r, score_rect)

    def game_over(self, surface):
        if self.l_score == self.max_points:
            game_over_surface = self.font.render('Blue pallet won', True, "blue")
        elif self.r_score == self.max_points:
            game_over_surface = self.font.render('Red pallet won', True, "red")

        game_over_rect = game_over_surface.get_rect(center=(surface.get_width()//2, 600 // 3))
        surface.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        self.l_score = 0
        self.r_score = 0
        time.sleep(2)
        pygame.quit()
        quit()
