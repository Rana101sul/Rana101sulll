from random import randint
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
#set humanplayer to False
humanplayer = False
while humanplayer == False:
    #set humanplayer to True
    humanplayer = input("Rock, Paper, Scissors?")
    #assign a random play to the randomplayer
    randomplayer = t[randint(0,2)]
    if humanplayer == randomplayer:
        print(f"humanplayer played {humanplayer}, Randomplayer played {randomplayer}")
        print("Tie!")        
    elif humanplayer == "Rock":
        print(f"humanplayer played {humanplayer}, Randomplayer played {randomplayer}")
        if randomplayer == "Paper":
            print("You lose!", randomplayer, "covers", humanplayer)
        else:
            print("You win!", humanplayer, "smashes", randomplayer)
    elif humanplayer == "Paper":
        print(f"humanplayer played {humanplayer}, Randomplayer played {randomplayer}")
        if randomplayer == "Scissors":
            print("You lose!", randomplayer, "cut", humanplayer)
        else:
            print("You win!", humanplayer, "covers", randomplayer)
    elif humanplayer == "Scissors":
        print(f"humanplayer played {humanplayer}, Randomplayer played {randomplayer}")
        if randomplayer == "Rock":
            print("You lose...", randomplayer, "smashes", humanplayer)
        else:
            print("You win!", humanplayer, "cut", randomplayer)
    else:
        print(f"humanplayer played {humanplayer}, Randomplayer played {randomplayer}")
        print("That's not a valid play. Check your spelling!")
    #humanplayer was set to True, but we want it to be False so the loop continues
    humanplayer = False