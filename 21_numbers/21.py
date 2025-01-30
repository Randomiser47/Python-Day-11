from art import logo
import random
# print(logo)

def number_dealer():
    numbers = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    randed = random.choice(numbers)
    return randed
computer_numbers = []
for i in range(0,3):
    computer_numbers.append(number_dealer())
print(computer_numbers)
