from helpers import *
from deel_1_computerwetenschappen import *
from random import randint
from visual import sphere, arrow


BOX_SIZE=40
DISPLAY_HEIGHT=600
DISPLAY_WIDTH=800
ROOSTER_WIDTH = DISPLAY_WIDTH/BOX_SIZE
ROOSTER_HEIGHT = DISPLAY_HEIGHT/BOX_SIZE


def teken_doos(rx,ry, grootte, kleur):
    rx, ry, grootte = float(rx), float(ry), float(grootte)
    #rx en ry zijn coordinaten in het rooster en x en y in coordinatenstelsel

    (x,y) = rooster_naar_coord(grootte, (rx,ry))
    box_loc = vector(x, y, 0)

    doos = box(pos=box_loc, height=grootte-2, length=grootte-2)
    doos.color=kleur
    radius=2.0
    padding_right = curve( pos=[ vector(x + (radius/2 + grootte/2), y-grootte/2, 0 ), vector(x + (radius/2 + grootte/2), y+grootte/2, 0 ) ], color=color.black, radius=radius )
    padding_top =curve( pos=[ vector(x - grootte/2, y + (radius/2  + grootte/2), 0 ), vector(x + grootte/2, y + radius/2  + grootte/2, 0 ) ], color=color.black, radius=radius )

    return [doos, padding_right, padding_top]


def can_move_down(doos, bodem, water):
    doos_x, doos_y = coord_naar_rooster(BOX_SIZE, (doos.doos.pos.x, doos.doos.pos.y))
    bodem_hoogte = bodem[doos_x-1]
    if doos_y > 1 and doos_y > bodem_hoogte+1:
        return True
    return False


def can_move_right(doos, bodem, water):
    doos_x, doos_y = coord_naar_rooster(BOX_SIZE, (doos.doos.pos.x, doos.doos.pos.y))
    if doos_x < ROOSTER_WIDTH and doos_y > bodem[doos_x]:
        return True
    return False


def can_move_left(doos, bodem, water):
    doos_x, doos_y = coord_naar_rooster(BOX_SIZE, (doos.doos.pos.x, doos.doos.pos.y))
    if doos_x > 1 and doos_y > bodem[doos_x-2]:
        return True
    return False


class doos():

    def __init__(self, x, y, color):
        box = teken_doos(x,y, BOX_SIZE, color)
        self.doos = box[0]
        self.padding_r = box[1]
        self.padding_t = box[2]

    def move_right(self):
        if can_move_right(self, bodemhoogte, waterhoogte):
            self.doos.pos += vector(BOX_SIZE, 0, 0)
            self.padding_r.pos[0] += vector(BOX_SIZE, 0, 0)
            self.padding_r.pos[1] += vector(BOX_SIZE, 0, 0)
            self.padding_t.pos[0] += vector(BOX_SIZE, 0, 0)
            self.padding_t.pos[1] += vector(BOX_SIZE, 0, 0)

    def move_left(self):
        if can_move_left(self, bodemhoogte, waterhoogte):
            self.doos.pos += vector(-BOX_SIZE, 0, 0)
            self.padding_r.pos[0] += vector(-BOX_SIZE, 0, 0)
            self.padding_r.pos[1] += vector(-BOX_SIZE, 0, 0)
            self.padding_t.pos[0] += vector(-BOX_SIZE, 0, 0)
            self.padding_t.pos[1] += vector(-BOX_SIZE, 0, 0)

    def move_down(self):
        if can_move_down(self, bodemhoogte, waterhoogte):
            self.doos.pos += vector(0, -BOX_SIZE, 0)
            self.padding_r.pos[0] += vector(0, -BOX_SIZE, 0)
            self.padding_r.pos[1] += vector(0, -BOX_SIZE, 0)
            self.padding_t.pos[0] += vector(0, -BOX_SIZE, 0)
            self.padding_t.pos[1] += vector(0, -BOX_SIZE, 0)

    def drop(self, bodem, water):
        doos_x, doos_y = coord_naar_rooster(BOX_SIZE, (self.doos.pos.x, self.doos.pos.y))
        bodemhoogte = bodem[doos_x - 1]
        x_coord, y_coord = rooster_naar_coord(BOX_SIZE, (doos_x, bodemhoogte + 1))
        radius=2.0

        self.doos.pos = vector(x_coord, y_coord, 0)
        self.padding_r.pos[0] = vector(x_coord + (radius / 2 + BOX_SIZE / 2), y_coord - BOX_SIZE / 2, 0)
        self.padding_r.pos[1] = vector(x_coord + (radius / 2 + BOX_SIZE / 2), y_coord + BOX_SIZE / 2, 0)
        self.padding_t.pos[0] = vector(x_coord - BOX_SIZE / 2, y_coord + (radius/2 + BOX_SIZE / 2), 0)
        self.padding_t.pos[1] = vector(x_coord + BOX_SIZE / 2, y_coord + (radius/2 + BOX_SIZE / 2), 0)


def generate_doos():
    x = randint(1, ROOSTER_WIDTH-1)
    type = randint(0,100)

    if type < 50:
        return ("upper", doos(x,ROOSTER_HEIGHT, color.green))

    elif type < 80:
        return ("water", doos(x, ROOSTER_HEIGHT, color.blue))

    elif type < 90:
        return ("downer", doos(x, ROOSTER_HEIGHT, color.yellow))

    else:
        return ("fire", doos(x, ROOSTER_HEIGHT, color.red))

venster = open_display(height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH)

bodemhoogte=[0]*ROOSTER_WIDTH
waterhoogte=[0]*ROOSTER_WIDTH

new_box = generate_doos()
type = new_box[0]
falling = new_box[1]

counter=0
while True:
    rate(30)
    counter+=1
    if venster.kb.keys:
        toets = venster.kb.getkey()

        if toets == "right":
            falling.move_right()

        elif toets == "left":
            falling.move_left()

        elif toets == "down":
            falling.drop(bodemhoogte, waterhoogte)

    if counter==8:
        if can_move_down(falling, bodemhoogte, waterhoogte):
            falling.move_down()

        else:

            if type == "upper":
                x,y = coord_naar_rooster(BOX_SIZE, (falling.doos.pos.x, falling.doos.pos.y))
                bodemhoogte[x-1] += 1
                print(bodemhoogte)

            if type == "water":
                x, y = coord_naar_rooster(BOX_SIZE, (falling.doos.pos.x, falling.doos.pos.y))
                waterhoogte[x - 1] += 1
                print(waterhoogte)

            new_box = generate_doos()
            type = new_box[0]
            falling = new_box[1]

        counter=0


