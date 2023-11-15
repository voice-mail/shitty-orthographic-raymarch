import numpy as np
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480), pygame.SCALED)
pixel_array = pygame.PixelArray(screen)
clock = pygame.time.Clock()
running = True

mapsize = [1000,1000,1000]

# Materials Loading
matcolors = [
    (0, 0, 0, 0), # 0 air
    (28, 28, 28, 255), # 1 Stone
    (78, 201, 65, 255) #2 Grass
]

# Player Controller Functions
ppos = [500, 500, 10]

# Map Functions
def mapgen_blank(x, y, z):
    map_array = np.zeros((x, y, z), dtype=np.uint8)
    return map_array

def mappreset_singlelayer(map_array):
    mapsize = map_array.shape
    for x in range(mapsize[0]):
        for y in range(mapsize[1]):
            for z in range(1):
                map_array[x][y][z] = 1
    return map_array

def mapstructure_testcubes(px, py, pz, l, w, h):
    for x in range(px, px + l):
        for y in range(py, py + w):
            for z in range(pz, pz + h):
                map_array[x][y][z] = 2
    px += 10
    py += 10
    pz += 10
    for x in range(px, px + l):
        for y in range(py, py + w):
            for z in range(pz, pz + h):
                map_array[x][y][z] = 2

                
map_array = mapgen_blank(1000, 1000, 1000)
map_array = mappreset_singlelayer(map_array)
mapstructure_testcubes(550, 550, 1, 10, 10, 10)



# Graphics Functions
def raymarch(x, y):
    # Calculate px, py once
    px = x + ppos[0] - 320
    py = y + ppos[1] - 240

    # Vectorized pz values
    pz_values = np.arange(ppos[2] + 480, ppos[2] - 520, -1)

    # Check bounds
    if 0 <= px < mapsize[0] and 0 <= py < mapsize[1]:
        # Get the segment of map_array that aligns with the ray
        segment = map_array[px, py, pz_values]

        # Find the first non-zero value
        nonzero_indices = np.nonzero(segment)[0]
        if nonzero_indices.size > 0:
            first_hit = nonzero_indices[0]
            return matcolors[segment[first_hit]]
    
    # Default color if no hit
    return (0, 0, 0, 0)


        

# Important Functions
def frame():
    for x in range(640):
        for y in range(480):
            pixel_array[x,y] = raymarch(x,y)
    pygame.display.flip()









# Mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frame()

    
# Exit

pygame.quit()
