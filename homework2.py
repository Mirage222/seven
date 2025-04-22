total_sum = 0
for i in range(1001):
    if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
        total_sum += i

print(f"Сумма чисел от 0 до 1000, кратных 2 и 3, но не кратных 4: {total_sum}")