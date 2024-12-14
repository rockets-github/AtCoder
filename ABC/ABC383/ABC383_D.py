def count_numbers_with_9_divisors(N):
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [x for x in range(limit + 1) if is_prime[x]]

    primes = sieve(int(N**0.5) + 1)
    count = 0

    for p in primes:
        if p**8 <= N:
            count += 1
        else:
            break

    for i in range(len(primes)):
        a = primes[i]
        if a**2 > N:
            break
        for j in range(i + 1, len(primes)):
            b = primes[j]
            if a**2 * b**2 <= N:
                count += 1
            else:
                break

    return count

N = int(input())
result = count_numbers_with_9_divisors(N)
print(result)
