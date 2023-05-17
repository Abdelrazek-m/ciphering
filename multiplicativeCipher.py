def encryption(text,key):
    cipher=''
    for i in text:
        if i.islower():
            cipher+=chr(((ord(i)-97)*key)%26+97)
        else:
            cipher+=chr(((ord(i)-65)*key)%26+65)
    return cipher

def rev(key):
    for i in range(1,25,2):
        if (key*i)%26==1:
            return i
def decryption(cipher,key):
    k=rev(key)
    text=''
    for i in cipher:
        if i.islower():
            text+=chr(((ord(i)-97)*k)%26+97)
        else:
            text+=chr(((ord(i)-65)*k)%26+65)
    return text

c=encryption('Secret',9)
print(c)
print(decryption(c,9))