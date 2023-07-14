# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)


# Input: [0, -1, 5, 2, 3]

# Output: 2 (-1 < 5, 2 < 3)


# Примечание: Пользователь может вводить значения списка или список задан изначально.
import random
lst = [random.randint(-100, 100) for i in range(random.randint(1, 20))]
print(lst)
count = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(lst[i], end=" ")
print(count)
