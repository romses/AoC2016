import md5

base="wtnhxymk"
hash="xxxxx99"
round=0
password=[False,False,False,False,False,False,False,False]

while False in password:
   m = md5.new(base+str(round))
   hash=m.hexdigest()
   round +=1
   if hash[5]>='0' and hash[5]<'8' and hash.startswith("00000"):
      if password[int(hash[5])]==False:
         password[int(hash[5])]=hash[6]

   hash = "xxxxx99"

print "The Password is {}".format( password)
