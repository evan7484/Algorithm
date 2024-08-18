#부분 문자열 다 구하고 중복 제거해서 개수 출력하면 될듯
#부분 문자열을 어떻게 구하는지가 젤 문제였네 
#set선언해서 1부터 쭉 늘려나가면서  다 구하기

S = input()
cnt = set()
n = len(S)
for i in range(n):
  for j in range(i+1,n+1):
    cnt.add(S[i:j])

print(len(cnt))