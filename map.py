from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.....W....W',
    'WWW.....WW.W',
    'W...WWWW...W',
    'WWW........W',
    'WWWWWW.....W',
    'W.......WWWW',
    'WWWWWWWWWWWW',
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
