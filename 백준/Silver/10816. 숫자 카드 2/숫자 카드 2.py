N = int(input())
card = list(map(int,input().split()))
M = int(input())
example = list(map(int,input().split()))

dic = {}
for i in range(len(card)):
  dic[card[i]] = 0

for i in range(len(card)):
  if card[i] in dic:
    dic[card[i]] += 1

for i in range(M):
  if example[i] not in dic:
    print(0, end = ' ')
  else:
    print(dic[example[i]], end = ' ')

# 1. 중복되는 숫자가 있을때 개수를 세서 value에 넣는 방법
# 2. 리스트에 없는 숫자가 있을때 0을 출력하기