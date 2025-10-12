#2920번

play = list(map(int,input().split()))
diff = []
for i in range(7):
    diff.append(play[i+1] - play[i])

if diff.count(1) == 7:
    print("ascending")
elif diff.count(-1) == 7:
    print("descending")
else:
    print("mixed")



