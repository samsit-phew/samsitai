import datetime
import time
import random
import webbrowser


print("""
███████  █████  ███    ███ ███████ ██ ████████      █████  ██
██      ██   ██ ████  ████ ██      ██    ██        ██   ██ ██
███████ ███████ ██ ████ ██ ███████ ██    ██        ███████ ██
     ██ ██   ██ ██  ██  ██      ██ ██    ██        ██   ██ ██
███████ ██   ██ ██      ██ ███████ ██    ██        ██   ██ ██ by samsitkarki.
""")


name = input("Before starting, tell me your name for the best experience!\nName: ")


current_hour = time.localtime().tm_hour
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"{greeting}, {name}! I am Samsit, your AI assistant. How can I help you? ")


while True:
    user_input = input(": ").lower().strip()

    match user_input:
        case "hi" | "hello" | "whatsupp" | "supp" | "yoo" | "whatsgudd":
            print(f"Hello, {name}!")

        case "flip a coin" | "coin flip" | "toss a coin" | "heads or tails":
            print(f"The coin landed on: {random.choice(['Heads', 'Tails'])}")

        case "sing a song for me" | "sing for me" | "sing a song":
            lyrics = [
                "Your morning eyes, I could stare like watching stars!",
                "I could walk you by, and I'll tell without a thought",
                "You'd be mine, would you mind if I took your hand tonight?",
                "Know you're all that I want in this life",
                "I'll imagine we fell in love",
                "I'll nap under moonlight skies with you",
                "I think I'll picture us, you with the waves",
                "The ocean's colors on your face",
                "I'll leave my heart with your air, so let me fly with you.",
                "Would you be forever with me?"
            ]
            for line in lyrics:
                print(line)
                time.sleep(2)
            print("That's all I know! I'm still learning more songs.")

        case "jokes" | "jokes plz" | "tell jokes":
            print("Imagine if Ninja got a lil taper fade...")
            time.sleep(2)
            print("Imagine if Caseoh did 10 jumping jacks...")
            time.sleep(2)
            print("BOOM!")

        case "can you joke for me?" | "hey there can you tell me jokes?" | "can you joke for me":
            jokes = [
                "Why don't skeletons fight each other? They don't have the guts!",
                "Why did the math book look sad? Because it had too many problems!",
                "Why don’t oysters donate to charity? Because they’re shellfish!",
                "What did one wall say to the other wall? 'I'll meet you at the corner.'",
                "Why can't your nose be 12 inches long? Because then it would be a foot!",
                "What do you get when you cross a snowman and a vampire? Frostbite!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What do you call fake spaghetti? An impasta!",
                "Why did the bicycle fall over? Because it was two-tired!",
                "What’s orange and sounds like a parrot? A carrot!"
            ]
            print(random.choice(jokes))

        case "can you perform mathematical calculation for me?" | "can you do maths for me?" | "hey can you do maths" | "maths":
            print("1. Addition\n2. Multiplication\n3. Division\n4. Subtraction")
            try:
                operation = int(input("What would you like to do? Enter only the number: "))
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))

                match operation:
                    case 1:
                        print(f"The answer is {num1 + num2}")
                    case 2:
                        print(f"The answer is {num1 * num2}")
                    case 3:
                        print(f"The answer is {num1 / num2}" if num2 != 0 else "Error: Cannot divide by zero!")
                    case 4:
                        print(f"The answer is {num1 - num2}")
                    case _:
                        print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        case "end" | "bye" | "bye, bye" | "seeyaa" | "end session":
            print(f"Okay then, bye! Activate the program whenever you want to meet me, {name}.")
            time.sleep(2)
            print("Shutting down the assistant...")
            time.sleep(5)
            print("Assistant has been shut down successfully!")
            break

        case "repeat after me" | "say what i said":
            say = input("What shall I say or repeat? ")
            print(say)

        case "scissors, paper, rock" | "wanna play scissors paper rock?" | "wanna scissors paper rock?":
            choices = ["scissors", "paper", "rock"]
            computer_choice = random.choice(choices)

            print("Ok, release your beast at the count of 3!")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")

            print(f"I chose: {computer_choice}!!!")
            user_choice = input("Your turn: ").lower().strip()

            match (user_choice, computer_choice):
                case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
                    print("You win! ")
                case ("rock", "rock") | ("scissors", "scissors") | ("paper", "paper"):
                    print("It's a tie! 🤝")
                case ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper"):
                    print("You lose! ")
                case _:
                    print("Invalid input. Please choose Rock, Paper, or Scissors.")
        case "fuck you" | "goo kha" | "samsit is gay" | "your gay " |"samsitdai is gay" :
            print("punishing you>>>>>")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("suffferrrrrrrrrr !!!!!")
            break
        case "open youtube" | "youtube" |"open youtube plz":
            webbrowser.open("https://www.youtube.com")
        case "github" | "open github" | "open githubb plz":
            webbrowser.open("https://github.com")
        case "gmail" |"open gmail" | " open gmail plz ":
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        case "open  google " | "google" |"open google plz":
            webbrowser.open("https://www.google.com")
        case "open wikipedia" | "wiki" | "wikipedia" :
            webbrowser.open("https://www.wikipedia.org")
        case "spotify" | "open spotify" :
            webbrowser.open("https://open.spotify.com")
        case "vscode" | "code" | "open vs code" | "vs code web":
            webbrowser.open("https://vscode.dev")
        case "googledrive" | "google drive" | " open google drive":
            webbrowser.open("https://drive.google.com/drive/home?dmr=1&ec=wgc-drive-globalnav-goto")


        case _:
            print(f"Sorry, I'm still learning and I don't understand that yet. Maybe you're trying to say something else, {name}?")
