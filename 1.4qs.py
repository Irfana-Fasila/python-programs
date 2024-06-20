count = 0
total_sum = 0
for number in range(101, 200):
    if number % 7 == 0:
        count += 1
        total_sum += number
print(f"Number of integers greater than 100 and less than 200 that are divisible by 7: {count}")
print(f"Sum of all integers greater than 100 and less than 200 that are divisible by 7: {total_sum}")
