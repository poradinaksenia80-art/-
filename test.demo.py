def calculate_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


result = calculate_sum(5)
print(f"Сумма чисел: {result}")
