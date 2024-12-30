import pygame
import math
from random import randint
from map import world_map
from input import *
from settings import *
from  player import Player
from raycasting import ray_casting
from drawing import Drawing

pygame.init()

screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

input_sys = Input()
player = Player()
input_sys.subscribe(player.movement)
drawing = Drawing(screen)

isQuit: bool = False
def event_handler(_event: pygame.event):
    global isQuit
    #print(_event)
    if _event.type == pygame.QUIT:
        isQuit = True

    if _event.type == pygame.KEYDOWN:
        if _event.key == 100: input_sys.key_down(KeyCode.RIGHT)
        if _event.key == 1073741903: input_sys.key_down(KeyCode.AR_RIGHT)
        if _event.key == 97: input_sys.key_down(KeyCode.LEFT)
        if _event.key == 1073741904: input_sys.key_down(KeyCode.AR_LEFT)
        if _event.key == 1073741905 or _event.key == 115: input_sys.key_down(KeyCode.DOWN)
        if _event.key == 1073741906 or _event.key == 119: input_sys.key_down(KeyCode.UP)

    if _event.type == pygame.KEYUP:
        if _event.key == 100: input_sys.key_up(KeyCode.RIGHT)
        if _event.key == 1073741903: input_sys.key_up(KeyCode.AR_RIGHT)
        if _event.key == 97: input_sys.key_up(KeyCode.LEFT)
        if _event.key == 1073741904: input_sys.key_up(KeyCode.AR_LEFT)
        if _event.key == 1073741905 or _event.key == 115: input_sys.key_up(KeyCode.DOWN)
        if _event.key == 1073741906 or _event.key == 119: input_sys.key_up(KeyCode.UP)


def quit_handler():
    print("Program kek")

while not isQuit:
    for event in pygame.event.get():
        event_handler(event)
    input_sys.update()

    screen.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock=clock)

    pygame.display.flip()
    clock.tick(FPS)
    #clock.tick()

quit_handler()

