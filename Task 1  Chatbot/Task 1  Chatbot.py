from datetime import datetime
import random

print("=" * 60)
print("🤖      WELCOME TO SMART RULE-BASED CHATBOT")
print("=" * 60)

name = input("Bot: Hello! What's your name? ")
print(f"Bot: Nice to meet you, {name}! 😊")
print("\nType 'help' to see all available commands.")
print("Type 'bye' anytime to exit.\n")

jokes = [
    "Why don't programmers like nature? Because it has too many bugs! 😂",
    "Why do Python programmers wear glasses? Because they can't C. 😄",
    "Why was the computer cold? It forgot to close its Windows! 🤣"
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Keep learning because knowledge never goes to waste.",
    "Believe in yourself. Every expert was once a beginner."
]

while True:
    user = input(f"{name}: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! 👋 How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking. 😊")

    elif "your name" in user:
        print("Bot: I'm SmartBot, your virtual assistant.")

    elif "my name" in user:
        print(f"Bot: Your name is {name}. 😄")

    elif "time" in user:
        print("Bot: Current Time:",
              datetime.now().strftime("%I:%M:%S %p"))

    elif "date" in user:
        print("Bot: Today's Date:",
              datetime.now().strftime("%d-%m-%Y"))

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif "quote" in user or "motivate" in user:
        print("Bot:", random.choice(quotes))

    elif "calculator" in user:
        try:
            print("Bot: Let's calculate!")
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Bot: Result =", num1 + num2)
            elif op == "-":
                print("Bot: Result =", num1 - num2)
            elif op == "*":
                print("Bot: Result =", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Bot: Result =", num1 / num2)
                else:
                    print("Bot: Division by zero is not allowed.")
            else:
                print("Bot: Invalid operator.")
        except ValueError:
            print("Bot: Please enter valid numbers.")

    elif "help" in user:
        print("\n📌 I can do the following:")
        print("• hi / hello")
        print("• how are you")
        print("• what is your name")
        print("• what is my name")
        print("• date")
        print("• time")
        print("• joke")
        print("• quote")
        print("• calculator")
        print("• thank you")
        print("• bye\n")

    elif "thank" in user:
        print("Bot: You're welcome! 😊 Happy to help.")

    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a wonderful day. 👋")
        break

    else:
        print("Bot: 🤔 I don't understand that yet.")
        print("Type 'help' to see what I can do.")