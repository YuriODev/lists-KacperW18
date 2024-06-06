# Your solution to Exercise 18
numbers = input()
lst = list(map(int,numbers.split()))
max_position = lst.index(max(lst)) 
min_position = lst.index(min(lst))
maximum , minimum = max(lst), min(lst)
lst[max_position] = minimum
lst[min_position] = maximum
print(" ".join(map(str,lst)))

