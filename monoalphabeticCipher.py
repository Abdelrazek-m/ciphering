#letters = 'ABCDEFGHIJKLMNOPQRSTYVWXYZ'

key='qwertyuiopasdmghjklzxcvbnf'
def encryption(text,k):
    cipher=''
    for l in text:
        cipher+=k[ord(l)-97]
    return cipher
def decryption(cipher,k):
    text=''
    for l in cipher:
        text+=chr(k.index(l)+97)   #k[ord(l)-65]
    return text
print(encryption('hello',key))
print(decryption('itssg',key))