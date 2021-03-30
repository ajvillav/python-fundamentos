import getpass

print("""A continuación vas a crear un correo electronico
Por favor ingresa los siguentes datos. """)
user = str(input('Ingresa el nombre de usuario que deseas: '))
print("""Elige la extensión que deseas:
1. @gmail.com
2. @gmail.es
3. @hotmail.com
4. @hotmail.es""")

while True:
    try:
        ext = str(input())
        if ext == '1' or ext == '@gmail.com':
            mail = user + '@gmail.com'
        elif ext == '2' or ext == '@gmail.es':
            mail = user + '@gmail.es'
        elif ext == '3' or ext == '@hotmail.com':
            mail = user + '@hotmail.com'
        elif ext == '4' or ext == '@hotmail.es':
            mail = user + '@hotmail.es'
        print('Su dirección de correo es: ', mail)
        break
    except:
        print('Usted ha ingresado una extensión envalida, intentelo de nuevo.')

pas = getpass.getpass('Elige tu contraseña: ')
print('Has creado tu correo exitosamente, ahora puedes logearte')

while True:
    m = str(input('Ingrese su dirección de correo: '))
    p = getpass.getpass('Ingrese su contraseña: ')
    if m == mail and p == pas:
        print('Felicidades, has entrado a tu correo electronico ', mail)
        break
    else:
        print('dirección de correo o contraseña incorrecta, intentalo de nuevo: ')ly