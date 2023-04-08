from getprimes import sieve_iter
import bisect

def check_for_primality(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_emirps():
    for prime in sieve_iter():
        if prime > 10:
            if str(prime) == str(prime)[::-1]:
                continue
            if check_for_primality(int(str(prime)[::-1])):
                yield prime

if __name__ == '__main__':
    a = get_emirps()

    for i in range(10000):
    
        print(next(a))
