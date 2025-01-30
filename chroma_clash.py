import art
import random
print(art.logo1)
print("Welcome to chroma clash")

Red = [
    ("Red", "0"),
    ("Red", "1"), ("Red", "1"),
    ("Red", "2"), ("Red", "2"),
    ("Red", "3"), ("Red", "3"),
    ("Red", "4"), ("Red", "4"),
    ("Red", "5"), ("Red", "5"),
    ("Red", "6"), ("Red", "6"),
    ("Red", "7"), ("Red", "7"),
    ("Red", "8"), ("Red", "8"),
    ("Red", "9"), ("Red", "9"),
    ("Red", "Skip"), ("Red", "Skip"),
    ("Red", "Reverse"), ("Red", "Reverse"),
    ("Red", "Draw Two"), ("Red", "Draw Two"),
]
Blue = [
    ("Blue", "0"),
    ("Blue", "1"), ("Blue", "1"),
    ("Blue", "2"), ("Blue", "2"),
    ("Blue", "3"), ("Blue", "3"),
    ("Blue", "4"), ("Blue", "4"),
    ("Blue", "5"), ("Blue", "5"),
    ("Blue", "6"), ("Blue", "6"),
    ("Blue", "7"), ("Blue", "7"),
    ("Blue", "8"), ("Blue", "8"),
    ("Blue", "9"), ("Blue", "9"),
    ("Blue", "Skip"), ("Blue", "Skip"),
    ("Blue", "Reverse"), ("Blue", "Reverse"),
    ("Blue", "Draw Two"), ("Blue", "Draw Two"),
]
Green = [
    ("Green", "0"),
    ("Green", "1"), ("Green", "1"),
    ("Green", "2"), ("Green", "2"),
    ("Green", "3"), ("Green", "3"),
    ("Green", "4"), ("Green", "4"),
    ("Green", "5"), ("Green", "5"),
    ("Green", "6"), ("Green", "6"),
    ("Green", "7"), ("Green", "7"),
    ("Green", "8"), ("Green", "8"),
    ("Green", "9"), ("Green", "9"),
    ("Green", "Skip"), ("Green", "Skip"),
    ("Green", "Reverse"), ("Green", "Reverse"),
    ("Green", "Draw Two"), ("Green", "Draw Two"),
]

Yellow = [
    ("Yellow", "0"),
    ("Yellow", "1"), ("Yellow", "1"),
    ("Yellow", "2"), ("Yellow", "2"),
    ("Yellow", "3"), ("Yellow", "3"),
    ("Yellow", "4"), ("Yellow", "4"),
    ("Yellow", "5"), ("Yellow", "5"),
    ("Yellow", "6"), ("Yellow", "6"),
    ("Yellow", "7"), ("Yellow", "7"),
    ("Yellow", "8"), ("Yellow", "8"),
    ("Yellow", "9"), ("Yellow", "9"),
    ("Yellow", "Skip"), ("Yellow", "Skip"),
    ("Yellow", "Reverse"), ("Yellow", "Reverse"),
    ("Yellow", "Draw Two"), ("Yellow", "Draw Two"),
]


# Repeat this for Blue, Green, and Yellow.

Wild = [
    ("Wild", "Wild"), ("Wild", "Wild"), ("Wild", "Wild"), ("Wild", "Wild"),
    ("Wild", "Draw Four"), ("Wild", "Draw Four"), ("Wild", "Draw Four"), ("Wild", "Draw Four"),
]

# Combine all cards into a single deck list:
deck = Red + Blue + Green + Yellow + Wild
# random.shuffle(deck)

player_hand = deck[0:7]
computer_hand = deck[7:14]
top_card = deck[14]
remaining_deck = deck[15:]

player_card = [("Red","2")]
computer_card = [("yellow","2")]


def is_valid(player_card,computer_card):
    top_card_color = top_card[0]
    player_card_color = player_card[0]
    computer_card_color = computer_card[0]
    if top_card_color in player_card_color:
        print("turn is for player")
    if top_card_color in computer_card:
        print("turn is valid for computer")
    else:
        print("turn is not valid for computer")
# while not player_hand or computer_hand:
#     print(f"Card on top{top_card}")


is_valid(player_card=player_card,computer_card=computer_card)
# if computer_hand == []:
#     print("You've lost to the computer!, Computer wins!!!")
# elif player_hand == []:
#     print("You have defeated the computer sucessfully. Congratulations. Player Wins!!!")