# Your solution to Exercise 13
numbers = input()
lst = list(map(int, numbers.split()))
total = 0
for x in lst:
    total += x
mean = total / len(lst)
print(f"{mean:.2f}")
