import numpy as np
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480), pygame.SCALED)
pixel_array = pygame.PixelArray(screen)
clock = pygame.time.Clock()
running = True


# Configuration Variables
mapsize = [1000,1000,1000]
maxraydistance = 600
cameraoffset = 50

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
mapstructure_testcubes(200, 400, 1, 10, 20, 1)
mapstructure_testcubes(240, 440, 1, 20, 10, 2)
mapstructure_testcubes(280, 480, 1, 10, 10, 3)

# Graphics Functions
def raymarch():
    for x in range(640):
        for y in range(480):
            cpos = [ppos[0] - 320 + x, ppos[1] + 240 - y + cameraoffset, ppos[2] + cameraoffset ]  # Adjusted coordinate calculation
            for i in range(maxraydistance):
                cpos[1] -= 1
                cpos[2] -= 1
                if 0 <= cpos[0] < mapsize[0] and 0 <= cpos[1] < mapsize[1] and 0 <= cpos[2] < mapsize[2]:
                    if map_array[cpos[0]][cpos[1]][cpos[2]] != 0:
                        pixel_array[x,y] = matcolors[map_array[cpos[0]][cpos[1]][cpos[2]]]
                        #print(cpos)
                        break
            else:
                continue
        
        pygame.display.flip()  # Update display after all pixels have been processed



        

# Important Functions
def frame():
    raymarch()
    









# Mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frame()

    
# Exit

pygame.quit()
