import pyAesCrypt
import os
import time

def test():
        print("success")

target = "pic.png"
    
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

try:
    fileRef = open("keys.txt", "r")
    keyList = fileRef.readlines()
    key = keyList[0]
    fileRef.close()

except:
    #Checking if it is already been executed
    print("Already nuked")
    quit()

# encryption
def aesEncrypt():
    encryptThis = target     #target
    global encryptDone 
    encryptDone = str(encryptThis + ".sss")
    pyAesCrypt.encryptFile(encryptThis, encryptDone, key, bufferSize)


def destroyOriginal():
#removing the plain text key file immediately after usage
    if os.path.exists(target):
        os.remove(target)
    else:
        pass

# decryption
def aesDecrypt():
    decryptThis = encryptDone
    pyAesCrypt.decryptFile(decryptThis, target , key, bufferSize)

    

aesEncrypt()
destroyOriginal()
#time.sleep(10)
aesDecrypt()