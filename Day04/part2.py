file = open('input.txt', 'r')

sectors=0

def decrypt(room,rounds):
   for i in range(0,rounds):
      decr=''
      for c in room:
         if c == "z":
            decr+="a"
         else:
            if c!="-":
               decr+=chr(ord(c)+1)
            else:
               decr+=c
      room=decr
   return room

def check(room):
   data=[]

   for i in range(0,len(room)):
      if room[i]=='[':
         checksum_start=i+1
      if room[i]==']':
         checksum_end=i
      if room[i]=='-':
         sec_start=i+1

   checksum=room[checksum_start:checksum_end]
   checksum2=""
   sector  =int(room[sec_start:checksum_start-1])
   roomname=room[0:sec_start-1]
   roomname=roomname.replace('-','')
   room=room[0:sec_start-1]

   letter_count = list({(char, roomname.count(char)) for char in roomname})
   letter_count.sort(key=lambda x: (-x[1], x[0]))  # sort by count, letter

   for k,v in letter_count:
      checksum2+=k

   if checksum2[0:5] == checksum:
      if "northpole" in decrypt(roomname,sector):
         print("The northpole-object-storage is located in sector {}".format(sector))

with file as f:
   lines = f.readlines()


for line in lines:
   line=line.strip()
   check(line)
