# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 1 вариант
# my_str = 'Я люблю Джавабв иабв Питон'
# my_list = my_str.split()
# new_list = [i for i in my_list if not 'абв' in i]
# result = ' '.join((new_list))
# print(result)

# 2 вариант
my_str = 'Я люблю Джавабв иабв Питон'
my_list = my_str.split()
new_list = list(filter(lambda x: not 'абв' in x, my_list))
print(*new_list)

