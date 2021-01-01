import win32api
import win32gui
import win32con
import time

from control.reply_map_common import ReplyMapCommon

import common.screen as screen


class ReplyMapActivity(ReplyMapCommon):

    # 进地图
    def clickMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 38)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):

        isAtHome = self.matchResImgInWindow(
            "act/fuxiang/home_0_0_30_20.png", 0.6)
        print("isAtHome", isAtHome)
        return isAtHome

    def isAtInMapReady(self):
        return self.matchResImgInWindow("act/fuxiang/ready_20_30_80_50.png")

    _exEnemys = [
        "enemy/sairen/9a5f883fc03ec499_45_75_55_85.png",
        "enemy/sairen/a1a51f2787c34af2_45_65_55_75.png",
        "enemy/sairen/a7fe7ec37a200550_45_45_55_55.png",
        "enemy/sairen/a8a80f0bc9553fe3_45_65_55_75.png",
        "enemy/sairen/a8c7ae53e543e1c2_45_45_55_55.png",
        "enemy/sairen/a94a956a9e359327_45_25_55_35.png",
        "enemy/sairen/a95ad40df205ff21_45_25_55_35.png",
        "enemy/sairen/a957a75495e3c0e1_45_25_55_35.png",
        "enemy/sairen/a2568e6954a5fa55_45_75_55_85.png",
        "enemy/sairen/a44995378e539c5b_45_25_55_35.png",
        "enemy/sairen/ab5aac689934b956_45_25_55_35.png",
        "enemy/sairen/ac49956bd62a0b97_45_48_55_55.png",
        "enemy/sairen/ad4b95226f72a453_45_75_55_85.png",
        "enemy/sairen/ad5c916a576c142f_45_75_55_85.png",
        "enemy/sairen/ae54b56a04cfa5d8_45_48_55_55.png",
        "enemy/sairen/b7b60101cdea2fc6_45_45_55_55.png",
        "enemy/sairen/b6236d825bd013be_45_75_55_85.png",
        "enemy/sairen/c003eef8151d3dc7_45_25_55_30.png",
        "enemy/sairen/d0e591352e9a2f1b_45_48_55_55.png",
        "enemy/sairen/dedcb828c8e2b236_45_75_55_85.png",
        "enemy/sairen/dedcf868c8c2b232_45_75_55_85.png",
        "enemy/sairen/ea75aa5825df011d_45_48_55_55.png",
        "enemy/sairen/ec80f8ecc262aa3f_45_25_55_35.png",
        "enemy/sairen/ecb0f486332b17c5_45_35_55_45.png",
        "act/fuxiang/ead5f0f5f4f00206_45_25_55_30.png",
        "act/fuxiang/954481d73ac82ddf_45_75_55_85.png",
        "act/fuxiang/cccccece8d848d96_45_75_55_85.png",

    ]

    _boss = [
        "act/fuxiang/8dc98c59a761b569_45_35_55_50.png",

        "act/fuxiang/cdc9c9e12171e99a_45_35_55_50.png",

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
