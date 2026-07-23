import random
# added by ai:
import time
# added by ai:
print("=" * 40)
print("🎲      WELCOME TO ROLL THE DICE      🎲")
print("=" * 40)

while True:
    choice = input("\n🎮 Roll the dice? (y/n): ").lower()

    if choice == "y":
        print("\n🎲 Rolling the dice...")
# added by ai:
        time.sleep(1)

        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)

        print(f"\n🎲 Dice 1: {num1}")
        print(f"🎲 Dice 2: {num2}")
        print(f"✨ Result: ({num1}, {num2})")

    elif choice == "n":
        print("\n👋 Thanks for playing!")
        print("See you next time! 🎉")
        break

    else:
        print("❌ Invalid choice! Please enter 'y' or 'n'.")
