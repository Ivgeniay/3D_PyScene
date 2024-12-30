import pygame
from settings import *
from raycasting import ray_casting

class Drawing:

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, pl_pos: (int, int), pl_angle: float):
        ray_casting(self.screen, pl_pos, pl_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, WHITE)
        self.screen.blit(render, FPS_POS)