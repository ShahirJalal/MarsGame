import time, random, math

###############
## VARIABLES ##
###############

WIDTH = 800 # window size
HEIGHT = 800

#PLAYER variables
PLAYER_NAME = "Shahir"
FRIEND1_NAME = "Aisyah"
FRIEND2_NAME = "Azrai"
current_room = 31 # start room = 31

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

#############
##   MAP   ##
#############

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT