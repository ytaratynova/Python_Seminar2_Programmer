# Реализуйте алгоритм перемешивания списка.

len_of_list = int(input("Введите длину списка:"))
my_list = []
for i in range(len_of_list):
    my_list.append(input(f"введите {i} элемент списка: "))
print(f"Ваш список выглядит так: {my_list}")

my_list_mix = []

if (len_of_list % 2 == 0):                          # Перемешиваем список путем перестановки местами пар соседних элементов.
    for i in range(0, len_of_list, 2):              
        my_list_mix.append(my_list[i + 1])
        my_list_mix.append(my_list[i])
else:
    for i in range(0, len_of_list//2 * 2, 2):       # Если количество элементов нечетное, то последний элемент вставляем в середину.
        my_list_mix.append(my_list[i + 1])
        my_list_mix.append(my_list[i])
    my_list_mix.insert(len_of_list//2, my_list[-1])
    
print(f'Ваш перемешанный список выглядит так: {my_list_mix}')


