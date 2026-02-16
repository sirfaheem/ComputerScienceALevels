#no you win message



import random

# Define the ranks and suits of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♣', '♦']

# Create a deck of cards
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + suit)

# Shuffle the deck
random.shuffle(deck)

# Deal the cards to the player and the dealer
player_hand = []
dealer_hand = []
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Calculate the total value of a hand
def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            total += 10
        elif card[0] == 'A':
            aces += 1
        else:
            total += int(card[0])
    # Add the value of the aces, if any
    for i in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

# Print the player's hand
print("Your hand:")
for card in player_hand:
    print(card)
print("Total:", calculate_hand(player_hand))

# Print the dealer's hand
print("Dealer's hand:")
print(dealer_hand[0])
print("Total:", calculate_hand([dealer_hand[0]]))

# Check if the player has 21
if calculate_hand(player_hand) == 21:
    print("Blackjack! You win.")
    exit()

# Prompt the player to hit or stand
while True:
    choice = input("(H)it or (S)tand? ")
    if choice.lower() == 'h':
        # Deal the player another card
        player_hand.append(deck.pop())
        # Calculate the total value of the player's hand
        total = calculate_hand(player_hand)
        # Print the player's hand
        print("Your hand:")
        for card in player_hand:
            print(card)
        print("Total:", total)
        # Check if the player has bust
        if total > 21:
            print("You bust! Dealer wins.")
            exit()
    elif choice.lower() == 's':
        break

# Reveal the dealer's hidden card
print("Dealer's hand:")
for card in dealer_hand:
    print(card)
total = calculate_hand(dealer_hand)
print("Total:", total)

# Dealer hits until their total is 17 or higher
while total < 17:
    dealer
