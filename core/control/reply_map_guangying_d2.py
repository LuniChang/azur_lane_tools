import win32api
import win32gui
import win32con
import time

from control.reply_map_common import ReplyMapCommon

import common.screen as screen


class ReplyGuangyiD2(ReplyMapCommon):

    # 进地图
    def clickMap(self):
        self._isNeedKeyMap = True
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(33, 75)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):

        isAtHome = self.matchResImgInWindow(
            "guangying/994d1b6664ae1c9b_0_0_20_15.png", 0.6)
        print("isAtHome", isAtHome)
        return isAtHome

    def isAtInMapReady(self):
        return self.matchResImgInWindow("guangying/ready_20_30_80_50.png")

    _exEnemys = [
        "enemy/sairen/a1a51f2787c34af2_45_65_55_75.png",
        "enemy/sairen/a7fe7ec37a200550_45_45_55_55.png",
        "enemy/sairen/a8a80f0bc9553fe3_45_65_55_75.png",
        "enemy/sairen/b7b60101cdea2fc6_45_45_55_55.png",
        "enemy/sairen/ec80f8ecc262aa3f_45_25_55_35.png",
        "enemy/sairen/ecb0f486332b17c5_45_35_55_45.png",
        "enemy/tiexie/d1_p1_47_47_54_54.png",
        "enemy/tiexie/d1_p2_47_47_54_54.png",
        "enemy/tiexie/d1_p3_47_47_54_54.png",
        "enemy/tiexie/d1_p4_47_47_54_54.png",
        "enemy/tiexie/d1_p5_47_47_54_54.png",
        "enemy/tiexie/d1_p6_47_47_54_54.png",
        "enemy/tiexie/d1_p7_47_47_54_54.png",

    ]

    _boss = [


    ]

    _findEnemysMode = 0

    def clickPoint(self):
        pass

    def setTeamPositionToSave(self):
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerLeftUp()

            time.sleep(5)
            self.leftClickPer(90, 75)
            time.sleep(15)

        return self.isInMap()
