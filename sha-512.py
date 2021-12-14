import hashlib

text = input("enter the text")

bord = text.encode()

print("SHA-512:", hashlib.sha3_512(bord).hexdigest())
