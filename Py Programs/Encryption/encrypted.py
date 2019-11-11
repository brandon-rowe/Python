from cryptography.fernet import Fernet
import time

start_time0 = time.time()
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
with open('test0.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    
end_time0 = time.time()
total_time0 = end_time0 - start_time0
print()
print("Started txt0 at ",start_time0)
print("Ended txt0 at ",end_time0)
print("Time lapsed for txt0 Encryption ",total_time0)

start_time1 = time.time()
#Get the key from file
file = open('key.key', 'rb')
key = file.read()
file.close()

#Open the file to encrypt
with open('txt1.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Write the encrypted file
with open('test1.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    
end_time1 = time.time()
total_time1 = end_time1 - start_time1
print()
print("Started txt1 at ",start_time1)
print("Ended txt1 at ",end_time1)
print("Time lapsed for txt1 Encryption ",total_time1)

start_time2 = time.time()
#Get the key from file
file = open('key.key', 'rb')
key = file.read()
file.close()

#Open the file to encrypt
with open('txt2.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Write the encrypted file
with open('test2.txt.encrypted', 'wb') as f:
    f.write(encrypted)
    
end_time2 = time.time()
total_time2 = end_time2 - start_time2
print()
print("Started txt2 at ",start_time2)
print("Ended txt2 at ",end_time2)
print("Time lapsed for txt2 Encryption ",total_time2)


#Write results to result.txt
results = open('results.txt', 'a')
results.write('Encrypting txt0\n\n')
results.write('Start time: {0}\nEnd Time: {1}\nTime Lapsed: {2}\n\n'.format(start_time0, end_time0, total_time0))
results.write('Encrypting txt1\n\n')
results.write('Start time: {0}\nEnd Time: {1}\nTime Lapsed: {2}\n\n'.format(start_time1, end_time1, total_time1))
results.write('Encrypting txt2\n\n')
results.write('Start time: {0}\nEnd Time: {1}\nTime Lapsed: {2}\n\n'.format(start_time2, end_time2, total_time2))
results.close()

