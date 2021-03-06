from Crypto.publickey import RSA

new_key = RSA.generate(4096, e=65537)
private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

print(private_key)
fd = open("private.pem", "wb")
fd.write(private_key)
fd.close()

print(public_key)
fd = open("public.pem", "wb")
fd.write(public_key)
fd.close()