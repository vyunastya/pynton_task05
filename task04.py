#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Данные вводятся корректно в алфавитном порядке
with open('str.txt', 'r') as file:
    my_str = file.read()
new_str=''
task = True #сжимаем
for char in my_str:
    if char.isdigit():
        task = False #восстанавливаем
        break
if task:
    temp_list = sorted(list(set(my_str)))
    for i, item in enumerate(temp_list):
        number = my_str.count(item)
        new_str = new_str + str(number) +item
else:
    start = 0
    end = 0
    for char in my_str:
        if char.isdigit():
            end+=1
        else:
            new_str = new_str + int(my_str[start:end]) * char
            end += 1
            start = end
with open('result.txt', 'w') as res:
    res.write(new_str)

