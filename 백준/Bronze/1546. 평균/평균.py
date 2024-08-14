subject_N = int(input())
i = 0
sum = 0
list2 = []
grade = list(map(int,input().split()))


grade.sort()
M = grade[-1]
for i in range(subject_N):
  list2.append(float(grade[i])/M*100)

for i in range(len(list2)):
  sum += list2[i]

Average = sum/subject_N

print(Average)



