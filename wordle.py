from typing import List
from graphics import *

def main():
    win = WordleWin()
    guesses = win.setupGuesses()
    target = "proxy"
    play(target, win, guesses)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def play(target: str, win: WordleWin, guesses: List[Guess]):
    tries = 0
    while tries < 6:
        click = win.getMouse()
        if click.isSubmitClick():
            correct = 0
            for letter_index in range(5):
                letter = guesses[tries].getLetter(letter_index)
                index = target.find(letter.getText())
                if index == letter_index:
                    letter.setFill("GREEN")
                    correct += 1
                elif index != -1:
                    letter.setFill("YELLOW")
                else:
                    letter.setFill("DARKGRAY")
            if correct == 5:
                win.drawWinText()
                break
            else:
                tries += 1
    if tries == 6:
        win.drawLoseText()

main()