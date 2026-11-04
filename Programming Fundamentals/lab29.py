gamers = ["Anna", "Luca", "Marco", "Sofia", "John"]
scores = [28, 30, 25, 27, 33]

#creating a list of tuples containing scores and corresponding gamers using zip function
gamer_scores = sorted(zip(scores, gamers))
#using reverse to sort the list in descending order
gamer_scores.reverse()

#this time I decided not to use try and except, also for praticing for the real function
#provided in the course, but also to make the code leaner, mode readable, simplier and better

#with while true, i create an asking loop valid until the user inputs a valid number
while True:
   
    n = int(input("Enter the number of top gamers to display: "))
    if n < 0 or n > len(gamer_scores):
        #learned from previus lessons, for better compatility, I used f-string to print the message, instead of static number
        print(f"Please enter a valid number between 0 and {len(gamer_scores)}.")
        #exiting said as above, the program will simply stop
        break
    else:
        for score, gamer in gamer_scores[:n]:
            print(f"{gamer}: {score}")
    
