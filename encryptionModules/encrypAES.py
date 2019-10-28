import pyAesCrypt
import os

if __name__ == "__main__":
    
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
        encryptThis = "keys.txt"     #target
        global encryptDone 
        encryptDone = str(encryptThis + ".sss")
        pyAesCrypt.encryptFile(encryptThis, encryptDone, key, bufferSize)


    def destroyKey():
        #removing the plain text key file immediately after usage
        if os.path.exists("keys.txt"):
            os.remove("keys.txt")
        else:
            pass


    # decryption
    def aesDecrypt():
        decryptThis = encryptDone
        pyAesCrypt.decryptFile(decryptThis, "recover.txt", key, bufferSize)

    aesEncrypt()
    destroyKey()
    aesDecrypt()