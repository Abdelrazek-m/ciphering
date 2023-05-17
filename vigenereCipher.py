def encryption(text,key):
    cipher=''; a=0
    for i in range(len(text)):
        if text[i]==' ':
            a+=1; cipher += ' '; continue
        cipher+=chr( ( ord(text[i]) -65+ ord(key[(i-a)%len(key)]) -65 ) %26+65)
    return cipher
def decryption(cipher,key):
    text=''; a=0
    for i in range(len(cipher)):
        if cipher[i] == ' ':
            a+=1; text+=' '; continue
        text+=chr( ( ord(cipher[i])-ord(key[(i-a)%len(key)])+26)%26+65)
    return text
#HELLO THERE -> PXPLA BAIRQ
key='ITEAM'
t=input('enter string: ')
c=encryption(t,key); print(c); print(decryption(c,key))
