chances = 1
secret_number = 9
limit=3
while chances<=limit:
    guess=int(input("Guess the number: "))
    chances+=1
    if guess == secret_number:
        print("Correct guess")
        break #even after correct guess loop will continue to break that
    #else:
    #    print("Try again")
else:
    print("Sorry you failed")