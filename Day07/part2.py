file = open('input.txt', 'r')

valid = 0
sum = 0

def check(pos,neg):
   tmp = ""
   for p in pos:
      tmp += "|"+p
   pos = tmp

   tmp = ""
   for n in neg:
      tmp += "|"+n
   neg = tmp

   for a in range(ord('a'),ord('z')+1):
      for b in range(ord('a'),ord('z')+1):
         aba = chr(a)+chr(b)+chr(a)
         bab = chr(b)+chr(a)+chr(b)
         if aba in pos and bab in neg:
            return True
   return False

with file as f:
   lines = f.readlines()


for line in lines:
   line=line.strip()
   line = line.replace('[','|')
   line = line.replace(']','|')
   fragments = line.split("|")

   positive = list()
   negative = list()

   for i in range(0,len(fragments)):
      if i%2 == 0:
         positive.append(fragments[i])
      else:
         negative.append(fragments[i])

   if check(positive,negative):
      sum +=1

print "There are {} IPv7 addresses, which supports SSL".format(sum)
