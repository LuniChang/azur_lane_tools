import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyHongranD3(BaseControl):

  
  

    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval




   
    #进地图
    def clickD3(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(55), self.getPosY(40)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    
        self.resetCusor()    

    def intoD3(self):
        win32gui.SetForegroundWindow(self.handle)
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
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(65), self.getPosY(70)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
        self.resetCusor()  

    
    def run(self):    
        team1BattleCount=0
        team2BattleCount=0
        team1MoveCount=0
        team2MoveCount=0
        teamNum=1


        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
           
            #底部菜单hash 
            self.resetCusor() 
            print("isAtHome")
            if self.isAtHome():
                team1BattleCount=0
                team2BattleCount=0
                team1MoveCount=0
                team2MoveCount=0
                teamNum=1
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
            print("isNewMission")   
            if self.isNewMission():  
               self.leftClickPer(99,99)
               time.sleep(3)

            



 
            if self.onGetSR() or self.onGetSSR() :
                 
                self.clickOnGetSR()
                time.sleep(2)

           
            if self.onBattleEnd():  
               self.battleContinue()
               time.sleep(2)
            if self.onGetItems():   
               self.battleContinue()
               time.sleep(2)
               

            
            if self.onBattleEndCount():  
               print("onBattleEndCount") 
               if teamNum==1:
                  team1BattleCount=team1BattleCount+1
               else:
                  team2BattleCount=team2BattleCount+1  
               self.battleContinue()
               time.sleep(4)

            

           
            print("isInMap")
            if self.isInMap():
                if self.isNewMission():  
                    self.leftClickPer(99,99)
                    time.sleep(3)

                time.sleep(1)
                if teamNum==1:
                    print("team1MoveCount",team1MoveCount)
                    if team1MoveCount==0:
                        time.sleep(3)
                        self.resetTeamLocation()
                        self.moveRight(2)
                        self.moveRight(3)
                        self.resetTeamLocation()
                        self.moveUp(1)
                    if team1MoveCount==1:   #此处经常走不到
                        self.resetTeamLocation()
                        self.moveUp(1)
                    #走到无怪区域  
                    if team1MoveCount==2: 
                        self.resetTeamLocation()
                        self.moveUp(1)
                     
                    if team1MoveCount==3: 
                        self.resetTeamLocation()
                        self.moveLeft(1)

                    #切队
                    if team1MoveCount==4: 
                        self.switchTeam()
                        teamNum=2

                    if team1MoveCount==5: 
                        self.moveUp(1)
                    #此处最糟糕打了5次
                    if team1MoveCount==6: 
                        self.resetTeamLocation()
                        self.moveUp(1)
                    print("team1BattleCount",team1BattleCount)
                    if team1BattleCount<5:
                        if team1MoveCount==7: 
                            self.resetTeamLocation()
                            self.moveLeft(1)   
                        if team1MoveCount==8: 
                            self.resetTeamLocation()
                            self.moveLeft(1)
                        if team1MoveCount==9: 
                            self.moveLeft(2)

                        #这里还不够五次就下去回溯 
                        if team1MoveCount==10: 
                            self.resetTeamLocation() 
                            self.moveDown(1) 
                        #在中间    
                        if team1MoveCount==11: 
                            self.resetTeamLocation() 
                            self.moveRight(1) 
                        if team1MoveCount==12: 
                            self.moveRight(2) 
                        if team1MoveCount==13: 
                            self.resetTeamLocation() 
                            self.moveRight(1) 
                         
                        if team1MoveCount==14: 
                            self.resetTeamLocation() 
                            self.moveDown(1)
                        #在底部    
                        if team1MoveCount==15: 
                            self.resetTeamLocation() 
                            self.moveLeft(1) 
                        if team1MoveCount==16: 
                            self.moveLeft(2)     
                        if team1MoveCount==17: 
                            self.moveLeft(3) 
                        if team1MoveCount==18: 
                            self.resetTeamLocation() 
                            self.moveUp(1)
                        if team1MoveCount==19: 
                            self.resetTeamLocation() 
                            self.moveUp(1) 
                            team1MoveCount=9 #循环

                    else:      #这里够五次换队
                        # if team1MoveCount==7 or team1MoveCount==9 : #走上进安全区 （也可拖动走到起点待定）
                        #     self.resetTeamLocation() 
                        #     self.moveUp(1)
                        # if team1MoveCount>9:
                        #     self.resetTeamLocation() 
                        #     self.dragPer(50,90,50,40)
                        #     self.leftClickPer(50,60) 
                        #     time.sleep(10)    
                        self.resetTeamLocation() 
                        self.dragPer(50,90,50,30)
                        #需要做判断

                        if team1MoveCount<=9:
                           self.leftClickPer(50,85) 
                        if team1MoveCount>9 and team1MoveCount<15:
                           self.leftClickPer(50,70) 
                        if team1MoveCount>=15:
                           self.leftClickPer(50,55)    
                        time.sleep(15)
                        self.switchTeam()
                        teamNum=2
                   

                    team1MoveCount=team1MoveCount+1


                else:
                    print("team2MoveCount",team2MoveCount)
                    if team2MoveCount==0:
                        #往右走3格子
                        self.moveRight(2)
                        time.sleep(2)
                        self.moveRight(3)
                        #来回切换复位
                        self.resetTeamLocation()
                   
                    if team2MoveCount==1:
                        self.moveUp(1)

                    if team2MoveCount==2:
                        self.moveUp(2)
                    #往上3次到达安全区域 然后切队
                    if team2MoveCount==3:
                        self.resetTeamLocation()
                        self.moveUp(1)
                        self.switchTeam()
                        teamNum=1
                    #此处一队应打完五次    
                    if team2MoveCount==4:
                        self.moveLeft(1)
                    if team2MoveCount==5:
                        self.resetTeamLocation()
                        self.moveUp(1)   
                    if team2MoveCount==6:
                        self.resetTeamLocation()
                        self.moveUp(1)  
                    if team2MoveCount==7:
                        self.resetTeamLocation() 
                        self.moveLeft(1)  
                    if team2MoveCount==8:
                        self.moveLeft(2)    
                    if team2MoveCount==9:
                        self.resetTeamLocation() 
                        self.moveLeft(1)    

                    if team2BattleCount<2:
                            
                        if team2MoveCount==10:
                            self.resetTeamLocation(4)
                            self.moveDown(1)   
                        if team2MoveCount==11:
                            self.moveDown(2)   
                        if team2MoveCount==12:
                            self.resetTeamLocation(4)
                            self.moveRight(1)   
                        if team2MoveCount==13:
                            self.moveRight(2)  
                        if team2MoveCount==14:
                            self.moveRight(3)  
                        if team2MoveCount==15:
                            self.resetTeamLocation(4)
                            self.moveUp(1)    
                        if team2MoveCount==16:
                            self.moveUp(2) 
                        if team2MoveCount==17:
                            self.resetTeamLocation(4) 
                            team2MoveCount=6   
                            
                    if team2BattleCount==2:
                         self.leftClickPer(50,50)  
                        
                              
                    team2MoveCount=team2MoveCount+1  
                    
                     
            xylist= self.getBossLocation() 
            if  len(xylist)>0:
                x,y=xylist[0]
                self.leftClick(x,y)
              
                time.sleep(20)

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



