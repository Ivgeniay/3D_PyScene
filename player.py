import pygame
from input import KeyCode
from settings import *
import math

class Player:
    def __init__(self) -> None:
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self) -> (int, int):
        return self.x, self.y

    def movement(self, _input: KeyCode):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if _input == KeyCode.UP:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if _input == KeyCode.DOWN:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if _input == KeyCode.LEFT:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if _input == KeyCode.RIGHT:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a

        if _input == KeyCode.AR_RIGHT: self.angle += player_rot_speed
        if _input == KeyCode.AR_LEFT: self.angle -= player_rot_speed
