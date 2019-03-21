'''
CS5001
Spring 2019
Hasti Gheibi Dehnashi
HW 5
'''

import turtle
turtle.hideturtle()

def main():
    ship_body = input("Do you want to draw the body? Y/N\n")
    if ship_body == "Y":
        draw_ship_body()
    else:
        print("You chose No")
        
    left_rocket = input("Do you want to draw the left rocket? Y/N\n")
    if left_rocket == "Y":
        draw_left_rocket()
    else:
        print("You chose No")

   

def draw_ship_body():
    turtle.penup()
    turtle.goto(0,175)
    turtle.pendown()
    turtle.goto(-50,100)
    turtle.goto(-50,-100)
    turtle.goto(50,-100)
    turtle.goto(50,100)
    turtle.goto(0,175)

def draw_left_rocket():
    turtle.penup()
    turtle.goto(-70,-50)
    turtle.pendown()
    turtle.goto(-40,-130)
    turtle.goto(-100,-130)
    turtle.goto(-70,-50)

def draw_right_rocket():
    turtle.penup()
    turtle.goto(70,-50)
    turtle.pendown()
    turtle.goto(40,-130)
    turtle.goto(100,-130)
    turtle.goto(70,-50)

def draw_left_flame():
    turtle.penup()
    turtle.goto(-100,-130)
    turtle.pendown()
    turtle.goto(-90,-150)
    turtle.goto(-80,-130)
    turtle.goto(-70,-160)
    turtle.goto(-60,-130)
    turtle.goto(-50,-150)
    turtle.goto(-40,-130)

def draw_right_flame():
    turtle.penup()
    turtle.goto(100,-130)
    turtle.pendown()
    turtle.goto(90,-150)
    turtle.goto(80,-130)
    turtle.goto(70,-160)
    turtle.goto(60,-130)
    turtle.goto(50,-150)
    turtle.goto(40,-130)

def draw_blanks(num_of_letters):
    num_of_letters += 1
    for i in range(num_of_letters):
        distance_between_blanks = int((20*i) + 10)
        length_of_blank = int((20*i))
        turtle.penup()
        turtle.goto(length_of_blank,-200)
        turtle.pendown()
        turtle.goto(distance_between_blanks,-200)

def write_letter(location, letter):
    turtle.penup()
    turtle.goto(location,-197)
    turtle.pendown()
    turtle.write(letter, align="center", font=("Arial", 12, "normal"))

#main()
#draw_ship_body()
#draw_left_rocket()
#draw_right_rocket()
#draw_left_flame()
#draw_right_flame()
draw_blanks(8)
write_letter(65, "N")
write_letter(85, "O")
