import random
# A rock, paper and scissors mini programn

hands = ["rock", "paper", "scissors"]
cpu_hand = random.choice(hands)
player = input("Rock, paper or scissors? \n").lower()

print(f"Your hand: {player}")
print(f"cpu entered: {cpu_hand}")

if player in hands :
    if player == "rock" and cpu_hand == "scissors":
        print("You win!")
    elif player == "paper" and cpu_hand == "rock":
        print("You win!")
    elif player == "scissors" and cpu_hand == "paper":
        print("You win!")
    elif player == cpu_hand:
        print("A draw!")
    else:
        print("You lose..")
else:
    print("Invalid hand...")
