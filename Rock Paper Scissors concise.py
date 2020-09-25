from random import randint


t = ["Rock", "Paper", "Scissors"] #list of possible options

#assign a random number to the computer
computer = randint(0,2)

#start loop
player = False

while player == False:
    rawinput = int(input(" 1.Rock 2.Paper 3.Scissors | Enter 1-3: ")) #number associated with list option
    playerinput = rawinput-1
    if playerinput == computer:
        print("Tie!")
        print("Computer entered:", t[computer], "You entered:", t[playerinput])
    elif (playerinput == 0 and computer == 1) or (playerinput == 1 and computer == 2) or (playerinput == 2 or computer == 0):
            print("You lose!") 
            print("Computer entered:", t[computer], "You entered:", t[playerinput])
    elif (playerinput == 1 and computer == 0) or (playerinput == 2 and computer == 1) or (playerinput == 0 or computer == 2):
            print("You win!") 
            print("Computer entered:", t[computer], "You entered:", t[playerinput])
    else:
        print("That's not a valid input.")
    playerchoice = int(input("Do you wish to continue? Enter 1 to continue or 0 to end "))#if you want to stay in loop or not
    if playerchoice == 1:
        player = False
        computer = t[randint(0,2)]
    elif playerchoice == 0:
        player = True
