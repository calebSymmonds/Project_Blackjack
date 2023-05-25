from art import logo
import random

def blackjack():
    print(logo)

    start = input("Welcome to blackjack! To play, type START.\n").lower()

    while start != "start":
        start = input("Invalid input. Type START to play.\n").lower()

    print("")
    print('Rules:\n•The deck is unlimited in size.\n•There are no jokers.\n•The Jack/Queen/King all count as 10.\n•The Ace can count as 11 (if current count is below 11) or 1 (if current count is 11 or above).\n•Going over 21 counts as a "bust" and you lose.\n•Get as close to 21 as you can to win!')
    print("")

    dealer_count = 0
    player_count = 0
    dealer_cards_in_hand = []
    player_cards_in_hand = []
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    dealer_cards_in_hand.append(random.choice(cards))
    for _ in range(2):
        player_cards_in_hand.append(random.choice(cards))

    if isinstance(player_cards_in_hand[0], int) and isinstance(player_cards_in_hand[1], int):
        player_count += player_cards_in_hand[0] + player_cards_in_hand[1]
    else:
        for card in player_cards_in_hand:
            if isinstance(card, int):
                player_count += card
            elif isinstance(card, str) and card in ['J', 'Q', 'K']:
                player_count += 10
            elif isinstance(card, str) and card == 'A':
                if player_count < 11:
                    player_count += 11
                else:
                    player_count += 1
    if 'A' in player_cards_in_hand and player_count > 21:
        number_of_aces = player_cards_in_hand.count('A')
        while player_count > 21 and number_of_aces > 0:
            player_count -= 10
            number_of_aces -= 1

    print(f"Dealer's card: {dealer_cards_in_hand}")
    if 'A' in player_cards_in_hand and ('10' in player_cards_in_hand or 'J' in player_cards_in_hand or 'Q' in player_cards_in_hand or 'K' in player_cards_in_hand):
        print(f"{player_cards_in_hand} Blackjack! You win!")
        play_again = input("Play again? (Yes or No)\n").lower()
        if play_again == "yes":
            blackjack()
        elif play_again == "no":
            print("Thanks for playing! Hire me, please.")
            return
        else:
            while play_again != "yes" and play_again != "no":
                play_again = input('Invalid input. Please type "Yes" or "No"\n').lower()
    else:
        choice = input(f"Your cards: {player_cards_in_hand} Hit or Stand?\n").lower()

    def player(cards, count):
        if choice == "hit":
            new_card = random.choice(cards)
            player_cards_in_hand.append(new_card)
            print(f"Your cards: {player_cards_in_hand}")

            def hit(cards, count):
                if isinstance(new_card, int):
                    count += new_card
                elif isinstance(new_card, str) and new_card in ['J', 'Q', 'K']:
                    count += 10
                elif isinstance(new_card, str) and new_card == 'A':
                    if count < 11:
                        count += 11
                    else:
                        count += 1

                if 'A' in player_cards_in_hand and count > 21:
                    number_of_aces = player_cards_in_hand.count('A')
                    while count > 21 and number_of_aces > 0:
                        count -= 10
                        number_of_aces -= 1
                return count

            count = hit(cards, count)
            print(f"Count: {count}")

            if count > 21:
                bust = input("You busted. Play again? (Yes or No)\n").lower()
                if bust == "yes":
                    blackjack()
                while bust != "yes":
                    if bust == "no":
                        print("Thanks for playing! Hire me, please.")
                        return
                    else:
                        bust = input('Invalid input. Please type "Yes" or "No"\n').lower()

    player(cards, player_count)
    print("Computer's hand: ")

blackjack()
