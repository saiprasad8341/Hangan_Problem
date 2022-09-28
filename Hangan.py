import random


print("Welcome to the Hangan Game.....")

word_list = ["SPOTON", "DELHIVERY", "APPLE", "BANANA", "INDIA", "PYTHON"]


chosen_word = random.choice(word_list)


display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

lives = 7
stages = ['''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \\
 |
_|___

''', '''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / 
 |
_|___
''', '''
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      
 |
_|___
''', '''
  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |      
 |
_|___
''', '''
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
''', '''
  _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
_|___
''', '''
  _______
 |/      |
 |      
 |      
 |       
 |      
 |
_|___
''']

while not end_of_game:
    guess = input("Guess a letter: ").upper()

    if guess in display:
      print(f"You've already gussied {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You losses the Game :-|!! ")

    # print(display)
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You Win!!!!!!")

    print(stages[lives])
