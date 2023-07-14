# Дан список чисел. Определите, сколько в нем встречается 
# различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6




# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

# list_user = list(map(int, input('write a number with space').split())) #map - преобразовывает из строки в тот тип данных, что укажешь 
list_user = (int(i) for i in input('write a number with space').split())
voc = {}
for i in list_user:
    if i not in voc:
        voc[i] = 0
    voc[i] += 1
print(len(voc.keys())) 