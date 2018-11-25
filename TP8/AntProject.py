from PIL.Image import *
import PIL.Image
import numpy
from AntClass import Direction, Turn
from threading import Thread, RLock, Barrier

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

    if ant_direction == Direction.TOP:
        pixel_right_neighbour = (ant_x + 2) % weight_painting, ant_y
        pixel_left_neighbour = (ant_x - 2) % weight_painting, ant_y
        pixel_ahead_neighbour = ant_x, (ant_y - 2) % height_painting
    elif ant_direction == Direction.BOT:
        pixel_right_neighbour = (ant_x - 2) % weight_painting, ant_y
        pixel_left_neighbour = (ant_x + 2) % weight_painting, ant_y
        pixel_ahead_neighbour = ant_x, (ant_y + 2) % height_painting
    elif ant_direction == Direction.RIGHT:
        pixel_right_neighbour = ant_x, (ant_y + 2) % height_painting
        pixel_left_neighbour = ant_x, (ant_y - 2) % height_painting
        pixel_ahead_neighbour = (ant_x + 2) % weight_painting, ant_y
    elif ant_direction == Direction.LEFT:
        pixel_right_neighbour = ant_x, (ant_y - 2) % height_painting
        pixel_left_neighbour = ant_x, (ant_y + 2) % height_painting
        pixel_ahead_neighbour = (ant_x - 2) % weight_painting, ant_y

    return pixel_left_neighbour, pixel_right_neighbour, pixel_ahead_neighbour


def compute_direction(current_direction, turn):
    if current_direction == Direction.TOP:
        if turn == Turn.AHEAD:
            return Direction.TOP
        elif turn == Turn.LEFT:
            return Direction.LEFT
        elif turn == Turn.RIGHT:
            return Direction.RIGHT
    elif current_direction == Direction.BOT:
        if turn == Turn.AHEAD:
            return Direction.BOT
        elif turn == Turn.LEFT:
            return Direction.RIGHT
        elif turn == Turn.RIGHT:
            return Direction.LEFT
    elif current_direction == Direction.RIGHT:
        if turn == Turn.AHEAD:
            return Direction.RIGHT
        elif turn == Turn.LEFT:
            return Direction.TOP
        elif turn == Turn.RIGHT:
            return Direction.BOT
    elif current_direction == Direction.LEFT:
        if turn == Turn.AHEAD:
            return Direction.LEFT
        elif turn == Turn.LEFT:
            return Direction.BOT
        elif turn == Turn.RIGHT:
            return Direction.TOP


def run_ant(painting, write_color, affinity_color, prob_move, prob_affinity_color, nb_step, lock):
    location_pixel = location_ant_start(painting.size[0], painting.size[1])

    for i in range(nb_step):
        barrier.wait()
        pixel_left, pixel_right, pixel_ahead = neighbour_pixel_location(painting.size, location_pixel)
        list_direction = [pixel_left, pixel_right, pixel_ahead]
        affinity_neighbour = [False, False, False]
        count_affinity = 0
        color_pixel_left = painting.getpixel(pixel_left)
        color_pixel_right = painting.getpixel(pixel_right)
        color_pixel_ahead = painting.getpixel(pixel_ahead)

        if(luminance(color_pixel_left, affinity_color)) < 40:
            affinity_neighbour[0] = True; count_affinity = count_affinity + 1
        if(luminance(color_pixel_right, affinity_color)) < 40:
            affinity_neighbour[1] = True; count_affinity = count_affinity + 1
        if(luminance(color_pixel_ahead, affinity_color)) < 40:
            affinity_neighbour[2] = True; count_affinity = count_affinity + 1

        new_prob_move = list(prob_move)
        if count_affinity == 3:
            new_prob_move = [1/3, 1/3, 1/3]
        elif count_affinity == 2:
            for b in range(len(affinity_neighbour)):
                if affinity_neighbour[b]:
                    new_prob_move[b] = prob_affinity_color/count_affinity
                else:
                    new_prob_move[b] = 1 - prob_affinity_color
        elif count_affinity == 1:
            for b in range(len(affinity_neighbour)):
                if affinity_neighbour[b]:
                    new_prob_move[b] = prob_affinity_color/count_affinity
                else:
                    new_prob_move[b] = (1 - prob_affinity_color)/2
        index = numpy.random.choice([0, 1, 2], p=new_prob_move)
        if index == 0:
            turn = Turn.LEFT
        elif index == 1:
            turn = Turn.RIGHT
        elif index == 2:
            turn = Turn.AHEAD
        location_pixel = (compute_direction(location_pixel[0], turn), list_direction[index][0], list_direction[index][1])
        with lock:
            color_pixel_3x3(plateau, (location_pixel[1], location_pixel[2]), write_color)


lock = RLock()
barrier = Barrier(3)
plateau=instance_painting(500,500,'plateau2.png')

thread_1 = Thread(target=run_ant, args=(plateau, (255,0,0), (0,0,255), (0.05,0.05,0.9), 0.8, 200000, lock,))
thread_2 = Thread(target=run_ant, args=(plateau, (0,255,0), (0,0,255), (0.01,0.01,0.98), 1, 200000, lock,))
thread_3 = Thread(target=run_ant, args=(plateau, (0,0,255), (0,0,255), (0.03,0.02,0.95), 0.4, 200000, lock,))


thread_1.start()
thread_2.start()
thread_3.start()


thread_1.join()
thread_2.join()
thread_3.join()

Image.show(plateau)
plateau.save("plateau.png", "png")
