# Your solution to Exercise 4
numbers = input()
lst = list(map(int, numbers.split(",")))
lst = [lst[x] for x in range(1,len(lst),2)]
print(",".join(map(str, lst)))
