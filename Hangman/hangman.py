# Write your code here
import random

state = True
won = 0
lost = 0
print("""H A N G M A N""")
while state:
    print("""Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:""")
    menu = input()
    if menu == "results":
        print("You won: " + str(won) + " times")
        print("You lost: " + str(lost) + " times")
        continue
    elif menu == "exit":
        break
    else:
        attempts = 8
        a = 0
        i = 0
        z = 0
        l_letter = []
        x = ('python', 'java', 'swift', 'javascript')
        main_word = random.choice(x)
        show_word = ("-" * (len(main_word)))
        s: list[str] = list(show_word)
        while i < attempts:
            i += 1
            print(*s, sep="")
            letter = input("Input a letter:")
            z += 1
            if len(letter) != 1:
                i -= 1
                print("Please, input a single letter.\n")
                continue
            if not str.islower(letter):
                print("Please, enter a lowercase letter from the English alphabet.\n")
                i -= 1
                continue
            if letter in l_letter:
                i -= 1
                print("You've already guessed this letter.\n")
                continue
            l_letter.append(letter)
            if letter in main_word:
                if letter not in s:
                    for pos, char in enumerate(main_word):
                        if char == letter:
                            a = pos
                            s[a] = letter
                    print("")
                    i -= 1
                else:
                    print("You've already guessed this letter.\n")
            else:
                print("That letter doesn't appear in the word.\n")

            if s == list(main_word):
                print("You guessed the word " + main_word + "!")
                break
        if s == list(main_word):
            print("You survived!")
            won += 1
        else:
            print("You lost!")
            lost += 1
