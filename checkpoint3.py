guess = input("Enter a guess: ")

length = len(guess)
if length < 5:
    print("Your guess was too few letters. Your word was " + str(length) + " letters in length. Try again and guess a 5 letter word.")
elif length > 5:
    print("Your guess was too many letters. Your word was " + str(length) + " letters in length. Try again and guess a 5 letter word.")
elif guess == "proxy":
    print("Congrats you won!")
else:
    print("That's not right. Guess again.")