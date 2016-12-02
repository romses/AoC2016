file = open('input.txt', 'r')

x_pos=1
y_pos=1

keypad = {(0,0):1,(0,1):2,(0,2):3,
          (1,0):4,(1,1):5,(1,2):6,
          (2,0):7,(2,1):8,(2,2):9}

print "The Door code is :"

while 1:
   char = file.read(1)
   if not char: break
#   print x_pos,y_pos,keypad[(y_pos,x_pos)]
   if char == '\n': print keypad[(y_pos,x_pos)]
   if char == "U": y_pos=max(0,y_pos-1)
   if char == "D": y_pos=min(2,y_pos+1)
   if char == "L": x_pos=max(0,x_pos-1)
   if char == "R": x_pos=min(2,x_pos+1)
