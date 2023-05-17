def encryption(plainText,key):
    cipher=''
    c=''
    for i in plainText:
        if ord(i)>=97:
            c=chr((ord(i)-97+key)%26 +97)
        else:
            c=chr((ord(i)-65+key)%26+65)
        cipher+=c
    return cipher

def decryption(cipherText,key):
    text=''
    c=''
    for i in cipherText:
        if ord(i)>=97:
            c=chr((ord(i)-97-key+26)%26+97)
        else:
            c=chr((ord(i)-65-key+26)%26+65)
        text+=c
    return text

print(encryption('Hello',3))
print(decryption('Khoor',3))