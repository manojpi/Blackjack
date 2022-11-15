from blackjack_helper import *


hand_value1 = draw_starting_hand("YOUR")

while hand_value1 < 21:
    should_hit = input('You have ' + str(hand_value1) + ". Hit (y/n)? ")

    if should_hit == 'n':
        break
    elif should_hit == 'y':
        card_value = draw_card()
        hand_value1 = hand_value1 + card_value
    else:
        print("Sorry I didn't get that.")

print_end_turn_status(hand_value1)

hand_value2 = draw_starting_hand("DEALER")
if hand_value2 < 17:
    print("Dealer has {}.".format(hand_value2))
    
while hand_value2 < 17:
  card_value = draw_card()

  hand_value2 += card_value
  if hand_value2 < 17:
    print("Dealer has {}.".format(hand_value2))
  
print_end_turn_status(hand_value2)

print_end_game_status(hand_value1, hand_value2)

