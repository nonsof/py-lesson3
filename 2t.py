# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

import random
# list_user = (int(i) for i in input('write a list').split())
# list_user = [i for i in range(1, n)]
rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(0, 100))
print(rand_list)

k = int(input('write a number'))

# output = rand_list[-k :] + rand_list[:-k]
for i in range(k):
    last = rand_list.pop()
    rand_list.insert(0, last)

print(rand_list)
