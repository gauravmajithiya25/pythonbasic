numbers = [1,-2,3,-4,5,6,-7,8,-9,10]

positive_numbers_count = 0
sum_even_numbers = 0
for number in numbers:
    if number > 0:
        positive_numbers_count += 1
    if number % 2 == 0:
        sum_even_numbers += number

print(f"Number of positive numbers: {positive_numbers_count}")
print(f"Sum of even numbers: {sum_even_numbers}")
