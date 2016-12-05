file = open('input.txt', 'r')

valid_triangles=0

triangles = (list(),list(),list())

def check(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        return True
    return False

with file as f:
    lines = f.readlines()


for line in lines:
    a = int(line[:5])
    b = int(line[6:10])
    c = int(line[11:])

    triangles[0].append(a)
    triangles[1].append(b)
    triangles[2].append(c)

for i in range (0,len(triangles[0])/3):
    for j in range (0,3):
        a = triangles[j][3*i]
        b = triangles[j][3*i+1]
        c = triangles[j][3*i+2]
        if check(a,b,c):
            valid_triangles += 1

print ("There are {} valid triangles".format(valid_triangles))
