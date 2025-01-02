import random

# Define the card values and suits
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
cards = []

for suit in suits:
    for rank in range(len(ranks)):
        cards.append([suit, ranks[rank]])
        
# print(cards)

# Shuffle the deck
# random.shuffle(cards)
# print(cards)

# pop up the card
# card = cards.pop()
# print(card)

# function
def shuffle():
    random.shuffle(cards)
    
def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

print(rank, values.get(rank))

# print(card)










    





