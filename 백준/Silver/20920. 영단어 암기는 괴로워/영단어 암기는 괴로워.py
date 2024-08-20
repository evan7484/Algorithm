#백준 20920번 영단어 암기는 괴로워
#단어를 문자열로 입력받고 개수를 세서 M을 넘는 단어만 단어장 리스트에 넣는다
#딕셔너리로 단어와 그에 나오는 횟수를 연결해준다
#그리고 횟수가 같은 것들끼리 길이를 비교
#그리고 그것마저 같은 것들끼리 사전순 비교

N,M = map(int,input().split())
number = {}
for i in range(N):
  word = input()
  if len(word) < M:
    continue

  if word in number:
    number[word] += 1
  else:
    number[word] = 1

number = sorted(number.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in number:
    print(i[0])