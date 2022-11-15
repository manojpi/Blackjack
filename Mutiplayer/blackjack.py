from blackjack_helper import *

player_numer = int(input("Welcome to Blackjack! How many players? "))
players_data = []
prev_yes_no = []
round_number = 1

for i in range(player_numer):
  player_name = input("What is player "+str(i+1)+" name? ").upper()
  players_data.append([player_name, 3, 'y',0])
  prev_yes_no.append('y')


def user_turn(user_name):
  user_hand = draw_starting_hand(user_name)
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand)).lower()
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
    
  print_end_turn_status(user_hand)
  return user_hand


def another_round_determiner(matrix):
  zero_scores = 0
  for row in matrix:
    if row[1] == 0:
      zero_scores += 1
  
  if zero_scores == len(matrix):
    return False
  
  for row in matrix:
    if row[2] == 'y' and row[1] > 0:
      return True

  return False


while another_round_determiner(players_data):

  print_header("Round " + str(round_number))

  for i in range(len(players_data)):
    if players_data[i][2] == 'y' and players_data[i][1] > 0:
      players_data[i][-1] = user_turn(players_data[i][0])

      players_data[i][2] = input("Do you (" + players_data[i][0] + ") want to play another hand (y/n)? ").lower()

  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)

  print_header('GAME RESULT')

  for player_data_index in range(len(players_data)):
    if prev_yes_no[player_data_index] == 'y' and players_data[player_data_index][1] > 0:
      rslt = print_end_game_status(players_data[player_data_index][-1], dealer_hand, players_data[player_data_index][0],players_data[player_data_index][1])
      players_data[player_data_index][1] = rslt
      if players_data[player_data_index][1] == 0:
        print(players_data[player_data_index][0]+" eliminated!")
        players_data[player_data_index][2] == 'n'
    prev_yes_no[player_data_index] = players_data[player_data_index][2]
  
  round_number += 1

else:
  print_header("All players eliminated!\nTHANK YOU FOR PLAYING THE BLACKJACK GAME")
