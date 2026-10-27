# Task 2

def calculate_standard_deviation(scores):
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    standard_deviation = variance ** 0.5

    return round(standard_deviation, 2)


scores = [70, 80, 75, 90, 85]


print("Standard Deviation:", calculate_standard_deviation(scores))
