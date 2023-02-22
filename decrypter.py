import os
import pyaes

## abre o arquivo que foi criptografado
file_name = "test.txt.youdied"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado
os.remove(file_name)

## cria o arquivo descriptografado
new_file = "test.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()