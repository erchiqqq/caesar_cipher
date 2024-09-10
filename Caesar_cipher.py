rus_small = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_big = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
eng_small = 'abcdefghijklmnopqrstuvwxyz'
eng_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text1 = input('Введите текст для шифрования: ')
shift = int(input('Введите значение сдвига: '))
cipher_or_decipher = input('Требуется шифровка или дешифровка? (ш/д): ')

def caesar_cipher(text_nach, sdvig):
    text_kon = ''
    for i in text_nach:
        if i.isalnum():
            if i.lower() in rus_small:
                if i.islower():
                    x = rus_small.find(i) + sdvig
                    if x > 31:
                        text_kon += rus_small[x - 32]
                    else:
                        text_kon += rus_small[x]
                else:
                    x = rus_big.find(i) + sdvig
                    if x > 31:
                        text_kon += rus_big[x - 32]
                    else:
                        text_kon += rus_big[x]
            elif i.lower() in eng_small:
                if i.islower():
                    x = eng_small.find(i) + sdvig
                    if x > 25:
                        text_kon += eng_small[x - 26]
                    else:
                        text_kon += eng_small[x]
                else:
                    x = eng_big.find(i) + sdvig
                    if x > 25:
                        text_kon += eng_big[x - 26]
                    else:
                        text_kon += eng_big[x]

        else:
            text_kon += i
    return text_kon

def caesar_decipher(text_nach, sdvig):
    text_kon = ''
    for i in text_nach:
        if i.isalnum():
            if i.lower() in rus_small:
                if i.islower():
                    x = rus_small.find(i) - sdvig
                    if x > 31:
                        text_kon += rus_small[x - 32]
                    else:
                        text_kon += rus_small[x]
                else:
                    x = rus_big.find(i) - sdvig
                    if x > 31:
                        text_kon += rus_big[x - 32]
                    else:
                        text_kon += rus_big[x]
            elif i.lower() in eng_small:
                if i.islower():
                    x = eng_small.find(i) - sdvig
                    if x > 25:
                        text_kon += eng_small[x - 26]
                    else:
                        text_kon += eng_small[x]
                else:
                    x = eng_big.find(i) - sdvig
                    if x > 25:
                        text_kon += eng_big[x - 26]
                    else:
                        text_kon += eng_big[x]

        else:
            text_kon += i
    return text_kon

if cipher_or_decipher == 'ш':
    print(caesar_cipher(text1, shift))
else:
    print(caesar_decipher(text1, shift))
