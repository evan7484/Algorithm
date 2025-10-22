# 28702번

FizzBuzz = []
num = 0
result = ""

for i in range(3):
    num = input()
    FizzBuzz.append(num)

for i in range(3):
    if FizzBuzz[i] != "FizzBuzz" and FizzBuzz[i] != "Buzz" and FizzBuzz[i] != "Fizz":
        num = int(FizzBuzz[i])+3-i
        break

if num%3 == 0:
    result = "Fizz"
if num%5 == 0:
    result = "Buzz"
if num%15 == 0:
    result = "FizzBuzz"
if result == "":
    result = num

print(result)