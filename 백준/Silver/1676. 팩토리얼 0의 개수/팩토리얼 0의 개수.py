#1676번

n = int(input())
num = 1
for i in range(1, n+1):
    num *= i

num_arr = str(num)
num_arr = list(num_arr)
num_arr.reverse()

result = 0
for i in num_arr:
    if i == "0":
        result += 1
    else:
        break
print(result)