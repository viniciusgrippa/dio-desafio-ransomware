import os
import pyaes

## Abrir arquivo criptografado

file_name = 'teste.txt.ransomwareretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## Chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## REmover arquivo criptografado
os.remove(file_name)


## Criar um novo arquivo descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

