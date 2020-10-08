import win32api
import win32gui
import win32con
import time
import random
from control.reply_map_common import ReplyMapCommon

import common.screen as screen


class ReplyMap72(ReplyMapCommon):

    # 进地图
    def clickMap(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(35, 35)
        self.resetCusor()

    def intoMap(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):
        return screen.autoCompareResImgHash(self.handle, "map7/on_map_0_0_30_20.png", 0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.handle, "map7/ready_20_30_80_50.png")

    _c1Enemys = [
        "map7/point_45_45_55_55.png",
        "map7/point2_45_45_55_55.png",
        # "map7/point3_47_47_54_54.png",
        "map7/point_45_38_55_55.png",
    ]
    _boss = ["map7/boss3_45_45_55_55.png",
             "map7/boss2_45_45_55_55.png",
             "map7/boss1_45_45_55_55.png",
             "enemy\\boss_48_45_52_55.png",
             "enemy\\boss1_47_47_54_54.png",
             "enemy\\boss2_47_47_54_54.png",
             "enemy\\boss3_47_47_52_52.png",
             "enemy\\boss4_46_46_50_52.png",
             ]

    # _lastWinHash=""
    def getEnemyLocation(self):

        # imgs = self._c1Enemys+self._enemys
        # winHash=screen.winScreenHash(self.handle)
        # if screen.alikeHash( self._lastWinHash, winHash, 0.8):

        #    imgs=self._enemys
        #    random.shuffle(imgs)

        # self._lastWinHash=winHash
        imgs = self._enemys
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.8)
            if len(xylist) > 0:
                return xylist

        return []

    def clickPoint(self):
        imgs = self._c1Enemys
       
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.8)
            if len(xylist) > 0:
                x, y = xylist[0]
                self.leftClick(x, y)
                time.sleep(10)

    def run(self):
        self._team1BattleCount = 0
        self._team2BattleCount = 0
        self._team1MoveCount = 0
        self._team2MoveCount = 0
        self._teamNum = 1

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)

            # 底部菜单hash
            self.resetCusor()

            if self.isAtHome():
                print("isAtHome")
                self._team1BattleCount = 0
                self._team2BattleCount = 0
                self._team1MoveCount = 0
                self._team2MoveCount = 0
                self._teamNum = 1
                self.clickMap()
                time.sleep(2)

            if self.isAtInMapReady():
                print("isAtInMapReady")
                self._team1BattleCount = 0
                self._team2BattleCount = 0
                self._team1MoveCount = 0
                self._team2MoveCount = 0
                self._teamNum = 1
                self.intoMap()
                time.sleep(2)

            if self.onSelectTeam():
                print("onSelectTeam")
                self.clickNeedLeaderCat()
                time.sleep(2)
                self.atTeamIntoMap()
                time.sleep(2)

            self.commonAction()

            if self.isInMap():
                print("isInMap")
                self.clickPoint()
                self.findAndBattle()

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")
