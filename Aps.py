#Essa parte criptografa o texto

from cryptography.fernet import Fernet
chave = Fernet.generate_key()
fernet = Fernet(chave)

texto = input("Insira o texto para criptografar:")

def cripto (texto, fernet): 
    texto = bytes(texto ,'utf-8')
    return  fernet.encrypt(texto).decode()
    

criptografado = cripto(texto, fernet)
print ("A criptografia resultou em:")
print (criptografado)

#Essa oarte desimcriptografa o texto

def desincripto (criptografado, fernet):
    desincripto = fernet.decrypt(criptografado)
    return (desincripto.decode())

texto_desincripto = desincripto (criptografado, fernet)
print ("A descriptografia resultou em:")
print (texto_desincripto)


