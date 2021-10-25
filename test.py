from os import name
import time 
import os.path
import shutil

timestr = time.strftime("%Y%m%d-%H%M%S")
username = 'juan'

imgMessage = 'venom.jpg'
name, ext = os.path.splitext(imgMessage)
print(ext)


filename = username + "-sent-" + timestr + ext

new_path = ".idea/inspectionProfiles/"+ filename
# shutil.copy2(imgMessage, f"fileSent/{filename}")
shutil.copy2(imgMessage, new_path)

# print(f"fileSent/{filename}")
