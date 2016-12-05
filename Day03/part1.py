file = open('input.txt', 'r')

valid_triangles=0

with file as f:
    lines = f.readlines()


for line in lines:
    a = int(line[:5])
    b = int(line[6:10])
    c = int(line[11:])

    if ((a + b) > c) and ((b + c) > a) and ((a + c) >b):
        valid_triangles +=1


print ("There are {} valid triangles".format(valid_triangles))
