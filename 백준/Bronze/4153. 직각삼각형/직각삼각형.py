# 4153번

a,b,c = 1,1,1
result = []
while a != 0 and b != 0 and c != 0:
    a,b,c = map(int,input().split())
    triangle = []
    triangle.append(a)
    triangle.append(b)
    triangle.append(c)
    triangle.sort()

    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        result.append("right")
    else:
        result.append("wrong")

for i in range(len(result)-1):
    print(result[i])