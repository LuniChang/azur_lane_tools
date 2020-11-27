import win32api
import win32gui
import win32con
import time

from control.reply_map_common import  ReplyMapCommon

import common.screen as screen

class ReplyHongranD3(ReplyMapCommon):

  
  

    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval




   
    #进地图
    def clickD3(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(55), self.getPosY(40)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    
        self.resetCusor()    

    def intoD3(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(70), self.getPosY(70)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      
        self.resetCusor()  

    def isAtHome(self):
        return self.matchResImgInWindow("hongran//home_20_30_80_85.png")

    def isAtD3Ready(self):
        return self.matchResImgInWindow("hongran//d3_ready_20_20_80_80.png")

    def getBossLocation(self):
        return screen.matchResImgInWindow(self.handle,"hongran//boss_45_45_55_55.png")
   
    def needUseKey(self):
        return screen.autoCompareResImgHash(self.handle,"hongran//usekey_30_26_70_76.png")
    def useKey(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(65), self.getPosY(70)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
        self.resetCusor()  
    
    def findAndClickBoss(self):
        xylist= self.getBossLocation() 
        if  len(xylist)>0:
            x,y=xylist[0]
            self.leftClick(x,y)
            
            time.sleep(5)

    
    def setTeamPositionToSave(self): 
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerRightUp()

            time.sleep(5)
            self.leftClickPer(25, 97)
            time.sleep(15)

            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerRightDown()

            time.sleep(5)
            self.leftClickPer(40, 25)
            time.sleep(15)

        return  self.isInMap() 

    def setTeamPositionToBoss(self,code): 
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                if code ==1:
                   self.dragPerRightUp()
                else:
                   self.dragPerLeftUp()

            time.sleep(5)
            if code ==1:
                self.leftClickPer(25, 85)
            else:
                self.leftClickPer(75, 85)
            time.sleep(15)

        return  self.isInMap() 
        
          
    
    def run(self):    
        self._team1BattleCount=0
        self._team2BattleCount=0
        self._team1MoveCount=0
        self._team2MoveCount=0
        self._teamNum=1
     
        win32gui.SetForegroundWindow(self.handle)
        while self._isRun:
            
           
            #底部菜单hash 
            self.resetCusor() 
            print("isAtHome")
            if self.isAtHome():
                self._team1BattleCount=0
                self._team2BattleCount=0
                self._team1MoveCount=0
                self._team2MoveCount=0
                self._teamNum=1
                self.clickD3()
                time.sleep(2)
             
            print("isAtD3Ready")
            if self.isAtD3Ready():
               self.intoD3()
               time.sleep(2)

            print("onSelectTeam")
            if self.onSelectTeam():  
               self.clickNeedLeaderCat()
               time.sleep(2)
               self.intoMap()
               time.sleep(2)
               
            print("needUseKey")   
            if self.needUseKey():  
               self.useKey()
               time.sleep(10)
            
            self.commonAction()
            
            self.findAndClickBoss()
           
            print("isInMap")
            if self.isInMap():
                # self.leftClickPer(99, 99)
                time.sleep(4)
                if self.isNewMission():  
                    self.leftClickPer(99,99)
                    time.sleep(3)
               
                # time.sleep(1)
                if self._teamNum==1:
                    print("self._team1MoveCount",self._team1MoveCount)
                    if self._team1MoveCount==0:
                        # time.sleep(3)
                        self.resetTeamLocation()
                        self.moveRight(2)
                        self.moveRight(3)
                        self.resetTeamLocation()
                        self.moveUp(1)
                    if self._team1MoveCount==1:   
                        self.resetTeamLocation()
                        self.moveUp(1)
                    #走到无怪区域  
                    if self._team1MoveCount==2: 
                        self.resetTeamLocation()
                        self.moveUp(1)
                     
                    if self._team1MoveCount==3: 
                        self.resetTeamLocation()
                        self.moveLeft(1)

                    #切队
                    if self._team1MoveCount==4: 
                        self.switchTeam()
                        self._teamNum=2

                    if self._team1MoveCount==5: 
                        self.moveUp(1)
                    #此处最糟糕打了5次
                    if self._team1MoveCount==6: 
                        self.resetTeamLocation()
                        self.moveUp(1)

                    print("self._team1BattleCount",self._team1BattleCount)
                    if self._team1BattleCount<5:
                        if self._team1MoveCount==7: 
                            self.resetTeamLocation()
                            self.moveLeft(1)   
                        if self._team1MoveCount==8: 
                            self.resetTeamLocation()
                            self.moveLeft(1)
                        if self._team1MoveCount==9: 
                            self.moveLeft(2)

                        #这里还不够五次就下去回溯 
                        if self._team1MoveCount==10: 
                            self.resetTeamLocation() 
                            self.moveDown(1) 
                        #在中间    
                        if self._team1MoveCount==11: 
                            self.resetTeamLocation() 
                            self.moveRight(1) 
                        if self._team1MoveCount==12: 
                            self.moveRight(2) 
                        if self._team1MoveCount==13: 
                            self.resetTeamLocation() 
                            self.moveRight(1) 
                         
                        if self._team1MoveCount==14: 
                            self.resetTeamLocation() 
                            self.moveDown(1)
                        #在底部    
                        if self._team1MoveCount==15: 
                            self.resetTeamLocation() 
                            self.moveLeft(1) 
                        if self._team1MoveCount==16: 
                            self.moveLeft(2)     
                        if self._team1MoveCount==17: 
                            self.moveLeft(3) 
                        if self._team1MoveCount==18: 
                            self.resetTeamLocation() 
                            self.moveUp(1)
                        if self._team1MoveCount==19: 
                            self.resetTeamLocation() 
                            self.moveUp(1) 
                            self._team1MoveCount=9 #循环

                    else:      #这里够五次换队
                        # if  self._team2MoveCount==6 :
                        #     self.switchTeam()
                        #     self._teamNum=2
                        # else :
                        # self.resetTeamLocation() 
                        self.setTeamPositionToSave()
                        time.sleep(15)
                        self.switchTeam()
                        self._teamNum=2
                   

                    self._team1MoveCount=self._team1MoveCount+1


                else:
                    print("self._team2MoveCount",self._team2MoveCount)
                    if self._team2MoveCount==0:
                        #往右走3格子
                        self.moveRight(2)
                        time.sleep(2)
                        self.moveRight(3)
                        #来回切换复位
                        self.resetTeamLocation()
                   
                    if self._team2MoveCount==1:
                        self.moveUp(1)

                    if self._team2MoveCount==2:
                        self.moveUp(2)
                    #往上3次到达安全区域 然后切队
                    if self._team2MoveCount==3:
                        self.resetTeamLocation()
                        self.moveUp(1)
                        self.switchTeam()
                        self._teamNum=1
                    #此处一队应打完五次    
                    if self._team2MoveCount==4:
                        self.moveLeft(1)

                    
                    # if self._team2MoveCount==5:
                        # self.switchTeam()
                        # self._teamNum=1
                        
                    if self._team2MoveCount==6:
                        self.resetTeamLocation()
                        self.moveUp(1)   
                    if self._team2MoveCount==7:
                        self.resetTeamLocation()
                        self.moveUp(1)  
                    if self._team2MoveCount==8:
                        self.resetTeamLocation() 
                        self.moveLeft(1)  
                    if self._team2MoveCount==9:
                        self.moveLeft(2)    
                    if self._team2MoveCount==10:
                        self.resetTeamLocation() 
                        self.moveLeft(1)    

                    if self._team2BattleCount<2:
                            
                        if self._team2MoveCount==11:
                            self.resetTeamLocation(4)
                            self.moveDown(1)   
                        if self._team2MoveCount==12:
                            self.resetTeamLocation(4)
                            self.moveRight(1)   
                        if self._team2MoveCount==13:
                            self.moveRight(2)  
                        if self._team2MoveCount==14:
                            self.moveRight(3)  
                        if self._team2MoveCount==15:
                            self.resetTeamLocation(4)
                            self.moveDown(1)    
                        if self._team2MoveCount==16:
                            self.resetTeamLocation(4) 
                            self.moveLeft(1) 
                        if self._team2MoveCount==17:
                            self.resetTeamLocation(4) 
                            self.moveLeft(1) 
                        if self._team2MoveCount==18:
                            self.moveLeft(2) 
                        if self._team2MoveCount==19:
                            self.moveLeft(3)
                        if self._team2MoveCount==20:
                            self.resetTeamLocation(4) 
                            self.moveUp(1) 

                        if self._team2MoveCount==21:
                            self.moveUp(2)  
                            self._team2MoveCount=10


                         
                            
                    if self._team2BattleCount==2:
                         self.leftClickPer(50,50)  
                         self.findAndClickBoss()
                         self.setTeamPositionToBoss(1)
                         time.sleep(10)
                         if self.isInMap():
                            self.setTeamPositionToBoss(2)
                        #  self.resetMapPosition()
                        #  self.scranDragMap()
                        
                              
                    self._team2MoveCount=self._team2MoveCount+1  
                    
                     
            self.findAndClickBoss()

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



