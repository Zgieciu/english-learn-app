import csv
import random
import os

words_pl = []
words_ang = []
guessed = []

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='-')
        next(reader)
        for row in reader:
            words_ang.append(row[0])
            words_pl.append(row[1])
            guessed.append(False)

# check that all words are guessed
def guessed_all():
    i = 0
    for guess in guessed:
        if guess:
            i += 1

    if i == len(guessed):
        return True
    else:
        return False
    
# check how many words user guessed
# return a precent of guessed words
def check_guess_percent():
    guessed_words = sum(guessed)
    return int(guessed_words / len(guessed) * 100)

# draw a bar with percent progress
def draw_percent():
    print()
    print('[', end='')
    for i in range(30):
        if i * (100 / 30) < check_guess_percent():
            print("█", end='')
        else:
            print(" ", end='')
    print(']\n')

# display percent bar and word to guess
def display_word():
    print(f'You guessed: {check_guess_percent()}% words')
    draw_percent()
    if pl_ang == 1:
        print(words_ang[word])
    if pl_ang == 2: 
        print(words_pl[word])

def clear_console():
    os.system('cls')

# program start
read_csv('./words.csv')
clear_console()

while not guessed_all():
    word = random.randint(0, len(words_pl) - 1)
    pl_ang = random.randint(1, 2)

    if guessed[word]:
        continue

    display_word()
    
    guess = input()

    if guess == 'exit':
        clear_console()
        exit()

    if guess == words_pl[word] or guess == words_ang[word]:
         guessed[word] = True
    
    clear_console()
    display_word()
    print(guess)

    if guess == words_pl[word] or guess == words_ang[word]:
        print(f'Yes! {words_ang[word]} - {words_pl[word]}')
    else:
        print(f'Sadly no, true meaning: {words_ang[word]} - {words_pl[word]}')
    input("\nPress Enter to continue")
    clear_console()

print('Good job! You guessed all words!')
input()