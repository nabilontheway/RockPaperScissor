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
    if choice == compChoice :
        result = "DRAW"
    elif (choice == 1 and compChoice == 2) or (compChoice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and compChoice == 3) or (compChoice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and compChoice == 3) or (compChoice == 2 and choice == 3):
        result = "Scissors"            

    #Print the Result.
    if result == "DRAW":
        print("<== It's a Draw ==>")
    elif result == choiceName:
        print("<== User Wins ==>")
    else:
        print("<== Computer Wins ==>")            

    #Ask if the User wants to play again
    print("Do you want to play again? (Y/N)")
    answer = input().lower()
    if answer == "n":    
        break

#After coming out of while loop, greet the user
print("Thanks for playing!")    