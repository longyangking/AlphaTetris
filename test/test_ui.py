import sys
sys.path.append("..")

import alphatetrix
import time
import numpy as np


if __name__ == "__main__":
    shape = (20,50)
    area = np.random.randint(8,size=shape)
    sizeunit = 10
    ui = alphatetrix.ui.UI(pressaction=lambda x:x,area=area,sizeunit=sizeunit)
    ui.start()

    for _ in range(10):
        time.sleep(0.5)
        ui.setarea(area=np.random.randint(6,size=shape))
    ui.gameend(10)
