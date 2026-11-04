#could do a check but this time I trust the user
n = int(input("Enter a number: "))
#starting the loop to print the pattern

#because we start from 0, we fixed the range to start from 1 and go to n + 1
for i in range(1, n + 1):
    #left part: starting from 1 and stopping at i , NOT i +1, the stop does not include the last number, so we need to add 1 to it
    left = "".join(str(x) for x in range(1, i + 1))
    #right part: starting from i - 1 and stopping at 0 (stopping same as above), with a step of -1
    right = "".join(str(x) for x in range(i - 1, 0, -1))
    #using the hint from the slides, using as "spacing" limiter, the number of user, fixed to -1 and doubled because are the lenght of both parts of the pyramid 

    #noticing also " |" in the slides, fixed with the same space
    print((left + right ).center(2 * n - 1) + " |")
