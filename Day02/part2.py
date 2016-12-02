file = open('input.txt', 'r')

x_pos=0
y_pos=2

keypad = {
(0,0):-1,(0,1):-1 ,(0,2):1  ,(0,3):-1 ,(0,4):-1,
(1,0):-1,(1,1):2  ,(1,2):3  ,(1,3):4  ,(1,4):-1,
(2,0):5 ,(2,1):6  ,(2,2):7  ,(2,3):8  ,(2,4):9,
(3,0):-1,(3,1):'A',(3,2):'B',(3,3):'C',(3,4):-1,
(4,0):-1,(4,1):-1 ,(4,2):'D',(4,3):-1 ,(4,4):-1,
}

print "The Door code is :"

while 1:
   char = file.read(1)
   if not char: break
#   print x_pos,y_pos,keypad[(y_pos,x_pos)]
   if char == '\n': print keypad[(y_pos,x_pos)]
   if char == "U": 
      if ((y_pos-1,x_pos) in keypad) and keypad[(y_pos-1,x_pos)] != -1:
         y_pos=max(0,y_pos-1)
   if char == "D":
      if ((y_pos+1,x_pos) in keypad) and keypad[(y_pos+1,x_pos)] != -1:
         y_pos=min(4,y_pos+1)
   if char == "L":
      if ((y_pos,x_pos-1) in keypad) and keypad[(y_pos,x_pos-1)] != -1:
         x_pos=max(0,x_pos-1)
   if char == "R":
      if ((y_pos,x_pos+1) in keypad) and keypad[(y_pos,x_pos+1)] != -1:
         x_pos=min(4,x_pos+1)
