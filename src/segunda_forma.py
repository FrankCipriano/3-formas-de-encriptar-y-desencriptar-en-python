from passlib.context import CryptContext

#-CREANDO EL CONTEXTO DE ENCRIPTADO, UTILIZANDO EL ALGORITMO DE MAYOR SEGURIDAD "pbkdf2_sha256"
CONTEXTO=CryptContext(
    schemes=['pbkdf2_sha256'],
    default='pbkdf2_sha256',
    pbkdf2_sha256__default_rounds=30000
)

texto='d8s$fs_po'

#-ENCRIPTANDO EL TEXTO
texto_encriptado1=CONTEXTO.hash(texto)
print(texto_encriptado1)

#-DESENCRIPTANDO EL TEXTO
print(CONTEXTO.verify(texto,texto_encriptado1))