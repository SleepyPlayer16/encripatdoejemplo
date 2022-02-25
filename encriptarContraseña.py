message = input('Ingresar alguna contraseña: ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5
encrypt = ''
decrypt = ''
import time
from string import digits

option = None
while (option != 1) and (option !=2):
    question = input('Encriptar (1) o desencriptar? (2): ')
    try:
        option = int(question)
    except ValueError:
        print('Elegir una opción valida')

if option == 1:
    for i in message:
        position=alphabet.find(i)
        newposition=(position+5)%26
        encrypt+=alphabet[newposition]
    print('Su contraseña encriptada es: ',encrypt)

elif option == 2:
    for i in message:
        pos=alphabet.find(i)
        newpos=(pos-5)%26
        decrypt+=alphabet[newpos]
    print('Su contraseña desencriptada es: ',decrypt)


