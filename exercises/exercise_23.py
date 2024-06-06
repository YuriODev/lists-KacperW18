# Your solution to Exercise 23
numbers = input()
lst = list(map(int, numbers.split()))
lst = reversed(sorted(lst))
print("".join(map(str, lst)))
