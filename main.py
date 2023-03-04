list = []
list.append(3)
name = 'Добрый день!'
list.append(name)
list.insert(0, 'Привет')
list.reverse()
print(list)
list.pop(1)
list.remove('Привет')
list[0] = 100
print(list)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_summ = list_1 + list_2
print(list_summ)

string = "Привет, Мир!"
print(string)
string_2 = " -  Здравствуй!"
print(string_2)
str_summ = string + string_2
print(str_summ)
print(3 * str_summ)
print(len(str_summ))

str_list = str_summ.split('!')
print(str_list)
STR = str_summ.upper()
str = str_summ.lower()
print(str_summ.lower())
print(str_summ.upper())
print(str_summ.capitalize())

print(str_summ.title())
print(str_summ.swapcase())

print(str_summ.startswith('Привет,'))
print(str_summ.endswith('!'))

int = "1234hj 6789"

print(int.isdigit())
print(int.isalpha())
print(int.isalnum())

print(str.islower())
print(STR.isupper())
print(str_summ.istitle())

small_str = str_summ[5:10:3]
print(small_str)

print(str_summ.find('к'))
print(str_summ.rfind('т'))

print(str_summ.index('т'))
print(str_summ.rindex('т'))

print(str_summ.replace('Мир', 'Иван'))

print(str_summ.count('р'))
