file = open('input.txt', 'r')

char={}

def topchar(chars):
   char=""
   count=0

   for k in chars:
      if chars[k]>count:
         count=chars[k]
         char=k
#      print k, chars[k],char,count
   return char

with file as f:
   lines = f.readlines()


for line in lines:
   line=line.strip()
   for i in range(0,8):
      if i not in char:
         char[i]={} 
      if line[i] not in char[i]:
         char[i][line[i]]=0
      char[i][line[i]]+=1


#print char

msg=""

for i in range(0,8):
   msg += topchar(char[i])

print "The message was {}".format(msg)
