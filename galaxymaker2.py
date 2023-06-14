# Goal for this page. I want to change up the galaxy so that it could be viewed two-dimensionally
# Each star will recieve coordinates, and each star surrounding it will be marked as a travel option
# combined_codes = []
# length_of_octagon_sides = 12
# height = 0
#
# # while True:
# starting_x = length_of_octagon_sides / 2 * 3/2
# starting_y = length_of_octagon_sides / 2 * -1
# curren_x = starting_x
# curren_y = starting_y
#
from turtle import Turtle, Screen

t = Turtle()
s = Screen()
for x in range(0, 9):
    t.forward(100)
    t.right(45)


s.exitonclick()