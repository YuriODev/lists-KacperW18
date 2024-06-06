# Your solution to Exercise 14
numbers = input()
lst = list(map(int, numbers.split()))
x_axis = lst[0]-lst[2]
y_axis = lst[1]-lst[3]
length = (x_axis**2 + y_axis**2)**0.5
print(f"{length:.2f}")
