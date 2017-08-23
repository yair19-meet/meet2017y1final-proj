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
truck1=truck1.stamp()
stamp_list1.append(truck1)
#truck2
turtle.register_shape("truck2.gif")
truck2=turtle.clone()
truck2.shape("truck2.gif")
truck2.goto(-350,-220)
truck2=truck2.stamp()
stamp_list2.append(truck2)
turtle.tracer(1,0)



turtle.mainloop()

