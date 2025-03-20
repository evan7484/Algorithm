import sys
sys.setrecursionlimit(10 ** 5)

def dfs(start_node):
    global cnt
    visited[start_node] = cnt
    graph[start_node].sort(reverse = True)
    for i in graph[start_node]:
      if visited[i] == 0:
        cnt += 1
        dfs(i)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1
for i in range(m):
  a,b = map(int,input().split())

  graph[a].append(b)
  graph[b].append(a)

dfs(r)
for i in range(1, n+1):
  print(visited[i])