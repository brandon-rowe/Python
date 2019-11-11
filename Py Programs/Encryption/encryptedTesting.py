from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

#Encode
message = "I am a super secret spy"
encoded = message.encode()

#Encrypt
f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)

#Get key again (demo)
file = open('key.key', 'rb')
key2 = file.read()
file.close()

#Decrypt
f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)

#Decode
original_message = decrypted.decode()
print(original_message)
