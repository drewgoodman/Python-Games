# © 2019, Drew Goodman, all rights reserved

import random

main_title = """
..######...##.....##.########..######...######..####.##....##..######..
.##....##..##.....##.##.......##....##.##....##..##..###...##.##....##.
.##........##.....##.##.......##.......##........##..####..##.##.......
.##...####.##.....##.######....######...######...##..##.##.##.##...####
.##....##..##.....##.##.............##.......##..##..##..####.##....##.
.##....##..##.....##.##.......##....##.##....##..##..##...###.##....##.
..######....#######..########..######...######..####.##....##..######..
..######......###....##.....##.########                                
.##....##....##.##...###...###.##......                                
.##.........##...##..####.####.##......                                
.##...####.##.....##.##.###.##.######..                                
.##....##..#########.##.....##.##......                                
.##....##..##.....##.##.....##.##......                                
..######...##.....##.##.....##.########                   """

winning_message = """
 #     #                                         ### 
  #   #    ####   #    #      #    #  #  #    #  ### 
   # #    #    #  #    #      #    #  #  ##   #  ### 
    #     #    #  #    #      #    #  #  # #  #   #  
    #     #    #  #    #      # ## #  #  #  # #      
    #     #    #  #    #      ##  ##  #  #   ##  ### 
    #      ####    ####       #    #  #  #    #  ### 
                                                     """

guess_list = []
n = random.randint(1, 99)
score = 0
mistakes = 0

def guess_input():
    global mistakes
    global score
    new_guess = int(input("Enter an integer from 1 to 99: "))
    while new_guess in guess_list:
      mistakes += 1
      score += 1
      if mistakes < 5:
        print("You've already tried that number, dum dum. Pick again!\n")
      elif mistakes == 5:
        print("Uh, seriously, you know you can just scroll up to see what you already guessed, right?\n")
      elif mistakes < 8:
        print("Okay, this is starting to get a little embarassing. Pick a NEW number, scrub.\n")
      elif mistakes < 10:
        print("There are no words. Pick another number or consider the possibility of being dropped on your head as an infant.\n")
      else:
        print("Just..... pick a new number.\n")
      new_guess = int(input("Enter an integer from 1 to 99: "))
    else:
      guess_list.append(new_guess)
      return new_guess

print(main_title)
input("\nPRESS ENTER TO CONTINUE: ")
print("""\nLet's play a game.

I'm thinking of a number between 1 and 99. Totally random, I swear.

It's up to you to guess it. Isn't this original?\n""")
input("PRESS ENTER TO CONTINUE: \n\n")
guess = guess_input()

while n != "guess":
    print
    score += 1
    if guess < n:
        print(f"{guess} || Too low....\n")
        guess = guess_input()
    elif guess > n:
        print(f"{guess} || Too high....\n")
        guess = guess_input()
    else:
        print(f"\n{n}! You guessed it!\n")
        break
    print

print(winning_message)
print(f"NUMBER OF GUESSES NEEDED: {score}")
if mistakes > 0:
    print(f"NUMBER OF MISTAKES MADE: {mistakes}")
input("\nPRESS ENTER FOR A FINAL VERDICT:\n")
if score == 1:
  print("Probability of psychic powers: 99.90034234234 % ")
elif score == 2:
  print("Is that a +30 luck modifier in your pocket or are you just happy that you won?")
elif score == 3:
  print("Is that a +15 luck modifier in your pocket or are you just happy that you won?")
elif score > 3 and score < 6:
  print("You made some solid guesses there! Can your luck get any better?")
elif score >= 6 and score < 10:
  print("A good effort! Try making fewer guesses next time!")
elif mistakes > 0 and mistakes <= 3:
  print("Probably would have helped if you didn't make some mistakes along the way.")
elif mistakes > 3 and mistakes <=5:
  print("Pro tip: You can scroll up to see what numbers you've already put in, FYI.")
elif mistakes > 5 and mistakes < 10:
  print("Not sure how to tell you this, but you kept picking the same numbers over and over again. You know what the definition of insanity is?")
elif mistakes >= 10:
  print("Honestly, you probably lost this game the instant you were born. Hope you respawn without that IQ debuff in your next life.")
else:
  print("Meh. Git gud, son.")