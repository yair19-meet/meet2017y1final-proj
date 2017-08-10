def crash():
    if pos_1 == pos_2:
        truck1.goto(pos_1[0]+square_size*10, pos_2[1])
        truck2.goto(pos_2[0]-square_size*10, pos_2[1])
