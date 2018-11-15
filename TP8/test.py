from PIL.Image import *
import PIL.Image
import numpy
from AntClass import Direction
from threading import Thread, RLock

def instance_painting(x, y, name_image):
    painting = PIL.Image.new('RGB', (x, y), color=(255, 255, 255))
    painting.save(name_image)
    return painting

def luminance(affinity_color, color_pixel):
    lum_affinity = 0.2426*affinity_color[0]+0.7152*affinity_color[1]+0.0722*affinity_color[2]
    lum_pixel = 0.2426*color_pixel[0]+0.7152*color_pixel[1]+0.0722*color_pixel[2]
    return abs(lum_affinity-lum_pixel)

def location_ant_start(weight_painting, height_painting):
    pixel_start = (0, 0)
    # 0=top, 1=bot, 2=left, 3=right
    border = numpy.random.randint(0, 4)
    if border == 0:
        return Direction.BOT, numpy.random.randint(1, weight_painting-1), 0
    elif border == 1:
        return Direction.TOP, numpy.random.randint(1, weight_painting-1), height_painting - 1
    elif border == 2:
        return Direction.RIGHT, 0, numpy.random.randint(1, height_painting - 1)
    elif border == 3:
        return Direction.LEFT, weight_painting - 1, numpy.random.randint(1, height_painting-1)

def color_pixel_3x3(painting, location_pixel, color):
    (weight, height) = painting.size
    x_pixel = location_pixel[0]
    y_pixel = location_pixel[1]

    #Check if the pixel is on any border of the painting and define the loop's scope
    if x_pixel != 0 and x_pixel != weight-1 and y_pixel != 0 and y_pixel != height-1:
        x_loop = y_loop = (-1, 2)
    elif x_pixel == 0:
        if y_pixel == 0:
            x_loop = y_loop = (0, 2)
        elif y_pixel == height-1:
            x_loop = (0, 2); y_loop = (-1, 1)
        else:
            x_loop = (0, 2); y_loop = (-1, 2)
    elif x_pixel == weight-1:
        if y_pixel == 0:
            x_loop = (-1, 1); y_loop = (0, 2)
        elif y_pixel == height-1:
            x_loop = y_loop = (-1, 1)
        else:
            x_loop = (-1, 1); y_loop = (-1, 2)
    elif y_pixel == 0:
        x_loop = (-1, 2); y_loop = (0, 2)
    else:
        x_loop = (-1, 2); y_loop = (-1, 1)

    #color the pixels
    for x in range(x_loop[0], x_loop[1]):
        for y in range(y_loop[0], y_loop[1]):
            painting.putpixel((x_pixel + x, y_pixel + y), color)

def neighbour_pixel_location(painting_size, ant_location):
    ant_direction = ant_location[0]
    weight_painting = painting_size[0]
    height_painting = painting_size[1]
    ant_x = ant_location[1]
    ant_y = ant_location[2]

    if ant_direction.TOP:
        pixel_right_neighbour = (ant_x + 1) % weight_painting, ant_y
        pixel_left_neighbour = (ant_x - 1) % weight_painting, ant_y
        pixel_ahead_neighbour = ant_x, (ant_y - 1) % height_painting
    elif ant_direction.BOT:
        pixel_right_neighbour = (ant_x - 1) % weight_painting, ant_y
        pixel_left_neighbour = (ant_x + 1) % weight_painting, ant_y
        pixel_ahead_neighbour = ant_x, (ant_y + 1) % height_painting
    elif ant_direction.RIGHT:
        pixel_right_neighbour = ant_x, (ant_y + 1) % height_painting
        pixel_left_neighbour = ant_x, (ant_y - 1) % height_painting
        pixel_ahead_neighbour = (ant_x + 1) % weight_painting, ant_y
    elif ant_direction.LEFT:
        pixel_right_neighbour = ant_x, (ant_y - 1) % height_painting
        pixel_left_neighbour = ant_x, (ant_y + 1) % height_painting
        pixel_ahead_neighbour = (ant_x - 1) % weight_painting, ant_y

    return pixel_left_neighbour, pixel_right_neighbour, pixel_ahead_neighbour


def run_ant(painting, write_color, follow_color, prob_move, prob_follow_color, nb_step, lock):
    location_pixel = location_ant_start(painting.size[0], painting.size[1])
    print(location_pixel)
    with lock:
        color_pixel_3x3(plateau, (location_pixel[1], location_pixel[2]), write_color)


    #for i in range(nb_step):

    #    seuil = True

        #Déterminer si couleur d'attirance correspond au seuil

    #    if (seuil):
    #    else:
    #        direction = numpy.random.choice(numpy.arange(1, prob_move.count()), prob_move)

lock = RLock()
plateau=instance_painting(50,50,'plateau.png')
#run_ant(plateau, (255,0,0), (255,0,0), (0.3,0.3,0.3), 0.5, 1)
thread_1 = Thread(target=run_ant, args=(plateau, (255,0,0), (255,0,0), (0.3,0.3,0.3), 0.5, 1, lock,))
thread_2 = Thread(target=run_ant, args=(plateau, (0,255,0), (0,255,0), (0.3,0.3,0.3), 0.5, 1, lock,))
thread_3 = Thread(target=run_ant, args=(plateau, (0,0,255), (0,0,255), (0.3,0.3,0.3), 0.5, 1, lock,))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

Image.show(plateau)