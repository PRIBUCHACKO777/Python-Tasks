# Import the random module to generate random numbers
import random

# These are the 8 possible answers for the Magic 8 Ball game
answer1 = "Yes, definitely!"
answer2 = "It is certain."
answer3 = "Hmm, I'm not sure. Ask again!"
answer4 = "I can't say right now."
answer5 = "It's better if you don't know now."
answer6 = "No way!"
answer7 = "The outlook is not so good."
answer8 = "Very doubtful."

# Print a welcome message to the player
Name = input("Hey There! What is your name? ")
print("Hello", Name,"! Welcome to the Magic 8 Ball Game!")


# Ask the player to type their question and store it in the 'question' variable
question = input("What's your question? ")

# Let the player know the ball is 'thinking'
print("Shaking the Magic 8 Ball...")

# Pick a random number between 1 and 8
choice = random.randint(1, 8)

# Check what number was picked and give the answer that matches the number
if choice == 1:
    print(answer1) # If the random number is 1, show answer1
elif choice == 2:
    print(answer2) # If the random number is 2, show answer2
elif choice == 3:
    print(answer3) # If the random number is 3, show answer3
elif choice == 4:
    print(answer4) # If the random number is 4, show answer4
elif choice == 5:
    print(answer5) # If the random number is 5, show answer5
elif choice == 6:
    print(answer6) # If the random number is 6, show answer6
elif choice == 7:
    print(answer7) # If the random number is 7, show answer7
elif choice == 8:
    print(answer8) # If the random number is 8, show answer8