# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

def count_digit_one(n):
    if n <= 0:
        return 0

    count = 0
    factor = 1

    while factor <= n:
        divisor = factor * 10
        count += (n // divisor) * factor + min(max(n % divisor - factor + 1, 0), factor)
        factor *= 10

    return count

n = int(input())
result = count_digit_one(n)
print(result)