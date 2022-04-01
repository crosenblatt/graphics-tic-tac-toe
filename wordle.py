from mimetypes import guess_extension
from re import sub
from typing import List
from graphics import *

class Guess:
    def __init__(self, win, y):
        self.letters = [Entry(Point(100 + x, y), 1) for x in range(100, 200, 20)]

        for letter in self.letters:
            letter.draw(win)

def main():
    win = setup_win()
    guesses = setup_guesses(win)
    target = "proxy"
    play(target, win, guesses)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def setup_win():
    win = GraphWin("Wordle", 500, 500)
    submit_button = Rectangle(Point(280, 280), Point(320, 320))
    submit_button.setFill("GRAY")
    submit_button.draw(win)

    submit_text = Text(Point(300, 300), "Submit")
    submit_text.draw(win)
    return win

def setup_guesses(win):
    return [Guess(win, y) for y in range(100, 220, 20)]

def play(target: str, win: GraphWin, guesses: List[Guess]):
    tries = 0
    while tries < 6:
        click = win.getMouse()
        if 280 <= click.getX() <= 320 and 280 <= click.getY() <= 320:
            correct = 0
            for letter_index in range(5):
                letter = guesses[tries].letters[letter_index]
                index = target.find(letter.getText())
                print(target + ".find(" + letter.getText() + ") = " + str(index))
                if index == letter_index:
                    letter.setFill("GREEN")
                    print("green")
                    correct += 1
                elif index != -1:
                    letter.setFill("YELLOW")
                    print("yellow")
                else:
                    letter.setFill("DARKGRAY")
                    print("no color")
            if correct == 5:
                win_text = Text(Point(350, 350), "You win!")
                win_text.draw(win)
                break
            else:
                tries += 1
    if tries == 6:
       lose_text = Text(Point(350, 350), "You lose!")
       lose_text.draw(win) 

main()