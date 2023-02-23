import turtle as tt
import random as rd
import time
from math import sqrt

def createScreen(LENGTH, WIDTH, backGround = "forest green"):
    screen = tt.Screen()
    screen.title("Turtle Racing- Beta 1.0.0")
    screen.setup(LENGTH, WIDTH)
    screen.bgcolor(backGround)

def createRoad(LENGTH):
    s = LENGTH/12
    road = tt.Turtle()
    road.speed(0)
    road.fillcolor("sienna")
    road.pen(shown= False)

    road.begin_fill()
    road.up()
    road.setpos(-5*s, 2*s)
    road.down()
    road.fd(2*s)
    road.right(90)
    road.fd(2*s)
    road.right(90)
    road.fd(s/2)
    road.left(90)
    road.fd(s)
    road.left(90)
    road.fd((3/2)*s)
    road.left(90)
    road.fd(3*s)
    road.right(90)
    road.fd(3*s)
    road.right(90)
    road.fd(s)
    road.left(90)
    road.fd(s)
    road.left(90)
    road.fd(s/2)
    road.right(90)
    road.fd(s)

    road.left(90)
    road.fd(s)
    road.right(90)
    road.fd(2*s)
    road.right(90)
    road.fd(s*3/2)
    road.right(90)
    road.fd(2*s)
    road.left(90)
    road.fd(s/2)
    road.right(90)
    road.fd(s)
    road.left(90)
    road.fd(s/2)
    
    road.right(90)
    road.fd(s)
    road.left(90)
    road.fd(s)
    road.left(90)
    road.fd(s*2)
    road.left(90)
    road.fd(s/2)
    road.right(90)
    road.fd(2*s)
    road.right(90)
    road.fd(s*3/2)
    road.right(90)
    road.fd(5*s)
    road.right(90)
    road.fd(3*s)
    road.left(90)
    road.fd(s)
    road.left(90)
    road.fd(3*s)
    road.right(90)
    road.fd(s*7/2)
    road.right(90)
    road.fd(2*s)
    road.left(90)
    road.fd(s/2)
    road.right(90)
    road.fd(2*s)
    road.end_fill()

def drawnTree_1(LENGTH, x, y, t1 = "brown", t2 = "green"): 
    s = LENGTH/(12*6)
    tree = tt.Turtle()
    tree.speed(0)
    tree.pen(shown= False)
    tree.up()
    tree.setpos(x, y)
    tree.down()

    tree.fillcolor(t1)
    tree.begin_fill()
    tree.left(90)
    tree.fd(3*s)
    tree.right(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.right(45)
    tree.fd(s*sqrt(2))
    tree.right(45)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.end_fill()

    tree.right(90)
    tree.fd(2*s)

    tree.fillcolor(t2)
    tree.begin_fill()
    tree.left(90)
    tree.fd(2*s)
    tree.right(90)
    for i in range(4):
        tree.fd(s)
        tree.right(90)
        tree.fd(s)
        tree.left(90)
    tree.right(90)
    for i in range(3):
        tree.fd(s)
        tree.right(90)
        tree.fd(s)
        tree.left(90)
    tree.right(180)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)

    

    tree.right(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.end_fill()

def drawnTree_2(LENGTH, x, y, t1 = "brown", t2 = "green"):
    s = LENGTH/(12*6*2)
    tree = tt.Turtle()
    tree.speed(0)
    tree.pen(shown= False)
    tree.up()
    tree.setpos(x, y)
    tree.down()

    tree.fillcolor(t2)
    tree.begin_fill()
    tree.left(180)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s)
    tree.left(90)
    tree.fd(s*2)
    tree.right(90)
    for i in range(5):
        tree.fd(s)
        tree.right(90)
        tree.fd(s)
        tree.left(90)
    tree.right(90)
    tree.fd(2*s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(2*s)
    tree.right(90)
    for i in range (4):
        tree.fd(s)
        tree.left(90)
        tree.fd(s)
        tree.right(90)
    for i in range(4):
        tree.fd(s)
        tree.right(90)
        tree.fd(s)
        tree.left(90)
    tree.right(90)
    tree.fd(4*s)
    tree.end_fill()

    tree.fillcolor(t1)
    tree.begin_fill()
    tree.right(90)
    tree.fd(2*s)
    tree.left(90)
    tree.fd(s)
    tree.right(45)
    tree.fd(s*sqrt(2))
    tree.right(45)
    tree.fd(s)
    tree.right(90+45)
    tree.fd(s*sqrt(2))
    tree.left(45)
    tree.fd(s)
    tree.left(90)
    tree.fd(s)
    tree.right(90)
    tree.fd(s*2)
    tree.right(90)
    tree.fd(2*s)
    tree.left(90)
    tree.fd(2*s)
    tree.left(45)
    tree.fd(s*sqrt(2))
    tree.right(90+45)
    tree.fd(s)
    tree.right(45)
    tree.fd(s*sqrt(2))
    tree.right(45)
    tree.fd(2*s)
    tree.left(90)
    tree.fd(s*4)
    tree.right(90)
    tree.fd(2*s)
    tree.right(90)
    tree.fd(s*4)
    tree.end_fill()

def drawnGrass(LENGTH, x, y):
    s = LENGTH/(400)
    num = rd.randrange(3, 6)
    someThing = rd.randint(1,20)
    grassColor = ''
    if someThing == 10:
        grassColor = 'brown'
    elif someThing < 10:
        grassColor = 'olive'
    else:
        grassColor = 'spring green'

    grass = tt.Turtle()
    grass.pen(shown= False)
    grass.speed(0)
    grass.up()
    grass.setpos(x, y)
    grass.down()
    grass.left(90)
    grass.fillcolor(grassColor)
    grass.begin_fill()
    for i in range (num):
        d = rd.randrange(3*s, 8*s)
        grass.fd(d)
        grass.right(90)
        grass.fd(s)
        grass.right(90)
        grass.fd(d)
        grass.left(180)
    grass.left(90)
    # grass.fd(s*(num))
    grass.end_fill()

def createLine(LENGTH, WIDTH):
    s = WIDTH/24
    line = tt.Turtle()
    line.pen(shown = False)
    line.speed(0)
    for k in range(2):
        line.up()
        if k==1:
            line.setpos(-LENGTH/2, WIDTH/2 - WIDTH/24)
            line.right(90)
        else:
            line.setpos(-LENGTH/2, -WIDTH/2 + WIDTH/24)
        line.down()
        line.left(90)

        for i in range(48):
            if i%2 == 0:
                line.fillcolor("white")
            else:
                line.fillcolor("black")
            line.begin_fill()

            for sqr in range(4):
                line.fd(s)
                if sqr == 3:
                    line.back(s)
                line.right(90)
            
            line.end_fill()

def fillBoomRadom(LENGTH, WIDTH, boomList, numOfBoom = 50):
    r = LENGTH/2400
    s = LENGTH/36
    for i in range(numOfBoom):
        x = rd.randrange(-LENGTH/2 , LENGTH/2)
        y = rd.randrange(-WIDTH/2 + WIDTH/12, WIDTH/2 - WIDTH/12)

        boom = tt.Turtle()
        boom.speed(0)
        boom.x = x
        boom.y = y
        boom.up()
        boom.setpos(x,y)
        boom.shape("circle")
        boom.shapesize(r)
        boom.color("red")
        boom.down()
        boomList.append(boom)
    hide = tt.Turtle()
    hide.pen(shown= False)
    hide.write("  HIDE BOOM\nGOOD LUCK!!!", False, align= "center", font=('Arial', '50', 'normal'))
    time.sleep(4)
    hide.undo()

    for boom in boomList:
        boom.color("forest green")
