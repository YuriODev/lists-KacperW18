# Your solution to Exercise 21
numbers = input()
lst = list(map(int, numbers.split()))
position = int(input())
value = int(input())
lst.insert(position, value)
print(" ".join(map(str,lst)))
