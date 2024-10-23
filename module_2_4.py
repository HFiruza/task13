# def is_prime(x):
#     for i in range(2, (x//2)+1):
#         if x % i == 0:
#             return False
#     return True
# def is_prime(a):
#     if a % a == 0 and a != 0:
#         return True
#     else:
#         return False
# a = int(input("Enter a number: "))
# print(is_prime(a))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes:', primes)
print('Not primes:', not_primes)
