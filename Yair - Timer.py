import turtle
import time

Timer_turtle = turtle.clone()

stamp_pos = []
tumps = []



def Time():
    global Timer_turtle

    for m in range(1):
        for s in range(60):
            stump = Timer_turtle.write(str(m) + " " + str(s))
            tumps.append(stump)
            old_stamp = tumps.pop(0)
            timer_turtle.clearstump(old_stump)
            time.sleep(1)

Time()


       

turtle.mainloop()





