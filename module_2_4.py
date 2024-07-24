numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_praimes = []

for p in range(2, 16):
    for i in range(2, p):
        if p % i == 0:
            not_praimes.append(p)
            break
    else:
        primes.append(p)

print('Primes: ', primes)
print('Not Primes: ', not_praimes)
