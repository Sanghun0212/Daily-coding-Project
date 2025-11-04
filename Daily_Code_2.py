# ## Day2
# import random  ## Have to put "import random" before making code to choose random variables

# choices = ["rock", "paper", "scissors"]
# print (" Lets, play Rock, Paper, Scissors!")
# print ("Type 'quit' to stop the game.")

# while True: ## means  work forever
#     user = input("Your choice (rock/paper/scissors): ").lower()

#     if user == "quit":
#         print("Game Over. Thanks for playing")
#         break

#     if user not in choices:
#         print("invalid choices!")
#         continue

#     computer =  random.choice(choices)
#     print(f"Computer chose: {computer}")


#     if user == computer:
#         print("It's a tie!")
    
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         print(" you win!")

#     else:
#         print("you lose!")



# ## Example of using "continue" under the if loop

# while True:
#     word = input("Enter a word (type 'skip' to skip, 'stop' to end)")

#     if word == "skip":
#         print("Skipping This Round!")
#         continue

#     if word == "Stop":
#         print("Stopping This!")
#         break

#     print("you typed:", word)



import random

choices = ["r", "s", "p"]

print("lets play the game")



while True:
        
    user = input("Please enter btw R,S,P:").lower()
    
    computer = random.choice(choices)
    
    if user == "quit":
            print("Thank you for playing!")

    if user not in choices:
            print("Please rewrite!(R,S,P)")
            continue

    
    if user == computer:
            print("You are Tie")
            continue
    elif user == "R" and computer == "S" or \
         user == "S" and computer == "P" or \
            user == "P" and computer == "R":
            print(" You win!!") 
            break
    else:
            print("you lose!")
            break
    print(f"The computer chose: {computer}")

print("Thank you for playing!!")


