from art import logo
import random

def blackjack():
    print(logo)

    start = input("Welcome to blackjack! To play, type START.\n").lower()

    while start != "start":
        start = input("Invalid input. Type START to play.\n").lower()

    print("")
    print('Rules:\n•The deck is unlimited in size.\n•There are no jokers.\n•The Jack/Queen/King all count as 10.\n•The Ace can count as 11 (if the current count is below 11) or 1 (if the current count is 11 or above).\n•Going over 21 counts as a "bust" and you lose.\n•Get as close to 21 as you can to win!')
    print("")

    dealer_count = 0
    player_count = 0
    dealer_cards_in_hand = []
    player_cards_in_hand = []
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    dealer_cards_in_hand.append(random.choice(cards))
    for _ in range(2):
        player_cards_in_hand.append(random.choice(cards))

    def calculate_count(cards):
        count = 0
        number_of_aces = 0
        for card in cards:
            if isinstance(card, int):
                count += card
            elif isinstance(card, str) and card in ['J', 'Q', 'K']:
                count += 10
            elif isinstance(card, str) and card == 'A':
                count += 11
                number_of_aces += 1

        while count > 21 and number_of_aces > 0:
            count -= 10
            number_of_aces -= 1

        return count

    player_count = calculate_count(player_cards_in_hand)
    dealer_count = calculate_count(dealer_cards_in_hand)

    print(f"Dealer's card: {dealer_cards_in_hand}")
    if player_count == 21:
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
        while choice != "hit" and choice != "stand":
            choice = input('Invalid input. Please type "Hit" or "Stand".').lower()

        while choice == "hit":
            new_card = random.choice(cards)
            player_cards_in_hand.append(new_card)
            print(f"Your cards: {player_cards_in_hand}")
            player_count = calculate_count(player_cards_in_hand)
            print(f"Count: {player_count}")

            if player_count > 21:
                bust = input("You busted. Play again? (Yes or No)\n").lower()
                if bust == "yes":
                    return blackjack()
                while bust != "yes":
                    if bust == "no":
                        print("Thanks for playing! Hire me, please.")
                        return
                    else:
                        bust = input('Invalid input. Please type "Yes" or "No"\n').lower()

            elif player_count == 21:
                print("You reached 21!")
                choice = "stand"
            else:
                choice = input(f"Your cards: {player_cards_in_hand} Hit or Stand?\n").lower()
                while choice != "hit" and choice != "stand":
                    choice = input('Invalid input. Please type "Hit" or "Stand".').lower()

    def dealer(cards, dealer_count):
        while dealer_count < 17:
            new_card = random.choice(cards)
            dealer_cards_in_hand.append(new_card)
            print(f"Dealer's cards: {dealer_cards_in_hand}")
            dealer_count = calculate_count(dealer_cards_in_hand)
            print(f"Count: {dealer_count}")

        if dealer_count >= 17 and dealer_count <= 21:
            if dealer_count == player_count:
                draw = input("It's a draw. Play again? (Yes or No)\n").lower()
                if draw == "yes":
                    return blackjack()
                while draw != "yes":
                    if draw == "no":
                        print("Thanks for playing! Hire me, please.")
                        return
                    else:
                        draw = input('Invalid input. Please type "Yes" or "No"\n').lower()
            elif dealer_count > player_count:
                lose = input("Dealer wins. Play again? (Yes or No)\n").lower()
                if lose == "yes":
                    return blackjack()
                while lose != "yes":
                    if lose == "no":
                        print("Thanks for playing! Hire me, please.")
                        return
                    else:
                        lose = input('Invalid input. Please type "Yes" or "No"\n').lower()
            elif dealer_count < player_count:
                win = input("You win! Play again? (Yes or No)\n").lower()
                if win == "yes":
                    return blackjack()
                while win != "yes":
                    if win == "no":
                        print("Thanks for playing! Hire me, please.")
                        return
                    else:
                        win = input('Invalid input. Please type "Yes" or "No"\n').lower()

        if dealer_count > 21:
            dealer_bust = input("Dealer busted. You win! Play again? (Yes or No)\n").lower()
            if dealer_bust == "yes":
                return blackjack()
            while dealer_bust != "yes":
                if dealer_bust == "no":
                    print("Thanks for playing! Hire me, please.")
                    return
                else:
                    dealer_bust = input('Invalid input. Please type "Yes" or "No"\n').lower()

    dealer(cards, dealer_count)

blackjack()
