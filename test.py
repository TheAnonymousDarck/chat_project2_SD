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

# Load Pic
# picture = QPixmap("background.png")

# # set up the label widget to display the pic
# label = QLabel(window)
# label.setPixmap(picture)
# label.setGeometry(QtCore.QRect(10, 40, picture.width(), picture.height()))

# embiggen the window to correctly fit the pic
# window.resize(picture.width()+20, picture.height()+100)