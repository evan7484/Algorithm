#25501번 재귀의 귀재
n = [0]
def recursion(s,l,r):
  n[0] += 1
  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    return recursion(s,l+1,r-1)

def isPalindrome(s):
  return recursion(s,0,len(s)-1)

T = int(input())
result1 = []
result2 = []
for i in range(T):
  S = input()
  result1.append(isPalindrome(S))
  result2.append(n[0])
  n = [0]

for i in range(T):
  print(result1[i],result2[i])
