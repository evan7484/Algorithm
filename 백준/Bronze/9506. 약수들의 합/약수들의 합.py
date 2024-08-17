def divisor(number): # number : 16
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(number//i)
        		# [1, 16, 2, 8, 4]
    result.sort() 
        		# [1, 2, 4, 8, 16]
    return result 

n = 0
nn = []
result = []
while n != -1:
  n = int(input())
  nn.append(n)

for i in range(len(nn)-1):
  result = divisor(nn[i])
  result.remove(nn[i])
  if sum(result) == nn[i]:
    print(nn[i],'= ',end = '')
    for j in range(len(result)):
      if j == len(result)-1:
        print(result[j])
      else:
        print(result[j],'+ ',end = '')
  else:
    print(nn[i],'is NOT perfect.')