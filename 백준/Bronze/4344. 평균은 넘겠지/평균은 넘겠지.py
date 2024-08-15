num = int(input())
sum = 0
n = 0
for i in range(num):
  grade = list(map(int,input().split()))
  student = grade[0]
  del grade[0]
  for j in range(student):
    sum += grade[j]
  m = sum/student

  for i in range(student):
    if grade[i] > m:
      n +=1
  print("{:.3f}%".format(n/student*100))
  student = 0; sum = 0; n = 0; m = 0;
  