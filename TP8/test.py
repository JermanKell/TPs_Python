from PIL.Image import *
import PIL.Image
import numpy
from threading import Thread

def instance_painting(x, y, name_image):
    painting = PIL.Image.new('RGB', (x, y), color=(255, 255, 255))
    painting.save(name_image)
    return painting

def luminance(affinity_color, color_pixel):
    lum_affinity = 0.2426*affinity_color[0]+0.7152*affinity_color[1]+0.0722*affinity_color[2]
    lum_pixel = 0.2426*color_pixel[0]+0.7152*color_pixel[1]+0.0722*color_pixel[2]
    return abs(lum_affinity-lum_pixel)

def location_pixel_start(weight_painting, height_painting):
    pixel_start = (0, 0)
    # 0=top, 1=bot, 2=left, 3=right
    border = numpy.random.randint(0, 4)
    if border == 0:
        return numpy.random.randint(0, weight_painting), 0
    elif border == 1:
        return numpy.random.randint(0, weight_painting), height_painting - 1
    elif border == 2:
        return 0, numpy.random.randint(0, height_painting - 1)
    elif border == 3:
        return weight_painting - 1, numpy.random.randint(0, height_painting)

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
            print(x_pixel+x, y_pixel+y)
            painting.putpixel((x_pixel + x, y_pixel + y), color)


def run_ant(painting, write_color, follow_color, prob_move, prob_follow_color, nb_step):
    pixel_start = location_pixel_start(painting.size[0], painting.size[1])
    #print(pixel_start)
    #for i in range(nb_step):
    #    seuil = True

        #Déterminer si couleur d'attirance correspond au seuil

    #    if (seuil):
    #    else:
    #        direction = numpy.random.choice(numpy.arange(1, prob_move.count()), prob_move)

plateau=instance_painting(50,50,'plateau.png')
run_ant(plateau, (255,0,0), (255,0,0), (0.3,0.3,0.3), 0.5, 1)
location = location_pixel_start(50, 50)
color_pixel_3x3(plateau, location, (230, 120, 0))
Image.show(plateau)
