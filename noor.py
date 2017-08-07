import turtle
import random #It will be useful for later

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y) #it's the turtle window size

turtle.penup()

SQUARE_SIZE = 20

turtle.bgcolor('blue')

#Initialize lists
unhealthy_food_pos = []
healthy_food_pos = []
unhealthy_food_stamps = []
healthy_food_stamps = []



healthy_food = turtle.clone()
turtle.register_shape("frygif.gif") #add apple picture
healthy_food.shape("frygif.gif")


#unhealthy_food = turtle.clone()
#unhealthy_food.register_shape("giphy.gif") #add chips picture 
#unhealthy_food.shape("giphy.gif")

#turtle.shape(".....")

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

def make_unhealthyfood():
    min_x1 = -int(SIZE_X/2/SQUARE_SIZE) + 3
    max_x1 = int(SIZE_X/2/SQUARE_SIZE) - 3
    min_y1 = -int(SIZE_Y/2/SQUARE_SIZE) + 3
    max_y1 = int(SIZE_Y/2/SQUARE_SIZE) - 3

    
    unhealthy_food_x = random.randint(min_x1, max_x1) * SQUARE_SIZE
    unhealthy_food_y = random.randint(min_y1, max_y1) * SQUARE_SIZE
    

    unhealthy_food.goto(unhealthy_food_x, unhealthy_food_y)
    unhealthy_food_pos1 = (unhealthy_food_x, unhealthy_food_y)
    unhealthy_food_pos.append (unhealthy_food_pos1)
    unhealthy_food_stamp1 = unhealthy_food.stamp()
    unhealthy_food_stamps.append(unhealthy_food_stamp1)

