# Title:Hangman PS2
# Name: George Warlow
# Hours Spent: 6
# Update: DONEZO 2
# Date: 08/11/2025

#variables

hangmans = ['''|------|--
|         
|         
|         
|         
|         
|_________''',
'''|------|--
|      o  
|         
|
|         
|_________''',
'''|------|--
|      o  
|      |  
|         
|         
|_________''',
'''|------|--
|      o  
|     /|  
|         
|         
|_________''',
'''|------|--
|      o  
|     /|\\ 
|         
|         
|_________''',
'''|------|--
|      o  
|     /|\\ 
|     /   
|         
|_________''',
'''|------|--
|      o  
|     /|\\ 
|     / \\ 
|         
|_________
Game Over! You've been hung.''']

valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = "hangman"
guess = ""
tries = 6
word_as_underscore = len(word) * '_ '
letters_in_word = list(word)
word_set = set(word)
correct_guesses = []
incorrect_guesses = []
complete = False
continue1 = False

#Display Hangman
def DisplayHangman():
    print(f'You have {tries} tries remaining.')
    if tries == 6:
        print(hangmans[0])
    elif tries == 5:
        print(hangmans[1])
    elif tries == 4:
        print(hangmans[2])
    elif tries == 3:
        print(hangmans[3])
    elif tries == 2:
        print(hangmans[4])
    elif tries == 1:
        print(hangmans[5])
    elif tries == 0:
        print(hangmans[6])
    else:
        print('Error: Invalid number of tries.')

#Update Word Display
def UpdateWordDisplay():
    global word_as_underscore
    display = ''
    for i in word:
        if i in correct_guesses:
            display += i + ' '
        else:
            display += '_ '
    word_as_underscore = display

#Guess
def Guess():
    print('=' * 50)
    print(word_as_underscore)
    print('=' * 50)
    global guess
    guess = input('Please write your guess: ')

def CheckGuess():
    if guess not in valid_letters:
        print('Invalid input. Please enter a single letter from a-z.')
        print('=' * 50)
    elif guess in word:
        print(f'Good guess! {guess} is in the word!')
        print('=' * 50)
    else:
        print(f'Sorry, {guess} is not in the word.')
        print('=' * 50)

#Update Guesses
def UpdateGuessList():
    global tries, complete
    if guess in letters_in_word:
        correct_guesses.append(guess)
        UpdateWordDisplay()
        if set(correct_guesses) == word_set:
            print('=' * 50)
            print(word_as_underscore)
            print('=' * 50)
            print('You have matched all letters!')
            complete = True
    else:
        incorrect_guesses.append(guess)
        tries -= 1
    # Display hangman after each guess, but not if game is complete
    if not complete:
        DisplayHangman()
    if tries <= 0:
        GameEnd()

def DisplayGuessLists():
    print(f'Your current correct guesses are {correct_guesses}')

#Game Start
def GameStart():
    print('=' * 50)
    print('Welcome To Hangman!')
    DisplayHangman()

#Game End
def GameEnd():
    global complete
    complete = True

#Game Loop
GameStart()
while not complete:
    Guess()
    CheckGuess()
    UpdateGuessList()
    DisplayGuessLists()
