guess = input("What's your guess? ")

length = len(guess)
if length < 5:
    print("Your guess was too few letters. Your word was " + str(length) + " letters in length. Try again and guess a 5 letter word.")
elif length > 5:
    print("Your guess was too many letters. Your word was " + str(length) + " letters in length. Try again and guess a 5 letter word.")
else:
    print(guess)