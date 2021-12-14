import hashlib

text = input("enter the text")

bord = text.encode()

print("MD5:", hashlib.md5(bord).hexdigest())
