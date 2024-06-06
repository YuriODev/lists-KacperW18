# Your solution to Exercise 22
binary = input()
digits = list(map(int, binary))
total = 0
for i in range(len(digits)):
    total += digits[-i-1] * 2**i
print(total)
        
