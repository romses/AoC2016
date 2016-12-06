import md5

base="wtnhxymk"
hash="xxxxx"
round=0
password=""


for i in range(0,8):
   while True:
      m = md5.new(base+str(round))
      hash=m.hexdigest()
      round +=1
      if hash.startswith('00000'):
         break

   password+=hash[5]

print "The Password is {}".format( password)
