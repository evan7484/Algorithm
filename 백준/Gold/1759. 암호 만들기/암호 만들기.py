from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')

L,C = map(int,input().split())
word = list(map(str,input().split()))

word.sort()
for password in combinations(word,L):
  count = 0
  for i in password: 
    if i in vowels:
      count += 1
  if count >= 1 and count <= L - 2:
    print(''.join(password))
