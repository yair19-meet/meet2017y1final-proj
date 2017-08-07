import turtle

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

W = "Up"
A = "Left"
S = "Down"
D = "Right"


direction_1 = UP
direction_2 = UP

def up_1():
    global direction
    direction = UP

def down_1():
    global direction
    direction = DOWN

def left_1():
    global direction
    direction = LEFT

def right_1():
    global direction
    direction = RIGHT


turtle.onkeypress(up_1, UP_ARROW)
turtle.onkeypress(down_1, DOWN_ARROW)
turtle.onkeypress(left_1,LEFT_ARROW)    
turtle.onkeypress(right_1,RIGHT_ARROW)

def up_2():
    global direction
    direction = UP

def down_2():
    global direction
    direction = DOWN

def left_2():
    global direction
    direction = LEFT

def right_2():
    global direction
    direction = RIGHT


turtle.onkeypress(up_2, W)
turtle.onkeypress(down_2, S)
turtle.onkeypress(left_2, A)    
turtle.onkeypress(right_2, D)


def move_truck1():
    global pos_list_1
    my_pos_1 = truck1.pos()
    x_pos_1 = my_pos_1[0]
    y_pos_1 = my_pos_1[1]

    new_pos_1 = truck1.pos()
    new_x_pos_1 = new_pos_1[0]
    new_y_pos_1 = new_pos_1[1]

    if direction_1 == RIGHT:
        track1.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction_1 == LEFT:
        track1.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left!')
    elif direction_1 == UP:
        track1.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction_1 == DOWN:
        track1.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved Down!")

    my_pos_1 = truck1.pos()
    pos_list_1.append(my_pos_1)
    


def move_truck2():
    global pos_list_2
    my_pos_2 = truck2.pos()
    x_pos_2 = my_pos_2[0]
    y_pos_2 = my_pos_2[1]

    new_pos_2 = truck2.pos()
    new_x_pos_2 = new_pos_2[0]
    new_y_pos_2 = new_pos_2[1]

    if direction_2 == RIGHT:
        track1.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction_2 == LEFT:
        track1.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left!')
    elif direction_2 == UP:
        track1.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction_2 == DOWN:
        track1.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved Down!")

        my_pos_2 = truck2.pos()
    pos_list_2.append(my_pos_2)


def move_trucks():
    move_truck1()
    move_truck2()


move_trucks()


turtle.mainloop()


  
