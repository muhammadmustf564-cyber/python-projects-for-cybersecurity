import random

correctguess = random.randint(1,100)
gameover = False
count = 0

while gameover == False:
    count += 1

    # take a guess from a player
    playerguess = int(input("Guess a number between 1 and 100: "))
    
    if playerguess == correctguess:
        print("Correct! You Win")
        gameover = True
    elif playerguess > correctguess:
        print("Too high, Try another guess")
    else:
        print("Too Low, Try another guess")
   
print(f"You guessed in {count} attempts")