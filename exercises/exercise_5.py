# Your solution to Exercise 5
numbers = input()
lst = list(map(int, numbers.split()))
unique_lst = []
for x in lst:
    if x not in unique_lst:
        unique_lst.append(x)
print(len(unique_lst))
