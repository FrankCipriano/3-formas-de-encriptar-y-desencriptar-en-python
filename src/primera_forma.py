from werkzeug.security import generate_password_hash,check_password_hash

texto='d8s$fs_po'

#-ENCRIPTANDO EL TEXTO, USANDO MULTIPLES ALGORITMOS DE ENCRIPTACION CON ITERACIONES DE EJEMPLO
texto_cifrado1=generate_password_hash(texto)
texto_cifrado2=generate_password_hash(texto,'sha256')
texto_cifrado3=generate_password_hash(texto,"sha256",30)
texto_cifrado4=generate_password_hash(texto,"pbkdf2:sha256")#-algoritmo de encriptacion con mayor seguridad
texto_cifrado5=generate_password_hash(texto,'pbkdf2:sha256',100)
texto_cifrado6=generate_password_hash(texto,"pbkdf2:sha256:30",30)
print(texto_cifrado1)
print(texto_cifrado2)
print(texto_cifrado3)
print(texto_cifrado4)
print(texto_cifrado5)
print(texto_cifrado6)

#-DESENCRIPTANDO EL TEXTO, PARA VERIFICAR SI LE ENCRIPTACION CORRESPONDE AL TEXTO PLANO
print(check_password_hash(texto_cifrado1,texto))
print(check_password_hash(texto_cifrado2,texto))
print(check_password_hash(texto_cifrado3,texto))
print(check_password_hash(texto_cifrado4,texto))
print(check_password_hash(texto_cifrado5,texto))
print(check_password_hash(texto_cifrado6,texto))