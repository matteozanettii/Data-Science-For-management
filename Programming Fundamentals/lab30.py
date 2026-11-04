from random import randint


def banner():
    # define the colors for the banner... (searched the color palette online)
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m' 

    # creating the banner for the game...
    banner = f"""
    {CYAN}
      ____ _   _ _____ ____ ____  
     / ___| | | | ____/ ___/ ___| 
    | |  _| | | |  _| \___ \___ \ 
    | |_| | |_| | |___ ___) |__) |
     \____|\___/|_____|____/____/ 
    {RESET}
           {YELLOW}THE NUMBER{RESET}
    ---------------------------------
    """
    return banner


def gamemainv1():
    maxnum = 10
    secret_number = randint(1,maxnum)
    print(f"\033[96m I selected a number between 1 and {maxnum} ... try to guess which one  \033[0m")
    while True:
        n=int(input(">"))
        if n == secret_number:
            print(f"\033[92m You Win! \033[0m")
            return ""
            
        print("Wrong...")

def gamemainv2():
    maxnum = 10
    secret_number = randint(1,maxnum)
    print(f"\033[96m I selected a number between 1 and {maxnum} ... try to guess which one  \033[0m")
    while True:
        n=input(">")
        
        if n == "ABAABBBA":
            print(f"\033[92m The secret number is {secret_number} \033[0m")
            print(f"\033[91m GAME OVER. \033[0m")
            return ""
        if int(n) == secret_number:
                    print(f"\033[92m You Win! \033[0m")
                    return ""
        print("Wrong...")

def gamemainv3():
    maxnum = 10
    attemptsRemaining = 5
    secret_number = randint(1,maxnum)
    print(f"\033[96m I selected a number between 1 and {maxnum} ... try to guess which one  \033[0m")
    while True:
        n=input(">")
        
        if n == "ABAABBBA":
            print(f"\033[92m The secret number is {secret_number} \033[0m")
            print(f"\033[91m GAME OVER. \033[0m")
            return ""
        if int(n) == secret_number:
                    print(f"\033[92m You Win! \033[0m")
                    return ""
        if attemptsRemaining == 1:
            print(f"\033[92m The secret number is {secret_number} \033[0m")
            print(f"\033[91m GAME OVER. \033[0m")
            return ""
        attemptsRemaining -= 1
        print("Wrong...")
        print("{} attempts left".format(attemptsRemaining))

def gamemainv4():
    #starting variables
    maxnum = 10
    attemptsRemaining = 5
    #following the scoring system from the assignment
    score = 0
    secret_number = randint(1,maxnum)
    
    #\033[96m is a formatting code (cyan) in this case, not mandatory but I would like to experiment it 
    #also now I just remade all the versions by copy pasting, but it would be better to assing colors to a variable
    #in order in the future to change them easily, but in the way I did formatting versions of the game
    #in different functions, I would have to change all of them, so I will leave it like this for now

    print(f"\033[96m I selected a number between 1 and {maxnum} ... try to guess which one  \033[0m")
    while True:
        n=input(">")
        if n == "ABBAAAAA":
                    print(f"\033[92m Restarting the game... \033[0m")
                    #maybe can be risky, but since is a return, it will exit the current function and start a new one, so the score will be reset to 0 and a new number will be generated 
                    return gamemainv4()
                    
                    
        if n == "ABAABBBA":
            print(f"\033[92m The secret number is {secret_number} \033[0m")
            print(f"\033[91m GAME OVER. \033[0m")
            score=score -5
            print(f"\033[92m Your score is {score} \033[0m")
            #clean return, we will see more return like this in the code for better clean
            return ""
        if int(n) == secret_number:
                    print(f"\033[92m You Win! \033[0m")
                    score+=7
                    print(f"\033[92m Your score is {score} \033[0m")
                    return ""
        #making this isequal because python starts from 0!
        if attemptsRemaining == 1:
            print(f"\033[92m The secret number is {secret_number} \033[0m")
            print(f"\033[91m GAME OVER. \033[0m")
            #adding the scoring also here, otherwise this count will be skipped
            score-=1
            print(f"\033[92m Your score is {score} \033[0m")
            return ""
        #as we can see no else needed because all if were passed at this point
        attemptsRemaining -= 1
        score-=1
        print("Wrong...")
        print("{} attempts left".format(attemptsRemaining))




#using by default the latest version of the game
print(banner())
print(gamemainv4())
