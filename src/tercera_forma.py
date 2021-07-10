from cryptography.fernet import Fernet

texto='d8s$fs_po'
#-GENERANDO UNA CLAVE EN FORMATO DE SECUENCIA DE BYTES
llave=Fernet.generate_key()
objeto_cifrado=Fernet(llave)
#-ENCRIPTANDO EL TEXTO CON LA LLAVE EN BYTES
texto_encriptado=objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)


#-DESENCRIPTANDO LLAVE EN SECUENCIA DE BYTES
texto_cifrado_bytes=objeto_cifrado.decrypt(texto_encriptado)
print(texto_cifrado_bytes)
#-DESENCRIPTANDO EL TEXTO CON LA LLAVE EN SECUENCIA DE BYTES
texto_cifrado=texto_cifrado_bytes.decode()
print(texto_cifrado)