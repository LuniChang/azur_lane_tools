import win32api
import win32gui
import win32con
import time
import random

from control.base_control import BaseControl

import common.screen as screen




class ReplyMapCommonAuto(BaseControl):
    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval
    
    def run(self):
       
        win32gui.SetForegroundWindow(self.handle)
        while self._isRun:
            
 
            self.clickReAutoMap()

            time.sleep(self.interval)
    

   