
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum_of_numbers = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0: 
        sum_of_numbers += i
        count += 1


average = sum_of_numbers / count
print(f"Среднее арифметическое чисел, кратных 3, на отрезке [{a}; {b}]: {average}")