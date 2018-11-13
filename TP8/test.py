from PIL.Image import *
import PIL.Image
import numpy
from threading import Thread

def instance_painting(x, y, name_image):
    painting = PIL.Image.new('RGB', (x, y), color = (255, 255, 255))
    painting.save(name_image)
    return painting

def luminance(affinity_color, color_pixel):
    lum_affinity= 0.2426*affinity_color[0]+0.7152*affinity_color[1]+0.0722*affinity_color[2]
    lum_pixel= 0.2426*color_pixel[0]+0.7152*color_pixel[1]+0.0722*color_pixel[2]
    return abs(lum_affinity-lum_pixel)

def location_pixel_start(weight_painting, height_painting):
    pixel_start = (0, 0)
    # 0=top, 1=bot, 2=left, 3=right
    border = numpy.random.randint(0, 4)
    if (border == 0):
        return (numpy.random.randint(0, weight_painting), 0)
    elif (border == 1):
        return (numpy.random.randint(0, weight_painting), height_painting - 1)
    elif (border == 2):
        return (0, numpy.random.randint(0, height_painting - 1))
    elif (border == 3):
        return (weight_painting - 1, numpy.random.randint(0, height_painting))


plateau=instance_painting(50,50,'plateau.png')

def del_rouge(i):
    (l, h) = i.size
    for y in range(h):
        for x in range(l):
            (rouge, vert, bleu) = i.getpixel((x, y))
            i.putpixel((x, y), (0, vert, bleu))


def run_ant(painting, write_color, follow_color, prob_move, prob_follow_color, nb_step):
    pixel_start = location_pixel_start(painting.size[0], painting.size[1])
    print(pixel_start)
    #for i in range(nb_step):
    #    seuil = True

        #Déterminer si couleur d'attirance correspond au seuil

    #    if (seuil):
    #    else:
    #        direction = numpy.random.choice(numpy.arange(1, prob_move.count()), prob_move)
run_ant(plateau, (255,0,0), (255,0,0), (0.3,0.3,0.3), 0.5, 1)