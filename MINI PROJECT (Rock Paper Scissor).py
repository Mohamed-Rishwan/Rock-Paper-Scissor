import random as r
choices = ["rock", "paper", "scissor"]
player_score = 0
computer_score = 0
tie_score = 0
print("ROCK PAPER SCISSOR GAME")
print("Type 'exit' to quit\n")
while True:
    player_choice = input("Enter your choice:").lower()
    if player_choice == "exit":
        print("\nThanks for playing!")
        print("======== FINAL SCOREBOARD ========")
        print(f"You: {player_score}")
        print(f"Computer: {computer_score}")
        print(f"Ties: {tie_score}")
        print("==================================")
        break
    if player_choice not in choices:
        print("Invalid choice! Try again.\n")
        continue
    computer_choice = r.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!\n")
        tie_score += 1
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper"):
        print("You win!\n")
        player_score += 1
    else:
        print("Computer wins!\n")
        computer_score+=1
