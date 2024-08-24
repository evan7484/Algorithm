total = []
sum_time = 0.0
sum = 0

for i in range(20):
  name, time, score = map(str, input().split())
  if score == 'A+':
    score = '4.5'
  elif score == 'A0':
    score = '4.0'
  elif score == 'B+':
    score = '3.5'
  elif score == 'B0':
    score = '3.0'
  elif score == 'C+':
    score = '2.5'
  elif score == 'C0':
    score = '2.0'
  elif score == 'D+':
    score = '1.5'
  elif score == 'D0':
    score = '1.0'
  elif score == 'F':
    score = '0.0'
  elif score == 'P':
    continue
  sum_time += float(time)
  total.append(float(time)*float(score))

for i in range(len(total)):
  sum += total[i]

print(sum/sum_time)
