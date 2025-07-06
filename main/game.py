import random

#Print Multiline Instruction
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    #Take the Input from the User
    choice = int(input("Enter Your Choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a Valid Choice: "))

    #Initialize Value of choiceName Variable corresponding to the Choice Value.
    if choice == 1:
        choiceName = "Rock"
    elif choice == 2:
        choiceName = "Paper"
    else:
        choiceName = "Scissors"    

    #Print User Choice.
    print("User Choice is: ", choiceName)
    print("Now it's Computer's turn....")

    #Computer Chooses any Number Between 1 to 3
    compChoice = random.randint(1,3)

    #Initialize Value of choiceName Variable corresponding to the Choice Value.
    if compChoice == 1:
        compChoiceName = "Rock"
    elif choice == 2:
        compChoiceName = "Paper"
    else:
        compChoiceName = "Scissors" 

    print("Computer's Choice is: ", compChoiceName)
    print(choiceName, "vs", compChoiceName)

    #Determine the winner
           