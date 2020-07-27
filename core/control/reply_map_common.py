import win32api
import win32gui
import win32con
import time
import random

from control.base_control import BaseControl

import common.screen as screen

RIGHT = 0
DOWN = 1
LEFT = 2


class ReplyMapCommon(BaseControl):

    _scranDirection = 0  # 0 → 1 ↓ 2←
    _nextScranDirection = 0
    _isScranMap = False

    team1BattleMaxCount = 5
    team2BattleMaxCount = 0

    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def getEnemyLocation(self):

        imgs = ["enemy\\ship_p1_45_45_55_55.png",
                "enemy\\ship_p2_45_45_55_55.png",
                "enemy\\ship_p3_45_45_55_55.png",
                "enemy\\ship_p4_45_45_55_55.png",
                "enemy\\ship_z1_45_45_55_55.png",
                "enemy\\ship_z2_45_45_55_55.png",
                "enemy\\ship_z3_45_45_55_55.png",
                "enemy\\ship_h1_45_45_55_55.png",
                "enemy\\ship_h1_45_45_55_55.png",
                "enemy\\ship_h2_45_45_55_55.png",
                "enemy\\ship_q1_45_45_55_55.png",
                "enemy\\ship_q2_45_45_55_55.png",
                ]

        random.shuffle(imgs)
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i],0.5)
            if len(xylist) > 0:
                return xylist
  
 

        return []

    def getBossLocation(self):
        xylist = screen.matchResImgInWindow(
            self.handle, "enemy\\d1_4_boss_45_45_55_55.png", 0.6)
        if len(xylist) > 0:
            return xylist
        xylist = screen.matchResImgInWindow(
            self.handle, "enemy\\d1_2_boss_45_45_55_55.png", 0.6)
        if len(xylist) > 0:
            return xylist
        xylist = screen.matchResImgInWindow(
            self.handle, "enemy\\d1_3_boss_45_45_55_55.png", 0.6)
        if len(xylist) > 0:
            return xylist
        xylist = screen.matchResImgInWindow(
            self.handle, "enemy\\boss_48_45_52_55.png", 0.6)
        if len(xylist) > 0:
            return xylist

        return []

    def dragPerLeft(self):
        self.dragPer(10, 50, 80, 50)

    def dragPerRight(self):
        self.dragPer(80, 50, 10, 50)

    def dragPerUp(self):
        self.dragPer(50, 20, 50, 70)

    def dragPerDown(self):
        self.dragPer(50, 70, 50, 20)

    def resetMapPosition(self):
        if not self._isScranMap:
            winHash = ""
            while  not screen.alikeHash(winHash ,screen.winScreenHash(self.handle),0.9) :
                self.dragPerUp()
                time.sleep(0.5)
                winHash = screen.winScreenHash(self.handle )
            while not screen.alikeHash(winHash ,screen.winScreenHash(self.handle),0.9) :
                self.dragPerLeft()
                time.sleep(0.5)
                winHash = screen.winScreenHash(self.handle )
            self._needResetMap = False
            self._scranMapEnd = False
            self._scranDirection = 0

    def scranDragMap(self):  # 全图扫描
        winHash = screen.winScreenHash(self.handle )
        self._isScranMap = True
        if self._scranDirection == RIGHT:
            self.dragPerRight()
            time.sleep(0.5)
            if screen.alikeHash(winHash ,screen.winScreenHash(self.handle),0.9) :
                self._nextScranDirection = LEFT
                self._scranDirection = DOWN
                return
        if self._scranDirection == DOWN:
            self.dragPerDown()
            # 换方向左右
            time.sleep(0.5)
            if screen.alikeHash(winHash ,screen.winScreenHash(self.handle),0.9) :
                self._isScranMap = False  # 扫完全图
                return

            self._scranDirection = self._nextScranDirection
        if self._scranDirection == LEFT:
            self.dragPerLeft()
            time.sleep(0.5)
            if screen.alikeHash(winHash ,screen.winScreenHash(self.handle),0.9) :
                self._nextScranDirection = RIGHT  # 左边到尽头 下去后往右
                self._scranDirection = DOWN
                return

    def findAndBattle(self):

        if self._teamNum == 1:
            if self._team1BattleCount < self.team1BattleMaxCount:
                xylist = self.getEnemyLocation()
                if len(xylist) > 0:
                    x, y = xylist[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else:
                    self.resetMapPosition()
                    self.scranDragMap()

            else:
                time.sleep(1)
                self.switchTeam()
                self._teamNum = 2

        if self._teamNum == 2:
            if self._team2BattleCount < self.team2BattleMaxCount:
                xylist = self.getEnemyLocation()
                if len(xylist) > 0:
                    x, y = xylist[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else:
                    self.resetMapPosition()
                    self.scranDragMap()
            else:
                xylist = self.getBossLocation()
                if len(xylist) > 0:
                    x, y = xylist[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else:
                    self.resetMapPosition()
                    self.scranDragMap()
