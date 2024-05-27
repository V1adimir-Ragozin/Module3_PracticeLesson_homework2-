def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
# print_params(a)            нельзя вызвать - параметр не поределено
# print_params(a, b)         нельзя вызвать - параметры не поределены
# print_params(a, b, c)      нельзя вызвать - параметры не поределены
print_params(b=25)
print_params(c = [1,2,3])
values_list = ['qwerty', 3.14, (1, 2, 3)]
values_dict = {'a': 'qwerty', 'b': 3.14, 'c': (1, 2, 3)}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 'qwerty']
print_params(*values_list_2, 42)   # вызов функции работает, т.к. количество параметров совпадает