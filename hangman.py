# Write your code here
import random


def main():
    print('H A N G M A N')
    play_token = 0
    while play_token == 0:
        play_input = input('Type "play" to play the game, "exit" to quit: ')
        if play_input == "play":
            hangman()
        elif play_input == "exit":
            play_token = 1


def hangman():
    # print('The game will be available soon.')
    list_of_words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(list_of_words)
    word_list = list(word)
    guess_list = ['-'] * len(word)
    guess_left = 8
    already_guess = set()

    # width = len(word)
    # fill_char = '-'
    # hint = word[:3].ljust(width, fill_char)

    # guess = input('Guess the word! ' + hint + ':  ')
    # for i in range(8):
    while guess_left != 0:
        print("\n" + "".join(guess_list))
        # print("".join(word_list))
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('You should input a single letter')
        elif not guess.isalpha() or not guess.islower():
            print('Please enter a lowercase English letter')
        elif guess in already_guess:
            print("You've already guessed this letter")
        elif word.find(guess) == (-1):
            print("That letter doesn't appear in the word")
            already_guess.add(guess)
            guess_left -= 1
        else:
            # if correct_guess.count(guess) == 0:
            for index, letter in enumerate(word_list):
                # print(letter)
                # print(index)
                if guess == letter:
                    guess_list[index] = guess
                    already_guess.add(guess)
            if guess_list == word_list:
                guess_left = 0
            # else:
            #     print('No improvements')
            #     guess_left -= 1

    if guess_list == word_list:
        print('You guessed the word!\n'
              'You survived!')
    else:
        print('You lost!')

# print("Thanks for playing! "
#       "\nWe'll see how well you did in the next stage")

# if guess == word:
#     print('You survived!')
# else:
#     print('You lost!')


if __name__ == '__main__':
    main()
