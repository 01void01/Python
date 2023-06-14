number = 20
print("Welcome, To the guessing game.\nDeveloper: Ankit Sharma\n")
instructions = "Instruction:\nYou have to guess the no. between 1 to 50. You will get only 10 chances.\n "
print(instructions)
print("10 guesses left\n")
no_of_guess = 1
while no_of_guess <= 10:
    inp = int(input("Guess the numbers: "))
    if inp < number:
        print("Your number is smaller, try a greater number\n ")
    elif inp > number:
        print("Your number is greater, try a smaller one\n ")
    else:
        print("Your guess is correct, Congratulations!!\n ")
        print("You finished the game in", no_of_guess, "tries.")
        break
    print(10 - no_of_guess, "guesses left\n")
    no_of_guess = no_of_guess + 1
    if no_of_guess > 10:
        print(11 - no_of_guess, "guesses left. BETTER LUCK NEXT TIME :_(")
