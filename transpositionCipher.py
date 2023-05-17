from math import *
def encryption(text,key):
    cipher=''
    for col in range(key):
        i=col
        while i<len(text):
            cipher+=text[i]
            i+=key
    return cipher


def decryption(cipher,key):
    text=''
    r_key=ceil(len(cipher)/key)
    for row in range(r_key):
        i=row
        while i<len(cipher):
            text+=cipher[i]
            i+=r_key
    return text




c=encryption('hello world',4)
print(c)
print(decryption(c,4))