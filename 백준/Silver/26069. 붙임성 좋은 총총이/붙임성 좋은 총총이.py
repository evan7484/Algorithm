#붙임성 좋은 총총이 ~ 무지개 춤
#처음 총총이와 만나는 사람을 춤추는 인원에 넣는다
#춤추는 리스트에 들어간 인원이 그 후에 다른 인원과 만나게 된다면 그 인원도 춤추는 리스트에 넣는다
#리스트의 개수를 출력한다

N = int(input())
Dance = ['ChongChong']
for i in range(N):
  meet = list(map(str,input().split()))
  if meet[0] in Dance:
    Dance.append(meet[1])
  elif meet[1] in Dance:
    Dance.append(meet[0])

Dance = set(Dance)
Dance = list(Dance)
print(len(Dance))