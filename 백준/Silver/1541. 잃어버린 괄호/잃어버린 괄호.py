# 백준 1541번 잃어버린 괄호
# -면 넘어가고 +만 먼저 계산후 -를 계산하면 될듯

num = ['0','1','2','3','4','5','6','7','8','9']
operator = ['+','-']
start = list(map(str,input()))
formulanum = []
formula = []
j = 0
number = 1

for i in range(len(start)):
  if start[i] in operator:
    s = ''.join(formulanum)
    formulanum.clear()
    formula.append(int(s))
    formula.append(start[i])
  elif start[i] in num:
    formulanum.append(start[i])
s = ''.join(formulanum)
formulanum.clear()
formula.append(int(s))

while j != number:
  if formula[j] == '+':
    n2 = formula.pop(j+1)
    formula.pop(j)
    n1 =  formula.pop(j-1)
    n = n1+n2
    formula.insert(j-1,n)
    j -= 1
  j += 1
  number = len(formula)
j = 0
number = 1
while j != number:
  if formula[j] == '-':
    n2 = formula.pop(j+1)
    formula.pop(j)
    n1 =  formula.pop(j-1)
    n = n1-n2
    formula.insert(j-1,n)
    j -= 1
  j += 1
  number = len(formula)

print(formula[0])