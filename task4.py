#Task 4

salaries = [28000, 29000, 27000, 60000, 26500, 27500]

mean = sum(salaries) / len(salaries)

total = 0

for x in salaries:
    total = total + (x - mean) ** 2

variance = total / len(salaries)

standard_deviation = variance ** 0.5

print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", round(standard_deviation, 2))

print("The salary spread is high because one employee earns 60000.")
print("This high salary increases the variance and standard deviation.")