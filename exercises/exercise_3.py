# Your solution to Exercise 3

numbers = input()
lst = list(map(int, numbers.split()))
lst = [lst[x] for x in range(len(lst)) if lst[x] % 2 == 0]
print(" ".join(map(str, lst)))