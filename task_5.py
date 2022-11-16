"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(ya_ping.stdout)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))


ARGS = ['ping', 'youtube.com']
youtube_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(youtube_ping.stdout)
for line in youtube_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
