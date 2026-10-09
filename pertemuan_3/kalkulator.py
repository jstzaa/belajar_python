num1 = int(input('masukkan no 1: '))
operator = str(input('pilih operator: '))
num2 = int(input('masukkan no 2: '))

# if operator == '+':
#     hasil = num1 + num2
#     print('hasil: ', hasil)
# elif operator == '-':
#     hasil = num1 - num2
#     print('hasil: ', hasil)
# elif operator == '*':
#     hasil = num1 * num2
#     print('hasil: ', hasil)
# elif operator == '/':
#     hasil = num1 / num2
#     print('hasil: ', hasil)
# else:
#     print('input salah')

hasil = {
    '+' : num1 + num2,
    '-' : num1 - num2,
    '*' : num1 * num2,
    '/' : num1 / num2,
    '%' : num1 % num2,
    '**' : num1 ** num2,
    '//' : num1 // num2,
}

print('hasil: ', hasil[operator])