def fale_with_text():
    # считываем данные из файла
    r = open('C:\\programming\\Test\\folder 1\\list 1.txt')
    return (r.read())
    r.close()

import string
def text_count(text):
    # получаем список слов из текста
    for char in string.punctuation:
        text = text.replace(char, "")
        text_list = text.split()

    # олучаем словарь
    x = {}
    for i in text_list:
        x[i] = text_list.count(i)

    # сортируем словарь по значеням
    sorted_x = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))

    #записываем данные в новый файл
    d = open('C:\\programming\\Test\\folder 1\\list 2.txt', 'w', encoding='ANSI')
    print('данные записаны в файл')
    return d.write(str(sorted_x))
    d.close()

text_count(fale_with_text())