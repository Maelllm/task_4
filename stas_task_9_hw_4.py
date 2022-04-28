list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['anaconda', (3, 4), 'a', 2 * 4, 'milk', 'beer', 8 % 3]  # Повторяющийся объект "замаскирован"

for i in list_1:
    if i in list_2:
        print(i in list_2)
        break
