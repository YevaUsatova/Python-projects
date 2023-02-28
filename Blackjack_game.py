import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffles(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.suit == "Ace":
            self.aces += 1
            return self.aces

    def adjust_for_ace(self):
        # If there is an ace and total value is bigger than 21 : do minus 10 and remove ace
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please, enter your bet: "))
        except:
            print("Sorry, please, provide and integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you dont have enough chips")
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Hit or stand? Enter h or s.")
        if x[0].lower()=="h":
            hit(deck,hand)
        elif x[0].lower() =="s":
            print("Player stands, dealers turn")
            playing = False
        else:
            print("Sorry, i didnt understand that. Please, eneter h or s only")
            continue
        break


def show_some(player, dealer):
    # to show dealer one card face up
    print("\n Dealer's card: ")
    print("First card is hidden")
    print(dealer.cards[1])

    # Show all the player cards
    for card in player.cards:
        print(f"\n Player's cards: {card}")


def show_all(player, dealer):
    # Show all the player cards
    for card in player.cards:
        print(f"\n Player's cards: {card}")
        print(f"Players total: {player.value}")

    # Show all the dealer cards
    for card in dealer.cards:
        print(f"\n Dealer's cards: {card}")
        print(f"Dealers total: {dealer.value}")


def player_busts(player, dealer, chips):
    print("Player lost busts")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player won busts")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer lost busts")
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer won busts")
    chips.win_bet()


def push(player, dealer):
    print("Dealer and player tie. PUSH")


while True:
    # Print an opening statement
    print("Welcome to the black jack game")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffles()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealler_hand = Hand()
    dealler_hand.add_card(deck.deal())
    dealler_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealler_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealler_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealler_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealler_hand.value <= 17:
            hit(deck, dealler_hand)

        # Show all cards
        show_all(player_hand, dealler_hand)

        # Run different winning scenarios
        if dealler_hand.value > 21:
            dealer_busts(player_hand, dealler_hand, player_chips)
        elif dealler_hand.value > player_hand.value:
            dealer_wins(player_hand, dealler_hand, player_chips)
        elif dealler_hand.value < player_hand.value:
            player_wins(player_hand, dealler_hand, player_chips)
        else:
            push(player_hand, dealler_hand)

    # Inform Player of their chips total
    print(f"Your total chips is: {player_chips.total}")
    # Ask to play again
    new_game = input("Would you like to play again? ")
    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing.")
        break