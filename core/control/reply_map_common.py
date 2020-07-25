import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

RIGHT=0
DOWN=1
LEFT=2

class ReplyMapCommon(BaseControl):

  
    _scranDirection = 0  # 0 → 1 ↓ 2←
    _nextScranDirection = 0
    _isScranMap = False
     
    
    team1BattleMaxCount = 5
    team2BattleMaxCount = 5


    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def getEnemyLocation(self):
        return screen.matchResImgInWindow(self.handle, "map//boss_48_45_54_55.png")  \
            or screen.matchResImgInWindow(self.handle, "map//boss_48_45_54_55.png") \
            or screen.matchResImgInWindow(self.handle, "map//boss_48_45_54_55.png") \
            or screen.matchResImgInWindow(self.handle, "map//boss_48_45_54_55.png")

    def getLocation(self):
        return screen.matchResImgInWindow(self.handle, "map//boss_48_45_54_55.png")

    def dragPerLeft(self):
        self.dragPer(10, 50, 80, 50)

    def dragPerRight(self):
        self.dragPer(80, 50, 10, 50)

    def dragPerUp(self):
        self.dragPer(50, 20, 50, 70)

    def dragPerDown(self):
        self.dragPer(50, 70, 50, 20)

    def resetMapPosition(self):
        if  not self._isScranMap:
            winHash = ""
            while winHash != screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self.dragPer(20, 20, 70, 70)
                winHash = screen.winScreenRectHash(self.handle, 0, 0, 50, 50)
            self._needResetMap = False
            self._scranMapEnd = False
            self._scranDirection = 0

    def scranDragMap(self):  # 全图扫描
        winHash = screen.winScreenRectHash(self.handle, 0, 0, 50, 50)
        self._isScranMap=True
        if self._scranDirection == RIGHT:
            self.dragPerRight()
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._nextScranDirection = LEFT
                self._scranDirection = DOWN
                return
        if self._scranDirection == DOWN:
            self.dragPerDown()
            # 换方向左右
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._isScranMap = False  # 扫完全图
                return

            self._scranDirection = self._nextScranDirection
        if self._scranDirection == LEFT:
            self.dragPerLeft()
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._nextScranDirection = RIGHT  # 左边到尽头 下去后往右
                self._scranDirection = DOWN
                return

    def findAndBattle(self):
        
        self.commonAction()

        if self._teamNum == 1 :
            if self._team1BattleCount < self.team1BattleMaxCount:
                xylist = self.getEnemyLocation()()
                if len(xylist) > 0:
                    x,y=xylist[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else :
                    self.resetMapPosition()
                    self.scranDragMap()

                
            else :
                self.switchTeam()

        if self._teamNum == 2 :
            if self._team2BattleCount < self.team2BattleMaxCount:
                xylist = self.getEnemyLocation()()
                if len(xylist) > 0:
                    x,y=xylist[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else :
                    self.resetMapPosition()
                    self.scranDragMap()
          