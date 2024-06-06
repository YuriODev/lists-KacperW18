# Your solution to Exercise 16
numbers = input()
lst = list(map(int,numbers.split()))
unique_lst = []
for x in range(len(lst)):
    value = lst.count(lst[x])
    if value == 1:
        unique_lst.append(lst[x])
print(" ".join(map(str, unique_lst)))
