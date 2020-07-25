import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyMap81(BaseControl):

  
  

    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval




   
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

    def getBossLocation(self):
        return screen.matchResImgInWindow(self.handle,"map8//boss_48_45_54_55.png")
   

   
  
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
                self.leftClickPer(99,99)
                time.sleep(2)
                if self.isNewMission():  
                    self.leftClickPer(99,99)
                time.sleep(2)
                # time.sleep(1)
                if self._teamNum==1:
                    print("self._team1MoveCount",self._team1MoveCount)
                    if self._team1MoveCount==0:
                        time.sleep(3)
                        self.resetTeamLocation()
                        self.moveRight(1)
                        self.resetTeamLocation()
                        self.moveDown(1)
                        self.moveDown(2)#B1
                    if self._team1MoveCount==1:   
                        self.resetTeamLocation()
                        self.moveRight(1)
                     #走到无怪区域 
                    if self._team1MoveCount==2: 
                        self.moveRight(2)
                    if self._team1MoveCount==3: #E3
                        self.resetTeamLocation()
                        self.moveRight(1)

                    #切队
                    if self._team1MoveCount==4: 
                        self.switchTeam()
                        self._teamNum=2

                    if self._team1MoveCount==5: #E2
                        self.moveUp(1)
               
                    if self._team1MoveCount==6: #F2
                        self.resetTeamLocation()
                        self.moveRight(1)
                    if self._team1MoveCount==7: #F1
                        self.resetTeamLocation()
                        self.moveUp(1)
                        self.switchTeam()
                        self._teamNum=2

                    if self._team1BattleCount+self._team2BattleCount<4:
                 
                        if self._team1MoveCount==8:  #G1
                            self.resetTeamLocation()
                            self.moveRight(1)
                        if self._team1MoveCount==9:  #G2
                            self.resetTeamLocation()
                            self.moveDown(1)
                        if self._team1MoveCount==10:  #G3
                            self.moveDown(2)
                        if self._team1MoveCount==11:  #H3
                            self.resetTeamLocation()
                            self.moveRight(1)
                        if self._team1MoveCount==12:  #H2
                            self.resetTeamLocation()
                            self.moveUp(1)
                        if self._team1MoveCount==13:  #E2
                            self.resetTeamLocation()
                            self.moveLeft(1)
                        if self._team1MoveCount==14:  #G1
                            self.resetTeamLocation()
                            self.moveUp(1)    
                        if self._team1MoveCount==15:  #E1
                            self.resetTeamLocation()
                            self.moveLeft(2)
                        if self._team1MoveCount==16:  #E2
                            self.resetTeamLocation()
                            self.moveDown(1)
                        if self._team1MoveCount==17:  #E3
                            self.moveDown(2)
                        if self._team1MoveCount==18:  #E2
                            self.resetTeamLocation()
                            self.moveUp(1)
                        if self._team1MoveCount==19:  #E1
                            self.resetTeamLocation()
                            self.moveUp(1)
                        if self._team1MoveCount==20:  #E1
                            self.resetTeamLocation()
                            self.moveRight(1)
                            self._team1MoveCount=7 #循环

                    else:      #这里够4次换队
  
   
                        self.switchTeam()
                        self._teamNum=2
                   

                    self._team1MoveCount=self._team1MoveCount+1


                else:
                    print("self._team2MoveCount",self._team2MoveCount)
                    if self._team2MoveCount==0:
                        #往右走1格子
                        self.moveRight(1)
                        self.resetTeamLocation()
                        self.moveDown(1)
    
                    if self._team2MoveCount==1:#B3
                        self.moveDown(2)

                    if self._team2MoveCount==2:
                        self.resetTeamLocation()
                        self.moveRight(1)
                
                    #此处无怪
                    if self._team2MoveCount==3:#D3
                        self.moveRight(2)
                        self._teamNum=1
                        self.switchTeam()
                        
                    if self._team2MoveCount==4:#E3
                        self.moveRight(1)

                    if self._team2MoveCount==5:#E2
                        self.resetTeamLocation()
                        self.moveUp(1)   
                    if self._team2MoveCount==6:#F2  无怪
                        self.resetTeamLocation()
                        self.moveRight(1)  
                    if self._team2MoveCount==7:#F2  无怪
                        self.switchTeam()
                        self._teamNum=1
                    if self._team2MoveCount==8:#H2  无怪
                        self.resetTeamLocation()
                        self.moveRight(1)  
                    if self._team2MoveCount==9:#I2  
                        # self.resetTeamLocation()
                        self.moveRight(2) 
                    if self._team2MoveCount==10:#J2  
                        self.resetTeamLocation()
                        self.moveRight(1)        
                    self._team2MoveCount=self._team2MoveCount+1   

            xylist= self.getBossLocation() 
            if  len(xylist)>0:
                x,y=xylist[0]
                self.leftClick(x,y)
                
                time.sleep(5)


                
            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



