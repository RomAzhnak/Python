"""s = input()
outs = ''
rep = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        rep += 1
    else:
        outs += s[i-1] + str(rep)
        rep = 1
outs += s[-1] + str(rep)
print(outs)

with open('input.txt') as file_in, open("output.txt", 'w') as file_out:
    symbol = '00'
    for s in file_in.read():
        if s.isdigit():
            symbol += s
        else:
            print(symbol[0] * int(symbol[1:]), file=file_out, end='')
            symbol = s

wcount = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tData = line.split()
        for elem in tData:
            elem = elem.lower()
            wcount[elem] = wcount.get(elem, 0) + 1
wcount = sorted(wcount.items(), key=lambda x: (-x[1], x[0]))
print(wcount[0][0], wcount[0][1])

numb, totalm, totalph, totalr = 0, 0, 0, 0
with open('input.txt', 'r', encoding='utf-8') as file_in, open("output.txt", 'w') as file_out:
    for line in file_in:
        math, physic, rus = list(map(int, line.split(';')[1:]))
        numb += 1
        totalm += math
        totalph += physic
        totalr += rus
        print("{:.9f}".format((math + physic + rus) / 3), file=file_out)
    print("{:.9f} {:.9f} {:.9f}".format(totalm / numb, totalph / numb, totalr / numb), file=file_out)

import sys
import os
print('Аргументы командной строки:')
for i in sys.argv:
    print(i)
print(os.getcwd())
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
    print('name', __name__)
print(dir())

import requests
    url = f.read().strip()
    print(url)
r = requests.get(url)
print(len(r.text.splitlines()))


import requests
import tkinter.filedialog
#w = tkinter.Tk()
#w.title("Выбор файла для анализа")
inf = tkinter.filedialog.askopenfile('r')
with open('dataset_3378_2.txt', 'r', encoding='utf-8') as f:
    print(f)
print(inf)
#w.destroy()
url = inf.readline().strip()
r = requests.get(url)
print(len(r.text.splitlines()))

import requests
fl = 'https://stepik.org/media/attachments/course67/3.6.3/' + ''
r = requests.get(fl)
print(r.text)

import requests
line = '699991.txt'
url = 'https://stepik.org/media/attachments/course67/3.6.3/'
line = requests.get(url + line).text.strip()
while line[0:2] != 'We':
    line = requests.get(url + line).text.strip()
    print(0)
print(line)


import os
import time
import tkinter.filedialog
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = ['"C:\\My Documents"', 'C:\\Code']
# source = 'D:\\Python\\ВидеокурсCoursera\\'
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
# target_dir = 'E:\\Backup'   # Подставьте ваш путь.
w = tkinter.Tk()
source = tkinter.filedialog.askdirectory() + os.sep
# w.destroy()
target_dir = r"D:\Python\ВидеокурсCoursera"
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
target = target_dir + os.sep + time.strftime('%Y%m%d_%H%M%S')
# Создаём каталог, если его ещё нет
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # создание каталога
    print('Каталог успешно создан', target_dir)
# 5. Используем команду "zip" для помещения файлов в zip-архив
# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
zip_command = '"C:\\Program Files\\WinRAR\\WinRAR" a -r- {} {}'.format(target, source)
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
"""

import tkinter as tk
from tkinter import filedialog as fd

def callback():
    name = fd.askopenfilename()
    print(name)


errmsg = 'Error!'
tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)
tk.mainloop()
