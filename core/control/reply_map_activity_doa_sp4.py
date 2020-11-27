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
        self.leftClickPer(50, 50)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):

        isAtHome = self.matchResImgInWindow("act/doa/home_0_0_30_20.png", 0.6)
        print("isAtHome", isAtHome)
        return isAtHome

    def isAtInMapReady(self):
        return self.matchResImgInWindow("act/doa/ready_20_30_80_50.png")

    _exEnemys = [
        "act/doa/enemy/8c3456952c5f2d9b_45_55_52_65.png",
        "act/doa/enemy/8d0d8fa322bad873_45_35_52_45.png",
        "act/doa/enemy/8d85b3d8c6c78d8c_45_55_52_65.png",
        "act/doa/enemy/8d85f3d8ce818d8d_45_35_52_45.png",
        "act/doa/enemy/8e8efd95928b8d0a_45_35_52_45.png",
        "act/doa/enemy/9a1aa565f7c58d90_45_35_52_45.png",
        "act/doa/enemy/9a9aa5f3939990d2_45_55_52_65.png",
        "act/doa/enemy/9a86f3da66636702_45_55_52_65.png",
        "act/doa/enemy/9d1d4272ab65662e_45_45_52_55.png",
        "act/doa/enemy/9d058626375d5d4e_45_45_52_55.png",
        "act/doa/enemy/a0f3f1c18fe2f310_45_35_52_45.png",
        "act/doa/enemy/a25a9cafea05ab34_45_55_52_65.png",
        "act/doa/enemy/a63bd7075c434b58_45_35_52_45.png",
        "act/doa/enemy/a94a16354e6f4ee4_45_35_52_45.png",
        "act/doa/enemy/a8768eea437c0be1_45_45_52_53.png",
        "act/doa/enemy/bd1d9d2d65640656_45_45_52_55.png",
        "act/doa/enemy/bf1d43528a6c664e_45_35_52_45.png",
        "act/doa/enemy/bf1d855152d3d162_45_35_52_45.png",
        "act/doa/enemy/c0ce853f6e8b724c_45_45_52_55.png",
        "act/doa/enemy/c4c4b52ecb724c7c_45_45_52_53.png",
        "act/doa/enemy/c5a79427e91876c5_45_35_52_45.png",
        "act/doa/enemy/ccbc2e4a758c93ca_45_45_52_53.png",
        "act/doa/enemy/d6c1d29633e50cb9_45_45_52_55.png",
        "act/doa/enemy/de0a86c9f4f1a9e0_45_45_52_53.png",
        "act/doa/enemy/e294a0457e62b9f6_45_55_52_65.png",
        "act/doa/enemy/e53525c2e6c9163b_45_35_52_45.png",
        "act/doa/enemy/e65799e215aa32c5_45_45_52_53.png",
        "act/doa/enemy/ea6486a4e7a58793_45_45_52_55.png",
        "act/doa/enemy/ea6686a627a68796_45_45_52_55.png",
        "act/doa/enemy/ec6c8ccc4ca59793_45_35_52_45.png",
        "act/doa/enemy/ed44b033e527ca78_45_45_52_53.png",
        "act/doa/enemy/f40c26499ab579e3_45_55_52_65.png",
        "act/doa/enemy/ffc4902fcc3a9125_45_35_52_45.png",

    ]

    _boss = [
        "act/doa/boss/b96ed77ec1c82284_50_45_55_55.png",
        "act/doa/boss/e060826b9edb65b9_48_45_55_55.png",
        "act/doa/boss/e161976f9e586419_48_45_55_55.png",
        "act/doa/boss/ec6a956bb3944c46_45_45_55_55.png",
        "act/doa/boss/ee0a906bb3d74d06_45_45_55_55.png",

    ]

    _findEnemysMode = 0

    def clickPoint(self):
        pass

    def setTeamPositionToSave(self):
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerLeftDown()

            time.sleep(5)
            self.leftClickPer(90, 35)
            time.sleep(15)

        return self.isInMap()
