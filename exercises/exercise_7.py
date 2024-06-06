# Your solution to Exercise 7
numbers = input()
lst = list(map(int, numbers.split()))
total = 0
for x in lst:
    total += x
print(total)