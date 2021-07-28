import os
import time
import shutil
import time

import libs

if __name__ == "__main__":
    libs.clear()
    print("Live-Edit85")
    libs.enter()

    target = str(input("Target: "))
    copy = str(input("Data yang dicopy: "))
    libs.clear()

    if os.path.exists(target) and os.path.exists(copy):
        delay = float(input("Delay: "))

        while True:
            libs.clear()

            named_tuple = time.localtime()
            os.system("cp -r " + copy + " " + target)
            print("Date: " + time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple))
            print("From " + copy + " to " + target)
            print("OK!")
            time.sleep(delay)
    else:
        print(target)
        print("Target or Copy is not found!")
