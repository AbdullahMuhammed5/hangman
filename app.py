import random

print("H A N G M A N")


def findOccurrences(s, ch):
  return [i for i, x in enumerate(s) if x == ch]


solved = False


def play_game():
  words = ['python', 'java', 'kotlin', 'javascript']
  choice = random.choice(words)
  hidden = "-" * len(choice)

  lives = 8
  inputs = errors = set()
  global solved

  while lives > 0:
    if not solved:
      letter = input(f'''\n{hidden}\nInput a letter: ''')

      if len(letter) > 1:
        print("You should input a single letter")
      elif letter in inputs or letter in errors:
        print("You've already guessed this letter")
      elif letter.isupper() or not letter.isalpha():
        print("Please enter a lowercase English letter")
      elif letter in choice:  # case letter found
        allOccurrences = findOccurrences(choice, letter)
        hidden = list(hidden)
        for i in allOccurrences:
          hidden[i] = letter
        hidden = "".join(hidden)
        inputs.add(letter)
      elif letter not in choice:  # case letter not found
        lives -= 1
        errors.add(letter)
        print("That letter doesn't appear in the word")
        if lives <= 0:
          print('''You lost!\n''')
          # reset to play again
          lives = 8
          inputs = errors = set()
          choice = random.choice(words)
          hidden = "-" * len(choice)
          break
    else:  # case winner
      print(f'''You guessed the word {choice}!\nYou survived!''')
      break

    solved = True if hidden.count("-") == 0 else False


state = 'play'

while state != 'exit' and not solved:
  state = input('Type "play" to play the game, "exit" to quit:')
  if state == 'play':
    play_game()

