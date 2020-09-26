import random

chances = 3
user = 0
comp = 0
print("\nPlease Choose a valid option from below list")
while(chances != 0):

    options = ("snake", "water", "gun")
    for index, opt in enumerate(options, 1):
        print(f"{index}. {opt}")

    choice = int(input("\nEnter the choice number\n"))
    if(1 <= choice <= 3):
        user_choice = options[choice - 1]
        comp_choice = random.choice(options)

        if(user_choice == comp_choice):
            pass

        elif((user_choice == "snake" and comp_choice != "gun") or (user_choice == "water" and comp_choice != "snake") or (user_choice == "gun" and comp_choice != "water")):
            user += 1
            chances -= 1

        else:
            comp += 1
            chances -= 1

        print("\nYou Chose --> " + user_choice)
        print("Computer Chose --> " + comp_choice)    
        print(f"You : {user}")
        print(f"Comp : {comp}")
        print(f"Chances Remaining : {chances}")

    else:
        print("Enter a valid option")

if(user == comp):
    print("\nThe game is Tied!")
elif(user > comp):
    print("\nYou won the game")
else:
    print("\nComputer Won the game")
