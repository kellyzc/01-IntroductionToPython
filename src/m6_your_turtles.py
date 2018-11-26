"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zach Kelly.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.tracer(10)

turtle1 = rg.SimpleTurtle()
turtle2 = rg.SimpleTurtle()
turtle1.pen = rg.Pen("red", 2)
turtle2.pen = rg.Pen("gray", 2)

for i in range(300):
    turtle1.forward(int(i / 10))
    turtle1.left(10)

for a in range(10):
    for b in range(15):
        turtle2.draw_circle(10)
        turtle2.forward(20)
        turtle2.left(b * 10)
        turtle2.forward(20)
    turtle2.go_to(rg.Point(0, 0))
    turtle2.set_heading(45 * a)


window.close_on_mouse_click()