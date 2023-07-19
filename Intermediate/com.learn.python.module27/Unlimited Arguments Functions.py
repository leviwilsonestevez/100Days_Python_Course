def total_sum(*numbers) -> int:
    total_sum = 0
    for arg in numbers:
        total_sum += arg
    return total_sum


print(total_sum(3, 5, 7, 8, 9, 0, 2, 546, 8, 33, 32, 8, 34, 23))
