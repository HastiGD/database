from spaceship import *

def main(wordlist_filename):
    
    print("Welcome to the game of hangman")
    
    try:
        dictionary = create_list_of_words_from_file(wordlist_filename)
        
    except FileNotFoundError:
        print("No such FILE in directory")
        turtle.done()
        
    else:
        secret_word = choose_random_word_from_list(dictionary)
        print(secret_word)
        secret_word_in_list = create_list_from_secret_word(secret_word)
        #print(secret_word_in_list)
        num_characters_in_word = len(secret_word)
        draw_blanks(num_characters_in_word)
        incorrect_guess_score = 0
        num_correct_letters_guessed = 0
        
        while incorrect_guess_score < 5 and num_characters_in_word != num_correct_letters_guessed:
            try:
                current_guess = prompt_user_for_guess()
                indices_of_current_guess_occurence = check_if_secret_word_contains_user_guess(secret_word_in_list, current_guess)
                
            except TypeError as error:
                print("ERROR", error)
                turtle.done()
                break
            
            else:
                if not indices_of_current_guess_occurence:
                    print("Incorrect Guess")
                    draw_next_part_of_ship(incorrect_guess_score, current_guess)
                    incorrect_guess_score += 1
                    print(incorrect_guess_score)
                    
                else:
                    for value in indices_of_current_guess_occurence:
                        num_correct_letters_guessed += 1 
                        print(num_correct_letters_guessed)
                        write_letter((20*value + 5), -197, current_guess)

        if incorrect_guess_score == 5:
            print("Game Over, word is", secret_word)
            turtle.done()
        if num_characters_in_word == num_correct_letters_guessed:
            print("Game over, you win!")
            play_again = input("Would you like to play again? Enter Y/N \n")
            play_again = play_again.lower()
            if play_again == "y":
                turtle.clearscreen()
                turtle.hideturtle()
                main("wordlist.txt")
            else:
                print("Goodbye")
                turtle.done()
                    
                    
                    
main("wordlist.txt")
    
