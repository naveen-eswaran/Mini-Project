import random

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock"     and computer == "scissors") or \
         (player == "scissors" and computer == "paper")   or \
         (player == "paper"    and computer == "rock"):
        return "player"
    else:
        return "computer"

def get_emoji(choice):
    emojis = {"rock": "✊", "paper": "🖐️", "scissors": "✌️"}
    return emojis[choice]

def main():
    print("✊🖐️✌️ Welcome to Rock Paper Scissors!")

    player_score = 0
    computer_score = 0
    draws = 0

    while True:
        print("\n--- Choose your move ---")
        print("1. Rock ✊")
        print("2. Paper 🖐️")
        print("3. Scissors ✌️")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "4":
            break

        moves = {"1": "rock", "2": "paper", "3": "scissors"}

        if choice not in moves:
            print("⚠️ Invalid choice! Enter 1, 2, 3 or 4.")
            continue

        player = moves[choice]
        computer = random.choice(["rock", "paper", "scissors"])

        print(f"\n🧑 You:      {get_emoji(player)}  {player.capitalize()}")
        print(f"🤖 Computer: {get_emoji(computer)}  {computer.capitalize()}")

        result = get_winner(player, computer)

        if result == "player":
            print("🎉 You Win this round!")
            player_score += 1
        elif result == "computer":
            print("😞 Computer Wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a Draw!")
            draws += 1

        print(f"\n📊 Score → You: {player_score} | Computer: {computer_score} | Draws: {draws}")

    # Final result
    print("\n====== FINAL SCORE ======")
    print(f"🧑 You:      {player_score}")
    print(f"🤖 Computer: {computer_score}")
    print(f"🤝 Draws:    {draws}")

    if player_score > computer_score:
        print("🏆 You are the overall Winner!")
    elif computer_score > player_score:
        print("🤖 Computer is the overall Winner!")
    else:
        print("🤝 Overall it's a Draw!")

    print("👋 Thanks for playing!")

main()