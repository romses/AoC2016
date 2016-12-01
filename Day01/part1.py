#!/usr/bin/python



file = open('input.txt', 'r')

old_direction = "N"

turn = {("N","L"):"W",
        ("N","R"):"O",
        ("W","L"):"S",
        ("W","R"):"N",
        ("O","L"):"N",
        ("O","R"):"S",
        ("S","L"):"O",
        ("S","R"):"W"}

pos_x=0
pos_y=0

with open('input.txt') as f:
   line = f.readlines()

steps = line[0].strip().split(",")

for step in steps:
   step=step.strip()
   direction = turn[old_direction,step[0]]
   many = int(step[1:])

   if direction == "N":
      pos_y = pos_y + many
   if direction == "S":
      pos_y = pos_y - many
   if direction == "O":
      pos_x = pos_x + many
   if direction == "W":
      pos_x = pos_x - many
  
#   print old_direction,"=>", step, direction, many
   old_direction = direction

print "The rabbits location is {} steps ahead".format(abs(pos_x)+abs(pos_y))
