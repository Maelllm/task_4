text = input('Enter your products ').lower()

list_1 = list(set(text.lower().split(sep=',')))

list_1.sort()
text_2 = ''

for i in list_1:
    text_2 += i
    text_2 += ','

print(text_2[:-1])
