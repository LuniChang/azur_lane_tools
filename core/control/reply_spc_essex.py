import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen


class ReplySpcEssexD3(BaseControl):

    assignLevel = 0

    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def onSelectTeam(self):
        print("onSelectTeam")
        return screen.autoCompareResImgHash(self.handle, "spc_essex//on_select_team_78_82_90_88.png")

    def onReady(self):
        return screen.autoCompareResImgHash(self.handle, "spc_essex//ready_80_84_96_94.png")

    def clickBattle(self):
        self.leftClickPer(85, 90)

    def isAtHome(self):
        print("isAtHome")
        return screen.autoCompareResImgHash(self.handle, "spc_essex//at_home_10_10_50_30.png")

    def clickEx(self):
        self.leftClickPer(90, 20)

    def clickHard(self):
        self.leftClickPer(90, 45)

    def clickNormal(self):
        self.leftClickPer(90, 55)

    def clickEasy(self):
        self.leftClickPer(90, 70)

    def run(self):
        battleCount = 0
        toBattleLevel = 2
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)

            # 底部菜单hash
            self.resetCusor()

            if self.isAtHome():
  
                if self.assignLevel == 0:
                    if toBattleLevel == 1:
                        self.clickEx()
                    if toBattleLevel == 2:
                        self.clickHard()
                    if toBattleLevel == 3:
                        self.clickNormal()
                    if toBattleLevel == 4:
                        self.clickEasy()
                    battleCount = battleCount+1
                    toBattleLevel = int(battleCount/15)+2

                    if battleCount > 45:
                        battleCount = 0
                    pass

                if self.assignLevel == 1:
                    self.clickEx()

                if self.assignLevel == 2:
                    self.clickHard()

                if self.assignLevel == 3:
                    self.clickNormal()

                if self.assignLevel == 4:
                    self.clickEasy()

                time.sleep(2)

            if self.onSelectTeam():
                self.clickNeedLeaderCat()
                time.sleep(2)
                self.intoMap()
                time.sleep(2)

            if self.onReady():
                self.clickBattle()

            if self.onBattleEnd():
                self.battleContinue()
                time.sleep(2)

            if self.onGetItems():
                self.battleContinue()
                time.sleep(2)
            if self.onBattleEndCount():

                self.battleContinue()
                time.sleep(3)

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")
