import turtle
import random #It will be useful for later
import time



SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X,SIZE_Y)
TIME_STEP = 1500
RIGHT_EDGE=400
LEFT_EDGE=-400
UP_EDGE=250
DOWN_EDGE=-250

turtle.bgcolor ('gray')

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

SQUARE_SIZE = 10
#healthy_food
healthy_food = turtle.clone()
turtle.register_shape("apple.gif") #add apple picture
healthy_food.shape("apple.gif")


pos_list_1 = []
pos_list_2 = []
#Initialize lists
unhealthy_food_pos = []
healthy_food_pos = []
unhealthy_food_stamps = []
healthy_food_stamps = []


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR="space"
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
    global RIGHT_EDGE
    global LEFT_EDGE
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

    if x_pos_1 >= RIGHT_EDGE:
        truck1.goto(LEFT_EDGE + SQUARE_SIZE, y_pos_1)
    if x_pos_1 <= LEFT_EDGE:
        truck1.goto(RIGHT_EDGE - SQUARE_SIZE, y_pos_1)
    if y_pos_1 >= UP_EDGE:
        truck1.goto(x_pos_1, DOWN_EDGE + SQUARE_SIZE)
    if y_pos_1 <= DOWN_EDGE:
        truck1.goto(x_pos_1, UP_EDGE - SQUARE_SIZE )
        


    my_pos_1 = truck1.pos()
    pos_list_1.append(my_pos_1)
    new_stamp=truck1.stamp()
    stamp_list1.append(new_stamp)
    old_stamp=stamp_list1.pop(0)
    truck1.clearstamp(old_stamp)
    pos_list_1.pop(0)
    print(truck1.pos())
    if truck1.pos() in healthy_food_pos:
        print("Hi")
        food1_ind = healthy_food_pos.index(truck1.pos()) #what does this do?
        healthy_food.clearstamp(healthy_food_stamps[food1_ind]) #remove eaten food stamp
        healthy_food_pos.pop(food1_ind) #remove eaten food position
        healthy_food_stamps.pop(food1_ind) #remove eaten food stamp
        print("you have eaten the healthy food!")
        counter1()
    if truck1.pos() in unhealthy_food_pos:
        print("Hi")
        food3_ind = unhealthy_food_pos.index(truck1.pos()) #what does this do?
        unhealthy_food.clearstamp(unhealthy_food_stamps[food3_ind]) #remove eaten food stamp
        unhealthy_food_pos.pop(food3_ind) #remove eaten food position
        unhealthy_food_stamps.pop(food3_ind) #remove eaten food stamp
        print("you have eaten the unhealthy food!")
        counter3()


    #turtle.ontimer(move_truck1,TIME_STEP)
    


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

    if x_pos_2 >= RIGHT_EDGE:
        truck2.goto(LEFT_EDGE + SQUARE_SIZE, y_pos_2)
    if x_pos_2 <= LEFT_EDGE:
        truck2.goto(RIGHT_EDGE - SQUARE_SIZE, y_pos_2)
    if y_pos_2 >= UP_EDGE:
        truck2.goto(x_pos_2, DOWN_EDGE + SQUARE_SIZE)
    if y_pos_2 <= DOWN_EDGE:
        truck2.goto(x_pos_2, UP_EDGE - SQUARE_SIZE )
        



    my_pos_2 = truck2.pos()
    pos_list_2.append(my_pos_2)
    new_stamp2=truck2.stamp()
    stamp_list2.append(new_stamp2)
    old_stamp=stamp_list2.pop(0)
    truck2.clearstamp(old_stamp)
    pos_list_2.pop(0)

    print(truck2.pos())
    if truck2.pos() in healthy_food_pos:
        print("Hi")
        food2_ind = healthy_food_pos.index(truck2.pos()) #what does this do?
        healthy_food.clearstamp(healthy_food_stamps[food2_ind]) #remove eaten food stamp
        healthy_food_pos.pop(food2_ind) #remove eaten food position
        healthy_food_stamps.pop(food2_ind) #remove eaten food stamp
        print("you have eaten the healthy food!")
        counter2()
       
                
    if truck2.pos() in unhealthy_food_pos:
        print("Hi")
        food4_ind = unhealthy_food_pos.index(truck2.pos()) #what does this do?
        unhealthy_food.clearstamp(unhealthy_food_stamps[food4_ind]) #remove eaten food stamp
        unhealthy_food_pos.pop(food4_ind) #remove eaten food position
        unhealthy_food_stamps.pop(food4_ind) #remove eaten food stamp
        print("you have eaten the unhealthy food!")
        counter4()
    
    #turtle.ontimer(move_truck2,TIME_STEP)


score_turtle2=turtle.clone()
score2=0
                
def counter2():
            global score2
            score2+=1
            score_turtle2.clear()
            score_turtle2.goto(-390,-240)
            score_turtle2.write("SCORE: " +str(score2))
            
            

score_turtle1=turtle.clone()
score1=0
def counter1():
            global score1
            score1+=1
            score_turtle1.clear()
            score_turtle1.goto(330,230)
            score_turtle1.write("SCORE: " +str(score1))


def counter3():
            global score1
            score1-=2
            score_turtle1.clear()
            score_turtle1.goto(330,230)
            score_turtle1.write("SCORE: " +str(score1),font=("Arial",8,"normal"))


def counter4():
            global score2
            score2-=2
            score_turtle2.clear()
            score_turtle2.goto(-390,-240)
            score_turtle2.write("SCORE: " +str(score2))
    
turtle.hideturtle()





#healthy_food_pos = [(100,100)]
#healthy_food_stamps = []

for this_healthy_food_pos in healthy_food_pos:
    healthy_food.goto(this_healthy_food_pos)
    healthyfood1 = healthy_food.stamp()
    healthy_food_stamps.append(healthyfood1)


unhealthy_food = turtle.clone()
turtle.register_shape("hot-dog-animated-gif-12.gif") #add chips picture 
unhealthy_food.shape("hot-dog-animated-gif-12.gif")


#unhealthy_food_pos = [(-100,100)]
#unhealthy_food_stamps = []

for this_unhealthy_food_pos in unhealthy_food_pos:
    unhealthy_food.goto(this_unhealthy_food_pos)
    unhealthyfood1 = unhealthy_food.stamp()
    unhealthy_food_stamps.append(unhealthyfood1)



def make_healthyfood():
    #the screen positions go from -SIZE/2 to +SIZE/2
    #we need to make food pieces only appear on game squares
    #so we cut up the game board into multiples of SQUARE_SIZE
    min_x = -int(SIZE_X/2/SQUARE_SIZE) + 1
    max_x = int(SIZE_X/2/SQUARE_SIZE) - 1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE) + 1
    max_y = int(SIZE_Y/2/SQUARE_SIZE) - 1

    #pick a position that is a random multiple of SQUARE_SIZE
    healthy_food_x = random.randint(min_x, max_x) * SQUARE_SIZE
    healthy_food_y = random.randint(min_y, max_y) * SQUARE_SIZE
    

    healthy_food.goto(healthy_food_x, healthy_food_y)
    healthy_food_pos1 = (healthy_food_x, healthy_food_y)
    healthy_food_pos.append(healthy_food_pos1)
    healthy_food_stamp1 = healthy_food.stamp()
    healthy_food_stamps.append(healthy_food_stamp1)

    turtle.ontimer(make_healthyfood,1800)

    

def make_unhealthyfood():
    min_x1 = -int(SIZE_X/2/SQUARE_SIZE) + 1
    max_x1 = int(SIZE_X/2/SQUARE_SIZE) - 1
    min_y1 = -int(SIZE_Y/2/SQUARE_SIZE) + 1
    max_y1 = int(SIZE_Y/2/SQUARE_SIZE) - 1

    
    unhealthy_food_x = random.randint(min_x1, max_x1) * SQUARE_SIZE
    unhealthy_food_y = random.randint(min_y1, max_y1) * SQUARE_SIZE
    

    unhealthy_food.goto(unhealthy_food_x, unhealthy_food_y)
    unhealthy_food_pos1 = (unhealthy_food_x, unhealthy_food_y)
    unhealthy_food_pos.append (unhealthy_food_pos1)
    unhealthy_food_stamp1 = unhealthy_food.stamp()
    unhealthy_food_stamps.append(unhealthy_food_stamp1)

    turtle.ontimer(make_unhealthyfood,4000)
    

make_healthyfood()
make_unhealthyfood()


time_turtle=turtle.clone()
winner_turtle = turtle.clone()

s = 60
def timer():
    global s
    time_turtle.clear()
    time_turtle.goto(-390,235)
    time_turtle.write(str(s))
    s-=1
    turtle.ontimer(timer,1000)
    if s==0 and score1>score2:
        
        winner_turtle.pencolor('yellow')
        winner_turtle.write("congratulations Truck1! You've collected the most healthy food!", align="center", font=("Arial",20,"normal"))
        
    elif s==0 and score2>score1:
        winner_turtle.pencolor('green')
        winner_turtle.write("congratulations Truck2! You've collected the most healthy food!", align="center", font=("Arial",20,"normal"))
        
        
        
        
    
timer()


##def timer():
##    for m in range (1):
##        for s in range (60):
##            time_turtle.clear()
##            time_turtle.write(str(m) + ": " + str(s))
##
##            #time_turtle.sleep(1)
##time()
turtle.mainloop()



    
    
    
    







