dot = list(map(int,input().split()))

width = dot[2] - dot[0]
height = dot[3] - dot[1]

if dot[0] < dot[1]:
    small = dot[0]
else:
    small = dot[1]
    

if width < height and width < small:
    print(width)
elif small < width and small < height:
    print(small)
else:
    print(height)