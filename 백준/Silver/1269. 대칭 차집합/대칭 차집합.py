#리스트로 해봐도 될듯? - > 중복제거로 딕셔너리 사용(dict.fromkeys())
#생각해보니 A에서 B 빼고 B에서 A를 빼는거라서 서로 같은 숫자를 절대 한 리스트에 추가할 수 가 없음 \ㅋㅋ
#1. 시간초과 -> 리스트로만 한게 문제인듯 정확히는 모르겟고

An,Bn = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
results = []
A = dict.fromkeys(A)
B = dict.fromkeys(B)

for i in B:
  if i not in A:
    results.append(i)
for i in A:
  if i not in B:
    results.append(i)

print(len(results))