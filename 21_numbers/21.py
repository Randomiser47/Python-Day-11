from art import logo
import random
# print(logo)
replay = True
def number_dealer():
    numbers = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    randed = random.choice(numbers)
    return randed

def list_addition(list_numbers):
    total = 0
    for num in list_numbers:
        total += num
    return total


computer_numbers = []
player_numbers = []

while replay == True:
    for i in range (0,2):
        player_numbers.append(number_dealer())
    print(f"Your score is {list_addition(player_numbers)}")

    recieve_another_number = input("Would you like to recieve another number?")  
    if recieve_another_number == "y":
        player_numbers.append(number_dealer())  
    print(f"Your score is {list_addition(player_numbers)}")
    computer_numbers.append(number_dealer())





    play_again = input("Would you like to play the game again?")
    if play_again == "y":
        replay = True
    elif play_again == "n":
        replay = False
print(computer_numbers)
print(player_numbers)