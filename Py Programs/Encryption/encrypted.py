from cryptography.fernet import Fernet
import time
start_time = time.time()
#Get the key from file
file = open('key.key', 'rb')
key = file.read()
file.close()

#Open the file to encrypt
with open('txt0.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Write the encrypted file
with open('test.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    
end_time = time.time()
total_time = end_time - start_time
print("Started at ",start_time)
print("Ended at ",end_time)
print("Time lapsed ",total_time)
