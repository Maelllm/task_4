list_1 = ['bread', 'milk', 'kolbasa']
for_list_3 = input('Enter your list ')
list_3 = for_list_3.split()

list_2 = []
for i in list_1:
    list_2.append(len(i))

list_4 = []
for n in list_3:
    list_4.append(len(n))

print('Самое длинное название продукта {} длинна {} символов'.format(list_1[list_2.index(max(list_2))],
                                                                     max(list_2)))
print('Самое длинное название продукта {} длинна {} символов'.format(list_3[list_4.index(max(list_4))],
                                                                     max(list_4)))
