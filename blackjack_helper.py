from random import randint


def print_card_name(card_rank):

    if card_rank < 1 or card_rank > 13:
        print("BAD CARD")

    else:
        if card_rank == 1:
            card_name = "Ace"
        elif card_rank == 11:
            card_name = "Jack"
        elif card_rank == 12:
            card_name = "Queen"
        elif card_rank == 13:
            card_name = "King"
        else:
            card_name = str(card_rank)

        if card_rank == 1 or card_rank == 8:
            print('Drew an ' + card_name)
        else:
            print('Drew a ' + card_name)

  
def draw_card():

    card_rank = randint(1, 13)
    print_card_name(card_rank)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank

    return card_value
    

def print_header(message):

    print("-----------")
    print(message)
    print("-----------")


def draw_starting_hand(name):

    print_header(name+" TURN")
    card1 = draw_card()
    card2 = draw_card()

    return card1+card2

   
def print_end_turn_status(hand_value):

    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")

    
def print_end_game_status(user_hand, dealer_hand):

    print_header("GAME RESULT")
    if user_hand > 21:
        print("Dealer wins!")
    elif dealer_hand > 21:
        print("You win!")
    elif dealer_hand == user_hand:
        print("Push.")
    elif dealer_hand > user_hand:
        print("Dealer wins!")
    elif user_hand > dealer_hand:
        print("You win!")