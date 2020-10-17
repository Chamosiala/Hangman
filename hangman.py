import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
while 1:
    choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
    while choice != "play" and choice != "exit":
        choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if choice == "exit":
        break
    correct_word = random.choice(words)
    letters = set()
    for char in correct_word:
        letters.update(char)
    hidden_word = '-' * (len(correct_word))
    hidden_word = list(hidden_word)
    guessed_letters = set()

    tries = 8
    while tries > 0:
        print("")
        for i in range(len(hidden_word)):
            print(hidden_word[i], end='')
        letter = input("\nInput a letter: ")

        if letter.islower() and len(letter) == 1 and letter not in guessed_letters:
            if letter in letters:
                guessed_letters.update(letter)
                for i in range(len(hidden_word)):
                    if correct_word[i] == letter:
                        hidden_word[i] = letter
            else:
                print("No such letter in the word")
                guessed_letters.update(letter)
                tries -= 1
            if '-' not in hidden_word:
                break
        elif len(letter) != 1:
            print("You should input a single letter")
        elif letter.isupper() or not letter.isalpha():
            print("It is not an ASCII lowercase letter")
        else:
            print("You already typed this letter")

    if tries > 0:
        print("You guessed the word!")
        print("You survived!\n")
    else:
        print("You lost!\n")
