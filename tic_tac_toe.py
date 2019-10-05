space_list = [" "] * 9

player_markers = {
  1: "X",
  2: "O"
}

moves_made = 0
victor = 0
win_state = False
turn_player = "0"

def board_render():
  # global space_list
  layout = """
 +-----+-----+-----+
 |1) {0} |2) {1} |3) {2} |
 +-----+-----+-----+
 |4) {3} |5) {4} |6) {5} |
 +-----+-----+-----+
 |7) {6} |8) {7} |9) {8} |
 +-----+-----+-----+
  """.rstrip().format(*space_list)
  print(f"\n<===== {player_names[turn_player].upper()}'s TURN =====>")
  print(layout)
  print(f"\n* WHAT WILL {player_names[turn_player].upper()} ({player_markers[turn_player]}) DO? ")


def Is_Int(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False


def make_move():
  move_needed = True
  while move_needed:
    move = input(f"Enter a number, 1 through 9, to place a marker ({player_markers[turn_player]}) on that spot:  ")
    if Is_Int(move):
      move = int(move) - 1
      if move >= 0 and move <= 8:
        if space_list[move] == " ":
          space_list[move] = player_markers[turn_player]
          move_needed = False
        else:
          print("You must pick an empty space.")
      else:
        print("Input must be 1 through 9")
    else:
      print("Input must be a number.")


def check_row(row_to_check):
  # evaluate each line of the board for 3 in a row
  global victor
  if all(x == row_to_check[0] for x in row_to_check):
    if row_to_check[0] == " ":
      return False
    elif row_to_check[0] == player_markers[1]:
      victor = 1
      return True
    elif row_to_check[0] == player_markers[2]:
      victor = 2
      return True
  else:
    return False


def eval_board():
  # check for victory conditions
  global victor
  if check_row(list(space_list)[:3]):
    return True
  elif check_row(list(space_list)[3:6]):
    return True
  elif check_row(list(space_list)[6:9]):
    return True
  elif check_row(list(space_list)[:9:3]):
    return True
  elif check_row(list(space_list)[1:9:3]):
    return True
  elif check_row(list(space_list)[2:9:3]):
    return True
  elif check_row(list(space_list)[:9:4]):
    return True
  elif check_row(list(space_list)[2:8:2]):
    return True
  elif moves_made == 9:
    victor = 0
    return True
  else:
    not("Not a match!")
    return False


print("""

######## ####  ######          ########    ###     ######          ########  #######  ######## 
   ##     ##  ##    ##            ##      ## ##   ##    ##            ##    ##     ## ##       
   ##     ##  ##                  ##     ##   ##  ##                  ##    ##     ## ##       
   ##     ##  ##       #######    ##    ##     ## ##       #######    ##    ##     ## ######   
   ##     ##  ##                  ##    ######### ##                  ##    ##     ## ##       
   ##     ##  ##    ##            ##    ##     ## ##    ##            ##    ##     ## ##       
   ##    ####  ######             ##    ##     ##  ######             ##     #######  ######## 
""")
input("\n  >> Press ENTER to PLAY:  \n")

print("<===== WHO IS PLAYING? =====>")
name_one = input("  >> Please enter a name for Player One. Press ENTER to confirm: ").strip()
if (name_one == ""):
  name_one = "Player One"
name_two = input("  >> Please enter a name for Player Two. Press ENTER to confirm: ").strip()
if (name_two == ""):
  name_two = "Player Two"

player_names = {
  1: name_one,
  2: name_two
}

print(f"{player_names[1]} ({player_markers[1]}) vs {player_names[2]} ({player_markers[2]})")

while turn_player != "1" and turn_player != "2" and turn_player not in player_names.values():
  turn_player = input("Who should go first? Enter a player name, 1 or a 2, then press ENTER: ").strip()
if turn_player == "1" or turn_player == "2":
  turn_player = int(turn_player)
else:
  turn_player = 1 if turn_player == player_names[1] else 2
print(f"\n{player_names[turn_player]} ({player_markers[turn_player]}) will go first.\n")
input("Press ENTER to start the game: ")


while win_state is False:
  board_render()
  make_move()
  turn_player = 1 if turn_player == 2 else 2
  moves_made += 1
  win_state = eval_board()
  
if (victor > 0):
  print("\n\n W E   H A V E   A   W I N N E R ! !")
else:
  print(f"\n\n I T ' S   A   T I E ! !")

print("""
 +-----+-----+-----+
 |1) {0} |2) {1} |3) {2} |
 +-----+-----+-----+
 |4) {3} |5) {4} |6) {5} |
 +-----+-----+-----+
 |7) {6} |8) {7} |9) {8} |
 +-----+-----+-----+
  """.rstrip().format(*space_list))

if (victor > 0):
  print(f"\n{player_names[victor]} is the winner!")
  input("Press ENTER to quit the game: ")
else:
  print("\nIt's a draw! Restart the problem to play another round?")
  input("Press ENTER to quit the game: ")