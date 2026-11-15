import random

def main():
  secret = random.randint(1, 100)
  print('I am thinking of a number between 1 and 100.')

  while True:
    try:
      guess = int(input('Your guess: '))
    except ValueError:
      print('Please enter a valid number.')
      continue

    if guess < secret:
      print('Too low.')
    elif guess > secret:
      print('Too high.')
    else:
      print('Correct! You guessed it.')
      break


if __name__ == '__main__':
  main()