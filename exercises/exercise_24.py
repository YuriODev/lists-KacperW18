# Your solution to Exercise 24
numbers = input()
lst = list(map(int, numbers.split()))
negative = [x for x in lst if x < 0]
positive = [x for x in lst if x > 0]
negative.sort(reverse=True)
positive.sort(reverse=True)
final = positive + negative
print(" ".join(map(str,final)))
