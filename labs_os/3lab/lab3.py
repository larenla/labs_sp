import requests

URL="http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
a = requests.get(URL) # получение запроса
a.encoding="windows-1251" # кодировка
print(a.text) # вывод на экран


