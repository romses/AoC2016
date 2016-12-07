file = open('input.txt', 'r')

valid = 0
sum = 0

def check(part):
   for i in range(0,len(part)-3):
      if part[i]==part[i+3] and part[i+1]==part[i+2] and part[i] != part[i+1]:
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
         positive.append(check(fragments[i]))
      else:
         negative.append(check(fragments[i]))
   
   if (True in positive) and (True not in negative):
      sum +=1

print "There are {} IPv7 addresses, which supports TLS".format(sum)
