def encryption(text,key,key2):
    cipher=''
    for i in text:
        if i==' ':
            cipher+=' '
        else:
            if i.islower():
                cipher += chr(((ord(i) - 97) * key + key2) % 26 + 97)
            else:
                cipher += chr(((ord(i) - 65) * key + key2) % 26 + 65)
    return cipher

def rev(key):
    for i in range(1,25,2):
        if (key*i)%26==1:
            return i
def decryption(cipher,key,key2):
    k=rev(key)
    text=''
    for i in cipher:
        if i==' ':
            text+=' '
        else:
            if i.islower():
                text += chr(((ord(i) - 97 - key2) * k) % 26 + 97)
            else:
                text += chr(((ord(i) - 65 - key2) * k) % 26 + 65)
    return text
k1=7
k2=2
c=encryption('Hello World',k1,k2)
print(c)
print(decryption(c,k1,k2))