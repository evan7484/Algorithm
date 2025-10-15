# 10845번

queue = []
result = []

N = int(input())

for i in range(N):
    x = 1
    command = list(map(str,input().split()))
    if command[0] == "push":
        x = int(command[1])
        queue.append(x)
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif len(queue) == 0:
        result.append(-1)
    elif command[0] == "pop":
        result.append(queue[0])
        del queue[0]
    elif command[0] == "front":
        result.append(queue[0])
    elif command[0] == "back":
        result.append(queue[-1])


for i in result:
    print(i)
