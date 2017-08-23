import turtle
import random
SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X,SIZE_Y)
stamp_list1=[]
stamp_list2=[]
pos_list_1=[]
pos_list_2=[]
turtle.hideturtle()
turtle.penup()
#truck1
turtle.register_shape("truck1.gif")
truck1=turtle.clone()
truck1.shape("truck1.gif")
truck1.goto(350,220)
first_truck=truck1.stamp()
stamp_list1.append(first_truck)
#truck2
turtle.register_shape("truck2.gif")
truck2=turtle.clone()
truck2.shape("truck2.gif")
truck2.goto(-350,-220)
second_truck=truck2.stamp()
stamp_list2.append(second_truck)
turtle.tracer(1,0)

SQUARE_SIZE = 20


pos_list_1 = []
pos_list_2 = []

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

W = "w"
A = "a"
S = "s"
D = "d"


direction_1 = DOWN
direction_2 = DOWN

def up_1():
    global direction_1
    direction_1 = UP
    move_truck1()
    

def down_1():
    global direction_1
    direction_1 = DOWN
    move_truck1()
    

def left_1():
    global direction_1
    direction_1 = LEFT
    move_truck1()

def right_1():
    global direction_1
    direction_1 = RIGHT
    move_truck1()


turtle.onkeypress(up_1, UP_ARROW)
turtle.onkeypress(down_1, DOWN_ARROW)
turtle.onkeypress(left_1,LEFT_ARROW)    
turtle.onkeypress(right_1,RIGHT_ARROW)
turtle.listen()
def up_2():
    global direction_2
    direction_2 = UP
    move_truck2()

def down_2():
    global direction_2
    direction_2 = DOWN
    move_truck2()

def left_2():
    global direction_2
    direction_2 = LEFT
    move_truck2()

def right_2():
    global direction_2
    direction_2 = RIGHT
    move_truck2()


turtle.onkeypress(up_2, W)
turtle.onkeypress(down_2, S)
turtle.onkeypress(left_2, A)    
turtle.onkeypress(right_2, D)
turtle.listen()

def move_truck1():
    global pos_list_1
    my_pos_1 = truck1.pos()
    x_pos_1 = my_pos_1[0]
    y_pos_1 = my_pos_1[1]

    

    if direction_1 == RIGHT:
        truck1.goto(x_pos_1 + SQUARE_SIZE, y_pos_1)
        print("You moved right!")
    elif direction_1 == LEFT:
        truck1.goto(x_pos_1 - SQUARE_SIZE, y_pos_1)
        print('You moved left!')
    elif direction_1 == UP:
        truck1.goto(x_pos_1, y_pos_1 + SQUARE_SIZE)
        print("You moved up!")
    elif direction_1 == DOWN:
        truck1.goto(x_pos_1, y_pos_1- SQUARE_SIZE)
        print("You moved Down!")

    my_pos_1 = truck1.pos()
    pos_list_1.append(my_pos_1)
    new_stamp=truck1.stamp()
    stamp_list1.append(new_stamp)
    old_stamp=stamp_list1.pop(0)
    truck1.clearstamp(old_stamp)
    pos_list_1.pop(0)


def move_truck2():
    global pos_list_2
    my_pos_2 = truck2.pos()
    x_pos_2 = my_pos_2[0]
    y_pos_2 = my_pos_2[1]

    

    if direction_2 == RIGHT:
        truck2.goto(x_pos_2 + SQUARE_SIZE, y_pos_2)
        print("You moved right!")
    elif direction_2 == LEFT:
        truck2.goto(x_pos_2 - SQUARE_SIZE, y_pos_2)
        print('You moved left!')
    elif direction_2 == UP:
        truck2.goto(x_pos_2, y_pos_2 + SQUARE_SIZE)
        print("You moved up!")
    elif direction_2 == DOWN:
        truck2.goto(x_pos_2, y_pos_2 - SQUARE_SIZE)
        print("You moved Down!")

    my_pos_2 = truck2.pos()
    pos_list_2.append(my_pos_2)
    new_stamp2=truck2.stamp()
    stamp_list2.append(new_stamp2)
    old_stamp=stamp_list2.pop(0)
    truck2.clearstamp(old_stamp)
    pos_list_2.pop(0)

<<<<<<< HEAD
score_turtle1=turtle.clone()
score1=0
def counter1():
    global score1
    score+=1
    score_turtle1.clear()
    score_turtle1.write(score)
    score_turtle1.goto(390,240)
    
score_turtle2=0
score2=0
def counter2():
    global score2
    score+=1
    score_turtle2.clear()
    score_turtle2.write(score)
    score_turtle2.goto(-390,-240)
    

    
=======
    turtle.ontimer(move_truck1,TIME_STEP)
    move_truck1()





turtle.mainloop()

