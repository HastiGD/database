from spaceship import *


def main(wordlist_filename):
    
    print("Welcome to the game of hangman")
    
    try:
        #the file containing the dictionary of words is read a list is created from it
        dictionary = create_list_of_words_from_file(wordlist_filename)
        
    except FileNotFoundError:
        #exits program if file doesn't exist
        print("No such FILE in directory")
        turtle.done()
        
    else:
        #a word is randomly chosen from dictionary
        secret_word = choose_random_word_from_list(dictionary)
        print(secret_word) #<----***ACTIVATE ME IF YOU WANT TO SEE THE SECRET WORD***
        
        #that word is turned into a list containing its individual characters
        secret_word_in_list = create_list_from_secret_word(secret_word) 
        num_characters_in_word = len(secret_word)
        #turtle draws blanks according to the number of characters in the word
        draw_blanks(num_characters_in_word)
        #winning and losing scores are initialized
        incorrect_guess_score = 0
        num_correct_letters_guessed = 0
        
        
        
        while incorrect_guess_score < 5 and num_characters_in_word != num_correct_letters_guessed:
            try:
                #user is prompted to make a guess until the game ends and they don't want to continue
                current_guess = prompt_user_for_guess()
                #check if user guessed correctly, if so, a list is created containing the location of the correct guess in the word
                indices_of_current_guess_occurence = check_if_secret_word_contains_user_guess(secret_word_in_list, current_guess)
                
            except TypeError as error:
                print("ERROR", error)
                turtle.done()
                break
            
            else:
                #checks for incorrect guesses and draws the ship and tally's score
                if not indices_of_current_guess_occurence:
                    print("Incorrect Guess")
                    draw_next_part_of_ship(incorrect_guess_score, current_guess)
                    incorrect_guess_score += 1
                    
                else:
                    #checks for accurate guesses and tally's score
                    for value in indices_of_current_guess_occurence:
                        num_correct_letters_guessed += 1 
                        write_letter((20*value + 5), -197, current_guess)

        #ends game if user loses
        if incorrect_guess_score == 5:
            print("Game Over, word is", secret_word)
            turtle.done()

        #notifies user that they won and asks if they want to play again
        if num_characters_in_word == num_correct_letters_guessed:
            print("Game over, you win!")
            user_name = input("Please enter your name")
            user_score = 1
            write_score_to_file("scoreslist.txt", user_name, user_score)
            play_again = input("Would you like to play again? Enter Y/N \n")
            play_again = play_again.lower()

            #restarts game if user wants to play again
            if play_again == "y":
                turtle.clearscreen()
                turtle.hideturtle()
                main("wordlist.txt")

            #ends game if user wants to quit
            else:
                print("Goodbye")
                turtle.done()
                    
                    
                    
main("wordlist.txt")
    
