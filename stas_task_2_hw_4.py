# В задании четко не указано должна ли быть строка произвольной или строго указанной в задании.
# Сделал оба варианта

text_1 = input('Enter your text ')
text_2 = 'Hillel school'

un_text_1 = sorted(set(text_1), key=text_1.index)  # Создаем новый отсортированный список из уникальных элементов
un_text_2 = sorted(set(text_2), key=text_2.index)

co_text_1 = []  # Объявляем переменные для списков с частотой повторений
co_text_2 = []

for i in un_text_1:  # Добавляем в наш список частоту повторений
    co_text_1.append(text_1.count(i))

for i in un_text_2:
    co_text_2.append(text_2.count(i))

dict_text_1 = {}  # Объявляем переменные для словарей
dict_text_2 = {}

for n in range(0, len(un_text_1)):  # Наполняем наши словари каждой комбинаций из двух список
    dict_text_1[un_text_1[n]] = co_text_1[n]

for n in range(0, len(un_text_2)):
    dict_text_2[un_text_2[n]] = co_text_2[n]

print(dict_text_2, dict_text_1, sep='\n')
