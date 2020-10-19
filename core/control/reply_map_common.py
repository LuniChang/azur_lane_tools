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

    _enemys = [

        "enemy\\ship_h1_45_45_55_55.png",
        "enemy\\ship_h2_45_45_55_55.png",
        "enemy\\ship_h3_47_47_54_54.png",
        "enemy\\ship_q1_45_45_55_55.png",
        "enemy\\ship_q2_45_45_55_55.png",
        "enemy\\ship_q3_47_47_54_54.png",
        "enemy\\ship_q4_46_46_53_53.png",
        "enemy\\ship_q5_46_46_53_53.png",
        "enemy\\ship_y1_46_46_53_53.png",
        "enemy\\ship_y2_46_46_53_53.png",
        "enemy\\ship_y3_46_46_53_53.png",
        "enemy\\ship_y4_45_45_55_55.png",
        "enemy\\ship_y5_45_45_53_53.png",
        "enemy\\ship_z1_45_45_55_55.png",
        "enemy\\ship_z2_45_45_55_55.png",
        "enemy\\ship_z3_45_45_55_55.png",
        "enemy\\ship_z4_46_46_53_53.png",
        "enemy\\ship_z4_47_47_54_54.png",
        "enemy\\ship_z5_46_46_53_53.png",
        "enemy\\ship_z5_47_47_54_54.png",
        "enemy\\ship_z6_46_46_53_53.png",
        "enemy\\ship_z6_47_47_54_54.png",
    ]

    _boss = ["enemy\\boss_48_45_52_55.png",
             "enemy\\boss1_47_47_54_54.png",
             "enemy\\boss2_47_47_54_54.png",
             "enemy\\boss3_47_47_52_52.png",
             "enemy\\boss4_46_46_50_52.png",

             ]
    _exEnemys = [


    ]
    
    def getEnemyLocation(self):

        imgs = self._enemys+self._exEnemys 

        # random.shuffle(imgs)
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.7)
            if len(xylist) > 0:
                return xylist

        return []

    def getBossLocation(self):
        imgs = self._boss

        random.shuffle(imgs)
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.7)
            if len(xylist) > 0:
                return xylist

        return []

    def dragPerLeft(self):
        self.dragPer(10, 50, 80, 50)

    def dragPerRight(self):
        self.dragPer(80, 50, 10, 50)

    def dragPerUp(self):
        self.dragPer(50, 20, 50, 70)

    def dragPerLeftUp(self):
        self.dragPer(10, 20, 80, 70)

    def dragPerRightUp(self):
        self.dragPer(80, 20, 10, 70)

    def dragPerDown(self):
        self.dragPer(50, 70, 50, 20)

    def dragPerLeftDown(self):
        self.dragPer(10, 70, 80, 20)

    def resetMapPosition(self):
        if not self._isScranMap:

            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerLeftUp()

            self._needResetMap = False
            self._scranMapEnd = False
            self._scranDirection = 0

    def setTeamPositionToSave(self):
        return True


    def scranDragMap(self):  # 全图扫描
        winHash = screen.winScreenHash(self.handle)
        self._isScranMap = True
        if self._scranDirection == RIGHT:
            self.dragPerRight()

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                self._nextScranDirection = LEFT
                self._scranDirection = DOWN
                return
        if self._scranDirection == DOWN:
            self.dragPerDown()
            # 换方向左右

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                self._isScranMap = False  # 扫完全图
                return

            self._scranDirection = self._nextScranDirection
        if self._scranDirection == LEFT:
            self.dragPerLeft()

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                self._nextScranDirection = RIGHT  # 左边到尽头 下去后往右
                self._scranDirection = DOWN
                return

    def findAndBattle(self):

        if self._teamNum == 1:
            if self._team1BattleCount < self.team1BattleMaxCount:
                xylist = self.getEnemyLocation()
                minX = self.getPosX(15)
                # maxY=self.getPosY(80)
                resList = []
                for point in xylist:
                    if point[0] >= minX:
                        resList.append(point)
                if len(resList) > 0 and not self.isSameWin():
                    x, y = resList[0]
                    # self.leftClick(x, y)
                    cx = self.getPosX(50)
                    cy = self.getPosY(50)
                    self.drag(x, y, cx, cy)  # 拖动不是一比一 大概是一半
                    time.sleep(2)
                    self.drag(x, y, cx, cy)
                    self.leftClick(cx, cy)
                    time.sleep(5)
                else:
                    if self.isSameWin():
                        self.setTeamPositionToSave()
                    self.resetMapPosition()
                    self.scranDragMap()

            else:
                time.sleep(10)
                if self.setTeamPositionToSave():
                    self.switchTeam()
                    self._teamNum = 2

               

        if self._teamNum == 2:
            if self._team2BattleCount < self.team2BattleMaxCount:
                xylist = self.getEnemyLocation()
                minX = self.getPosX(15)
                # maxY=self.getPosY(80)
                resList = []
                for point in xylist:
                    if point[0] >= minX:
                        resList.append(point)
                if len(resList) > 0:
                    x, y = resList[0]

                    cx = self.getPosX(50)
                    cy = self.getPosY(50)
                    self.drag(x, y, cx, cy)  # 拖动不是一比一 大概是一半
                    time.sleep(2)
                    self.drag(x, y, cx, cy)
                    self.leftClick(cx, cy)
                    time.sleep(5)
                else:
                    self.resetMapPosition()
                    self.scranDragMap()
            else:
                xylist = self.getBossLocation()
                minX = self.getPosX(15)
                # maxY=self.getPosY(80)
                resList = []
                for point in xylist:
                    if point[0] >= minX:
                        resList.append(point)
                if len(resList) > 0:
                    x, y = resList[0]
                    self.leftClick(x, y)
                    time.sleep(5)
                else:
                    self.resetMapPosition()
                    self.scranDragMap()
