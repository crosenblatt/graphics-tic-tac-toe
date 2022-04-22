guess = input("Enter a guess: ")

length = len(guess)
if length < 5:
    print("too short")
elif length > 5:
    print("too long")
else:
    print(guess)