from random import randint
result = ["win", "lose","draw","win","loss"]
choice = ["Rock", "Paper", "Scissors"]
computer = randint(1,3)
print(result[(int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors."))-computer+2)], "Computer chose:",choice[computer-1])


