# Assume m and n are particular integers, for example:
m = 3  # example value for m
n = 2  # example value for n

# a. Check if 6m + 8n is even
is_even = (6*m + 8*n) % 2 == 0

# b. Check if 10mn + 7 is odd
is_odd = (10*m*n + 7) % 2 == 1

# c. Check if m^2 - n^2 is composite when m > n > 0
# A number is composite if it is not prime and greater than 1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_composite(num):
    return num > 1 and not is_prime(num)

is_m2_n2_composite = is_composite(m**2 - n**2)

# Print results
print("6m + 8n is even:", is_even)
print("10mn + 7 is odd:", is_odd)
print("m^2 - n^2 is composite when m > n > 0:", is_m2_n2_composite)



Output:  
6m + 8n is even: True
10mn + 7 is odd: True
m^2 - n^2 is composite when m > n > 0: False
