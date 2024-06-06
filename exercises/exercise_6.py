# Your solution to Exercise 6
numbers = input()
lst = list(map(int, numbers.split()))
count = 0
for x in range(1,len(lst)-1):
    if lst[x-1] < lst[x] and lst[x+1] < lst[x]:
        count += 1
print(count)
