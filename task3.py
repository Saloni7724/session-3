#Task 3 

friend_a = [200, 200, 200, 200, 200]
friend_b = [100, 300, 150, 400, 50]

def standard_deviation(numbers):

    mean = sum(numbers) / len(numbers)

    total = 0

    for x in numbers:
        total = total + (x - mean) ** 2

    variance = total / len(numbers)

    return variance ** 0.5


sd_a = standard_deviation(friend_a)
sd_b = standard_deviation(friend_b)

print("Friend A SD =", sd_a)
print("Friend B SD =", round(sd_b, 2))

print("Friend A has more consistent spending.")
print("Friend B has more variation in spending.")