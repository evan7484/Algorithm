N ,M = map(int,input().split())
pokemonName = {}
pokemonNum = {}

for i in range(N):
  pokemonname = input()
  pokemonName[pokemonname] = i+1
  pokemonNum[i+1] = pokemonname 
  
for i in range(M):
  pokemontest = input()
  try:
    pokemontest = int(pokemontest)
    print(pokemonNum[pokemontest])
  except:
    print(pokemonName[pokemontest])
    
