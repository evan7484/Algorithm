s = list(map(str,input()))
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = 0
numA = []

for i in range(26):
  if alphabet[i] in s:
    n = s.index(alphabet[i])
    alphabet.insert(i,n)
    del alphabet[i+1]
  else: 
    alphabet.insert(i,-1)
    del alphabet[i+1]

for i in alphabet:
  print(i,end = ' ')
    

