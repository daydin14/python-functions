# Challenge 1
def sum_to(n):
    sum = 0
    while (n > 0):
        sum += n
        n -= 1
    return sum
print(sum_to(6))
print(sum_to(10))