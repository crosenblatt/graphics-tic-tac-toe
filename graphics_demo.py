from graphics import *

win = GraphWin("Demo", 400, 400)
c = Circle(Point(50, 50), 10)
r = Rectangle(Point(100, 100), Point(300, 300))
t = Text(Point(200, 200), "Hello World!")
c.draw(win)
r.draw(win)
t.draw(win)
win.getMouse()
win.close()