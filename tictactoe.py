from dis import dis
from pydoc import cli
from graphics import *

TOP_LEFT_MIDPOINT = Point(100, 100)
TOP_MIDDLE_MIDPOINT = Point(300, 100)
TOP_RIGHT_MIDPOINT = Point(500, 100)

MIDDLE_LEFT_MIDPOINT = Point(100, 300)
MIDDLE_MIDDLE_MIDPOINT = Point(300, 300)
MIDDLE_RIGHT_MIDPOINT = Point(500, 300)

BOTTOM_LEFT_MIDPOINT = Point(100, 500)
BOTTOM_MIDDLE_MIDPOINT = Point(300, 500)
BOTTOM_RIGHT_MIDPOINT = Point(500, 500)

CIRCLE_RADIUS = 50

def main():
    win = setup()
    play(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def setup():
    win = GraphWin("Tic Tac Toe", 600, 600)

    l1 = Line(Point(200, 0), Point(200, 600))
    l1.draw(win)

    l2 = Line(Point(400, 0), Point(400, 600))
    l2.draw(win)

    l3 = Line(Point(0, 200), Point(600, 200))
    l3.draw(win)

    l4 = Line(Point(0, 400), Point(600, 400))
    l4.draw(win)

    return win

def play(win: GraphWin):
    player = "X"
    turns_played = 0
    board = [["NONE" for i in range(3)] for j in range(3)]

    while turns_played < 9:
        print("starting turn")
        clicked = win.getMouse()
        x = clicked.getX()
        y = clicked.getY()

        if x <= 200 and y <= 200:
            board[0][0] = player
            draw(player, TOP_LEFT_MIDPOINT, win)
        elif x > 200 and x <= 400 and y <= 200:
            board[0][1] = player
            draw(player, TOP_MIDDLE_MIDPOINT, win)
        elif x > 400 and y <= 200:
            board[0][2] = player
            draw(player, TOP_RIGHT_MIDPOINT, win)
        elif x <= 200 and y > 200 and y <= 400:
            board[1][0] = player
            draw(player, MIDDLE_LEFT_MIDPOINT, win)
        elif x > 200 and x <= 400 and y > 200 and y <= 400:
            board[1][1] = player
            draw(player, MIDDLE_MIDDLE_MIDPOINT, win)
        elif x > 400 and y > 200 and y <= 400:
            board[1][2] = player
            draw(player, MIDDLE_RIGHT_MIDPOINT, win)
        elif x <= 200 and y > 400:
            board[2][0] = player
            draw(player, BOTTOM_LEFT_MIDPOINT, win)
        elif x > 200 and x <= 400 and y > 400:
            board[2][1] = player
            draw(player, BOTTOM_MIDDLE_MIDPOINT, win)
        elif x > 400 and y > 400:
            board[2][2] = player
            draw(player, BOTTOM_RIGHT_MIDPOINT, win)

        if check_win(board):
            disp = Text(Point(300, 300), player + " Wins!")
            disp.draw(win)
            return

        turns_played += 1
        if player == "X":
            player = "O"
        else:
            player = "X"

    disp = Text(Point(300, 300), "Tie!")
    disp.draw(win)

def check_win(board):
    print(board)
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "NONE":
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != "NONE":
            return True

    return board[0][0] == board[1][1] == board[2][2] != "NONE" or board[0][2] == board[1][1] == board[2][0] != "NONE"

def draw(player, point: Point, win: GraphWin):
    if player == "O":
        c = Circle(point, CIRCLE_RADIUS)
        c.draw(win)
    else:
        x = point.getX()
        y = point.getY()

        l1 = Line(Point(x + 50, y + 50), Point(x - 50, y - 50))
        l1.draw(win)

        l2 = Line(Point(x + 50, y - 50), Point(x - 50, y + 50))
        l2.draw(win)

main()