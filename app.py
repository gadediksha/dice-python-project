import random

def roll_dice():
    return random.randint(1, 6)

player1_score = 0
player2_score = 0

print("******Welcome to the Dice Game******")
print("-----------------------------------\n")
print("Each player gets 3 chances.\n")

for i in range(1, 5):
    print(f"--- Round {i} ---")

    input("Player 1 press Enter to roll the dice:")
    p1 = roll_dice()
    player1_score += p1
    print("Player 1 rolled:", p1)

    input("Player 2 press Enter to roll the dice:")
    p2 = roll_dice()
    player2_score += p2
    print("Player 2 rolled:", p2)

    print()

print("🚩 Final Results")
print("Player 1 Total Score:", player1_score)
print("Player 2 Total Score:", player2_score)

if player1_score > player2_score:
    print("🏆 Player 1 Wins!")
elif player2_score > player1_score:
    print("🏆 Player 2 Wins!")
else:
    print("🤝 It's a Tie!")