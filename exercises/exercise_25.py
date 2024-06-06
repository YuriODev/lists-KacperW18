# Your solution to Exercise 25
value = int(input())
image = [["." for x in range(value)] for y in range(value)]
for x in range(value):
    for y in range(value):
        if x == y or x == (value - y - 1) or y == (value-1)/2 or x == (value-1)/2:
            image[x][y] = "*"
for row in image:
    print(" ".join(row))
    


