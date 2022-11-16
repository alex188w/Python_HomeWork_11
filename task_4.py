"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

strs = ['разработка', 'администрирование', 'protocol', 'standard']
strs_bytes = []

for s in strs:
    s = s.encode('utf-8')
    strs_bytes.append(s)
    print(s)

for s in strs_bytes:
    print(s.decode('utf-8'))
