from random import choice

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
diffrent_symbols = 'il1Lo0O'
char = ''

def is_valid_num(num):
    return num.isdigit() and int(num) > 0

def get_data(text, data, yes, no, answer = ''):
    while answer != yes and answer != no:
        answer = input(f'{text} {yes}/{no} ').strip()
    if answer == yes:
        global char
        char += data

def generate_password(length, chars):
    password = ''
    for _ in range(int(length)):
        password += choice(char)
    return password

pass_count = ''
while not is_valid_num(pass_count):
    pass_count = input('Сколько паролей сгенерировать? (Введите число больше 0) ').strip()

pass_len = ''
while not is_valid_num(pass_len):
    pass_len = input('Какой длины пароли сгенерировать (Введите число больше 0) ').strip()

get_data('Включать ли в пароли цифры "0123456789"?', digits, 'да', 'нет')
get_data('Включать ли в пароли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?', uppercase_letters, 'да', 'нет')
get_data('Включать ли в пароли строчные буквы "abcdefghijklmnopqrstuvwxyz"?', lowercase_letters, 'да', 'нет')
get_data('Включать ли в пароли символы "!#$%&*+-=?@^_"?', punctuation, 'да', 'нет')
get_data('Оставить в паролях неоднозначные символы "il1Lo0O"?', diffrent_symbols, 'да', 'нет')

for _ in range(int(pass_count)):
    print(generate_password(pass_len, char))
input('Нажмите ENTER чтобы выйти')