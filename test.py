import time
##

alpha = "abcdefghijklmnopqrstuvwxyz 0123456789&é'(-è_çà)=" ##the aplha
key = "qeyfmchoganlujxwbtkrzbvips 0123456789&é'(-è_çà)="   ##the alpha key
keyListTest = []
##

##

textC = "Hello World"   ##the text to encrypt
encrypted = ""  ##the text encrypted
decrypted = ""
textCList = []          ##the text to encrypt in list format

##


##

def crypt(lettre,keyVar, alphaVar):
    global encrypted
    for i in range(len(alpha)):
        if lettre == alpha[i]:
            encrypted = encrypted + keyVar[i]
        elif lettre == alpha[i].upper():
            encrypted = encrypted + keyVar[i].upper()
        

    
print("\n\n\n\n\t\t\tVoici le traducteur raskayen 1.0\t\t\t\n\n\n")
textC = input("\tVeuillez écrire votre message a crypter ici : ")
print("\n\tEncryption en cours ", ".", ".",".",".")
for i in range(len(textC)):
    crypt(textC[i], key , alpha)
time.sleep(0.5)
print("\n\n")
print("Message crypté : ", encrypted, "\n\n\n\n")
time.sleep(2.5)


