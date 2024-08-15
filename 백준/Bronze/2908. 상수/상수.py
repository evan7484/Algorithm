A,B = map(list,input().split())

A.reverse()
B.reverse()

a = int(A[0])*100 + int(A[1])*10 + int(A[2])
b = int(B[0])*100 + int(B[1])*10 + int(B[2])

if a > b:
  print(a)
else:
  print(b)
