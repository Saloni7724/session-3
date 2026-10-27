
# Task 1

steps = [4500, 7000, 5000, 8000, 4000, 9000, 6000]

mean = sum(steps) / len(steps)


print("Mean:", mean)

variance = sum((x - mean) ** 2 for x in steps) / len(steps)

print("Variance:", variance)

