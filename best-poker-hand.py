from collections import defaultdict
from enum import Enum

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

def best_hand(hand):
    # Parse the hand into a list of tuples (rank, suit)
    parsed_hand = []
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank == '2':
            parsed_hand.append((Rank.TWO, Suit[suit]))
        elif rank == '3':
            parsed_hand.append((Rank.THREE, Suit[suit]))
        elif rank == '4':
            parsed_hand.append((Rank.FOUR, Suit[suit]))
        elif rank == '5':
            parsed_hand.append((Rank.FIVE, Suit[suit]))
        elif rank == '6':
            parsed_hand.append((Rank.SIX, Suit[suit]))
        elif rank == '7':
            parsed_hand.append((Rank.SEVEN, Suit[suit]))
        elif rank == '8':
            parsed_hand.append((Rank.EIGHT, Suit[suit]))
        elif rank == '9':
            parsed_hand.append((Rank.NINE, Suit[suit]))
        elif rank == 'T':
            parsed_hand.append((Rank.TEN, Suit[suit]))
        elif rank == 'J':
            parsed_hand.append((Rank.JACK, Suit[suit]))
        elif rank == 'Q':
            parsed_hand.append((Rank.QUEEN, Suit[suit]))
        elif rank == 'K':
            parsed_hand.append((Rank.KING, Suit[suit]))
        elif rank == 'A':
            parsed_hand.append((Rank.ACE, Suit[suit]))

    # Sort the hand by rank
    parsed_hand.sort(key=lambda x: x[0].value)

    # Check for flush
    flush = len(set(suit for _, suit in parsed_hand)) == 1

    # Check for straight
    straight = all(parsed_hand[i][0].value == parsed_hand[i-1][0].value + 1 for i in range(1, len(parsed_hand)))

    # Check for four of a kind
    four_of_a_kind = any(len([card for card in parsed_hand if card[0] == rank]) == 4 for rank in set(rank for rank, _ in parsed_hand))

    # Check for full house
    full_house = any(len([card for card in parsed_hand if card[0] == rank]) == 3 for rank in set(rank for rank, _ in parsed_hand)) and any(len([card for card in parsed_hand if card[0] == rank]) == 2 for rank in set(rank for rank, _ in parsed_hand))

    # Check for three of a kind
    three_of_a_kind = any(len([card for card in parsed_hand if card[0] == rank]) == 3 for rank in set(rank for rank, _ in parsed_hand))

    # Check for two pair
    two_pair = len([rank for rank in set(rank for rank, _ in parsed_hand) if len([card for card in parsed_hand if card[0] == rank]) == 2]) == 2

    # Check for one pair
    one_pair = any(len([card for card in parsed_hand if card[0] == rank]) == 2 for rank in set(rank for rank, _ in parsed_hand))

    # Determine the best hand
    if straight and flush:
        return "Straight Flush"
    elif four_of_a_kind:
        return "Four of a Kind"
    elif full_house:
        return "Full House"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a Kind"
    elif two_pair:
        return "Two Pair"
    elif one_pair:
        return "One Pair"
    else:
        return "High Card"

# Test the function
print(best_hand([("2", "H"), ("3", "D"), ("4", "C"), ("5", "S"), ("6", "H")]))  # Straight
print(best_hand([("2", "H"), ("2", "D"), ("2", "C"), ("2", "S"), ("6", "H")]))  # Four of a Kind
print(best_hand([("2", "H"), ("2", "D"), ("2", "C"), ("6", "S"), ("6", "H")]))  # Full House
print(best_hand([("2", "H"), ("3", "H"), ("4", "H"), ("5", "H"), ("6", "H")]))  # Flush
print(best_hand([("2", "H"), ("3", "D"), ("4", "C"), ("5", "S"), ("6", "D")]))  # Straight
print(best_hand([("2", "H"), ("2", "D"), ("2", "C"), ("6", "S"), ("7", "H")]))  # Three of a Kind
print(best_hand([("2", "H"), ("2", "D"), ("6", "C"), ("6", "S"), ("7", "H")]))  # Two Pair
print(best_hand([("2", "H"), ("2", "D"), ("3", "C"), ("6", "S"), ("7", "H")]))  # One Pair
print(best_hand([("2", "H"), ("3", "D"), ("4", "C"), ("6", "S"), ("7", "H")]))  # High Card