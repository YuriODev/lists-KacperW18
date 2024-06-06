# Your solution to Exercise 19
words = input()
lst = words.split("_")
for x in lst:
    print(x.capitalize(), end="")
print("".join(lst))

