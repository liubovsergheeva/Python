# Тип данных string:
message_string = 'hello'
# Тип данных int (integer):
age_integer = 100
# Тип данных float:
height_float = 165.5
# Тип данных bytes - это неизменяемые последовательности отдельных байтов. добавляется префикс 'b':
bytes_type = b'this is massive of bytes'
# объекты bytes могут быть созданы с помощью встроенного класса bytes(), например, заполненный нулями объект байтов
# указанной длины:
byyy = bytes(10)
# список list - самый универсальный составной тип данных в Python,элементы одного списка могут иметь разные типы данных,
#  Получить доступ к элементам при помощи оператора нарезки ( [ ] и [:] ) и индексов
my_list = [True, 777, 3.11, 'text', 70.1]
# кортеж - составной тип данных, его элементы не могут быть изменены, похоже на список для чтения и экономит место в
# памяти
my_tuple = (True, 777, 3.12, 'eto text', 77.2)
# set это коллекционный тип данных и хранит только уникальные значения:
s = set('123456')
se = set('setttt')
set = {"hi", "bye"}
# отличие set от frozenset в том что у set изменяемый тип данныхб, а у  frozenset - неизменяемый (ситуация как со
# списком и кортежем)
fro = frozenset('12356')
frozzz = frozenset('124text6sake')
frozen = frozenset('qwerty')
# dict - словарь, неупорядоченная коллекция произвольных объектов с доступом по ключу:
dictionary = {'dict': 1, 'dictionary': 2, 'slovar': 3, 'slovo': 4}

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль:
aa = str(123)
bb = str(555)
cc = aa+bb
# Вывести в консоль все выше перечисленные переменные с добавлением типа данных:
print(message_string, type(message_string))
print(age_integer, type(age_integer))
print(height_float, type(height_float))
print(bytes_type, type(bytes_type))
print(byyy, type(byyy))
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(s, type(s))
print(se, type(se))
print(set, type(set))
print(fro, type(fro))
print(frozzz, type(frozzz))
print(frozen, type(frozen))
print(dict, type(dict))
print(cc, type(cc))
# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую):
print(message_string, ",", age_integer, type(message_string), type(age_integer))
print(message_string, age_integer, type(message_string), type(age_integer))
# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(message_string + str(age_integer))
print(aa, ''+'', age_integer)
