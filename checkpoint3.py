guess = input("Enter a guess: ")

length = len(guess)
if length < 5:
    print("too short")
elif length > 5:
    print("too long")
elif guess == "laila":
    print(guess + " correct!")
else:
    print(guess + " incorrect")