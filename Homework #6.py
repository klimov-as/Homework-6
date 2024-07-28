my_dict = {'Петя': 1990, 'Вася': 1980, 'Саша': 2000}
print(my_dict)
print(my_dict['Вася'])
print(my_dict.get('Коля', 'Такого значения нет'))
my_dict.update({'Юля': 2015,
                'Света': 2020})
a = my_dict.pop('Петя')
print(a)
print(my_dict)

my_set = {2, 1, 3, 3, 2, 'text', 1, 1, 'text'}
print(my_set)
my_set.add(5)
my_set.add(5.7)
my_set.discard(1)
print(my_set)