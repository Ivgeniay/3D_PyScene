import pygame
from settings import *
from raycasting import ray_casting
from map import mini_map

class Drawing:

    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
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

    def draw_minimap(self, player):
        self.screen_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.screen_map, YELLOW, (int(map_x), int(map_y)), (map_x + WIDTH * math.cos(player.angle),
                                                     map_y + WIDTH * math.sin(player.angle)))
        pygame.draw.circle(self.screen_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.screen_map, GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.screen.blit(self.screen_map, MAP_POS)