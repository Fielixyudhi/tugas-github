import os
word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def variable(n):
    if n < 10:
        return word[n]
    elif n >= 1_000_000_000:
        return variable(n // 1_000_000_000) + ' billion ' + (variable(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return variable(n // 1_000_000) + ' million ' + (variable(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (variable(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return variable(n // 1_000) + " thousand " + (variable(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (variable(n % 100) if n % 100 != 0 else '')
        else:
            return variable(n // 100) + ' hundred ' + (variable(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n // 10 == 2:
            return ' twenty ' + (variable(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 3:
            return ' thirty ' + (variable(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 4:
            return ' fourty ' + (variable(n % 10) if n % 10 != 0 else '')
        elif n // 10 == 5:
            return ' fifty ' + (variable(n % 10) if n % 10 != 0 else '')
        else:
            return variable (n // 10) + 'ty ' + (variable(n % 10) if n % 10 != 0 else '')
     
    else :
        if n==10:
            return 'ten'
        elif n==11:
            return 'eleven'
        elif n==12:
            return 'twelve'
        elif n==13:
            return 'thirteen'
        elif n==15:
            return 'fifteen'
        else :
            return variable(n%10) + 'teen'

while True:
    os.system('cls')
    print(" Monggo Boleh Dicoba Mas Mbak ")
    try:
        n = int(input('Mau angka berapa mas/mbak ? '))
        print(f'{n:,} = {variable(n)}')
    except:
        print('mas/mbak salah nih data yang kalian masukkan: ')
    os.system('pause')