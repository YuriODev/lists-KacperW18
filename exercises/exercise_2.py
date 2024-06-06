# Your solution to Exercise 2
user_input = input()
lst = user_input.split()
lst.sort()
reversed = lst[::-1]
print(" ".join(reversed))
