a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

fn = a1*n0 + a0
if fn <= c*n0 and a1<=c: #a1이 c 보다 크다면 a0가 음수일 때 n0가 계속 커질 때 결국 fn이 더 큰값이 될 수 밖에 없기 때문에 조건을 추가해줘야함. 
  print(1)
else:
  print(0)