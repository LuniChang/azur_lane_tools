import win32api
import win32gui
import win32con
import time

from control.reply_map_common import ReplyMapCommon

import common.screen as screen


class ReplyMapActivity(ReplyMapCommon):

    # 进地图
    def clickMap(self):
        #win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(25, 35)
        self.resetCusor()

    def intoMap(self):
        #win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):
        return screen.autoCompareResImgHash(self.handle,"act/tiexie/map_c1_0_0_30_20.png",0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.handle, "act/tiexie/ready_20_30_80_80.png")



    _c1Enemys = [
            "enemy\\tiexie\\c1_p1_47_47_54_54.png",
            "enemy\\tiexie\\c1_p2_47_47_54_54.png",
            "enemy\\tiexie\\c1_p3_47_47_54_54.png",
            "enemy\\tiexie\\c1_p4_46_46_54_54.png",
            "enemy\\tiexie\\c1_p5_46_46_54_54.png",
            # "enemy\\tiexie\\c1_p6_47_47_54_54.png",

        ]

    def getEnemyLocation(self):

        imgs = self._c1Enemys+self._enemys

        # random.shuffle(imgs)
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.7)
            if len(xylist) > 0:
                return xylist

        return []



    def run(self):
        self._team1BattleCount = 0
        self._team2BattleCount = 0
        self._team1MoveCount = 0
        self._team2MoveCount = 0
        self._teamNum = 1

        while self._isRun:
            #win32gui.SetForegroundWindow(self.handle)

            # 底部菜单hash
            self.resetCusor()
            print("isAtHome")
            if self.isAtHome():
                self._team1BattleCount = 0
                self._team2BattleCount = 0
                self._team1MoveCount = 0
                self._team2MoveCount = 0
                self._teamNum = 1
                self.clickMap()
                time.sleep(2)

            print("isAtInMapReady")
            if self.isAtInMapReady():
                self._team1BattleCount = 0
                self._team2BattleCount = 0
                self._team1MoveCount = 0
                self._team2MoveCount = 0
                self._teamNum = 1
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
