import win32api
import win32gui
import win32con
import time

from control.reply_map_common import ReplyMapCommon

import common.screen as screen


class ReplyMapActivity(ReplyMapCommon):

    # 进地图
    def clickMap(self):
        screen.setForegroundWindow(self.getHandle())
        self.leftClickPer(65, 65)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.getHandle())
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):
        return screen.autoCompareResImgHash(self.getHandle(), "act/sp_huapohaikong/home_0_0_30_20.png", 0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.getHandle(), "act/sp_huapohaikong/ready_30_30_80_50.png")

    _boss = [
        "act/sp_huapohaikong/boss1_50_45_55_55.png",
        "act/sp_huapohaikong/boss2_50_45_55_56.png",
        "act/sp_huapohaikong/boss3_50_48_55_56.png",
        "act/sp_huapohaikong/boss4_45_40_55_55.png",
        "act/sp_huapohaikong/boss5_45_45_55_55.png",
        "act/sp_huapohaikong/boss6_45_45_55_55.png",
        "act/sp_huapohaikong/boss7_45_45_55_55.png",
    ]

    _exEnemys = [
        "act/sp_huapohaikong/air1_46_46_53_53.png",
        "act/sp_huapohaikong/air2_46_46_53_53.png",
        "act/sp_huapohaikong/air3_46_46_53_53.png",
        "act/sp_huapohaikong/air4_46_46_53_53.png",

    ]

    def setTeamPositionToSave(self):
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.getHandle()), 0.8):
                winHash = screen.winScreenHash(self.getHandle())
                self.dragPerRightUp()

            time.sleep(5)
            self.leftClickPer(30, 60)
            time.sleep(15)

        return  self.isInMap()   

    def run(self):
        self._team1BattleCount = 0
        self._team2BattleCount = 0
        self._team1MoveCount = 0
        self._team2MoveCount = 0
        self._teamNum = 1

        while self._isRun:
            win32gui.SetForegroundWindow(self.getHandle())
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
            # screen.grabCaptureDir(self.getHandle(),"reply_battle")
