import random

lives = 9
word = ['kitty', 'snake', 'black','house']
secret_word = random.choice(word)
clue = ['?', '?', '?', '?', '?']
guessed_correctly = False

def update_clue(guessed_letter,secret_word,clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

while lives > 0:
    print(clue)
    print(f'lives left:{lives}')
    guess = input('Guess the letter or the whole word')

    if guess == secret_word:
        guessed_correctly = True
        break
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('Incorrect')
        lives = lives - 1
if guessed_correctly:
    print('You won')
else:
    print('Lost')








