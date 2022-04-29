"""
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
"""

cout_5 = 0
for i in range(10):
    s_input = 'Attempt=' + str(i+1) + ' Enter any number: '
    i_num = int(input(s_input))
    print('You entered the number',i_num)
    if i_num==5:
        cout_5 += 1

print('Digit 5 has been entered ', cout_5, ' times')