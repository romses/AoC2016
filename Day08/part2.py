file = open('input.txt', 'r')

display=[[" " for x in range(50)] for i in range(6)]

count=0

def execute(line):
   line=line.strip()
   tokens = line.split()
   if tokens[0] == "rotate": 
      dir = line[7]
      if tokens[1]=="row":
         row = int(tokens[2].split('=')[1])
         amount = int(tokens[4])
         tmp = display[row][-amount:] + display[row][:len(display[row])-amount]
         display[row]=tmp

      if tokens[1]=="column":
         col = int(tokens[2].split('=')[1])
         carry = display[0][col]
         amount = int(tokens[4])

         for r in range(amount):
            tmp = display[5][col]
            i=4
            while i>=0:
               display[i+1][col]=display[i][col]
               i-=1
            display[0][col]=tmp


   if tokens[0]=="rect":
      A,B = tokens[1].split("x")
      for a in range(int(A)):
         for b in range(int(B)):
            display[b][a]="*"

with file as f:
   lines = f.readlines()

for line in lines:
   execute(line)


for line in display:
   for pos in line:
      if pos == "*":
         count +=1

for i in display:
   print " ".join(i)
