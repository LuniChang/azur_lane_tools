import win32api
import win32gui
import win32con
import time

from control.reply_map_common import ReplyMapCommon

import common.screen as screen

class ReplyMapActivity(ReplyMapCommon):

  
  




   
    #进地图
    def clickMap(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(44), self.getPosY(34)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)   
        self.resetCusor()    

    def intoMap(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(70), self.getPosY(68)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      
        self.resetCusor()  

 

    def isAtHome(self):
        return self.matchResImgInWindow("map8//at_home_0_0_40_20.png")

    def isAtInMapReady(self):
        return self.matchResImgInWindow("map8//81ready_20_30_80_86.png")

   
  
    def run(self):    
        self._team1BattleCount=0
        self._team2BattleCount=0
        self._team1MoveCount=0
        self._team2MoveCount=0
        self._teamNum=1

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
           
            #底部菜单hash 
            self.resetCusor() 
            print("isAtHome")
            if self.isAtHome():
                self._team1BattleCount=0
                self._team2BattleCount=0
                self._team1MoveCount=0
                self._team2MoveCount=0
                self._teamNum=1
                self.clickMap()
                time.sleep(2)
             
            print("isAtInMapReady")
            if self.isAtInMapReady():
                self._team1BattleCount=0
                self._team2BattleCount=0
                self._team1MoveCount=0
                self._team2MoveCount=0
                self._teamNum=1
                self.intoMap()
                time.sleep(2)

            print("onSelectTeam")
            if self.onSelectTeam():  
               self.clickNeedLeaderCat()
               time.sleep(2)
               self.atTeamIntoMap()
               time.sleep(2)
               
           
            self.commonAction()

            

           
            print("isInMap")
            if self.isInMap():
                self.findAndBattle()
                

      


                
            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



