import hashlib

text = input("enter the text")

bord = text.encode()

print("SHA-256:", hashlib.sha256(bord).hexdigest())
