import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("C:/Users/Nithin/Desktop/MCA Projects/ImagePassword/src/test.txt", "data.txt.aes", password, bufferSize)
# decrypt
#pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)