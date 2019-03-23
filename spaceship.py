'''
CS5001
Spring 2019
Hasti Gheibi Dehnashi
HW 5

Consulted stackoverflow to learn how to count lines in a file, adapted following piece of code:

for i, line in enumerate(file):
        pass
    print(i+1)

https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
'''

import turtle
turtle.hideturtle()

import random

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
    for i in range(num_of_letters):
        distance_between_blanks = int((20*i) + 10)
        length_of_blank = int((20*i))
        turtle.penup()
        turtle.goto(length_of_blank,-200)
        turtle.pendown()
        turtle.goto(distance_between_blanks,-200)

def write_letter(xlocation, ylocation, letter):
    turtle.penup()
    turtle.goto(xlocation,ylocation)
    turtle.pendown()
    turtle.write(letter, align="center", font=("Arial", 12, "normal"))

def create_list_of_words_from_file(filename):
    file = open(filename, "r")
    wordList = []
    for words in file:
        current_word = words.strip()
        wordList.append(current_word)
    file.close
    return wordList

def choose_random_word_from_list(a_list):
    rand_word = random.choice(a_list)
    return rand_word

def prompt_user_for_guess():
    keep_prompting = True
    
    while keep_prompting:
        user_guess = input("Guess a letter\n")
        user_guess = user_guess.lower()
        if len(user_guess) > 1:
            print("Please guess one letter at a time")
        if user_guess.isalpha() == False:
            print("Please enter a letter")
        if len(user_guess) == 1 and user_guess.isalpha():
            keep_prompting = False
            return user_guess

def create_list_from_secret_word(word):
    list_of_characters_in_secret_word = []
    for character in word:
        list_of_characters_in_secret_word.append(character)
    return list_of_characters_in_secret_word

def check_if_secret_word_contains_user_guess(list_from_secret_word, user_guess):
    indices = [i for i, character in enumerate(list_from_secret_word) if character == user_guess]
    return indices

def draw_next_part_of_ship(number, letter):
    if number == 0:
        draw_ship_body()
        write_letter((75 - 10*number), 200, letter)
        
    if number == 1:
        draw_left_rocket()
        write_letter((75 - 10*number), 200, letter)
        
    if number == 2:
        draw_right_rocket()
        write_letter((75 - 10*number), 200, letter)
        
    if number == 3:
        draw_left_flame()
        write_letter((75 - 10*number), 200, letter)
    
    if number == 4:
        draw_right_flame()
        write_letter((75 - 10*number), 200, letter)

def write_score_to_file(scoresfile, player_name, score):
    scoresfile = open(scoresfile, "a")
    scoresfile.write("\n {} scored {} points".format(player_name, score))
    scoresfile.close()
    
"""

main()
draw_ship_body()
draw_left_rocket()
draw_right_rocket()
draw_left_flame()
draw_right_flame()
draw_blanks(8)
write_letter(65, "N")
write_letter(85, "O")
"""
