#prime number
number = 29
is_prime = True
for i in range(2, number):
    if (number % i) == 0:
        is_prime = False
        print(f"{number} is not a prime number.")
        break
if is_prime:
    print(f"{number} is a prime number.")