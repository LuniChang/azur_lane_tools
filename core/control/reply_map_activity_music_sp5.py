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
        return screen.autoCompareResImgHash(self.handle, "act/music/map_0_0_30_20.png", 0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.handle, "act/music/ready_20_30_80_50.png")

    _exEnemys = [
        "act/music/enemy/8a8ae86179bd9d38_46_76_54_86.png",
        "act/music/enemy/8ae5148079a2e7bf_46_76_54_86.png",
        "act/music/enemy/9a9a82a4961e9f1f_46_34_54_44.png",
        "act/music/enemy/9a996d68693d1c69_46_34_54_44.png",
        "act/music/enemy/9a82697b613d2f91_46_46_54_54.png",
        "act/music/enemy/9e9e9eaeae0a4a41_46_34_54_44.png",
        "act/music/enemy/94c5029e7f71a4ce_45_45_55_55.png",
        "act/music/enemy/94c5459659b1f1c7_46_46_54_54.png",
        "act/music/enemy/95e575168a0ab975_46_34_54_44.png",
        "act/music/enemy/805d9e3de0495bea_46_46_54_56.png",
        "act/music/enemy/8879c2652b33c73b_46_46_54_56.png",
        "act/music/enemy/9899e161c1d7c747_46_46_54_54.png",
        "act/music/enemy/9899e161e9e2a70f_46_76_54_86.png",
        "act/music/enemy/8043678f6bd13fe0_46_46_54_56.png",
        "act/music/enemy/9695666665c1c6ab_46_76_54_86.png",
        "act/music/enemy/c6c6d6da98c8ccb4_46_46_54_54.png",
        "act/music/enemy/c60e6c59324e4fec_46_46_54_56.png",
        "act/music/enemy/c14543cb1f91eeb8_46_46_54_56.png",
        "act/music/enemy/cacd6c383481f9b3_46_76_54_86.png",
        "act/music/enemy/cbae2c79030e3b33_46_46_54_56.png",
        "act/music/enemy/dc90d283f2d92579_46_46_54_56.png",
        "act/music/enemy/e0e1f9790f8741d1_46_46_54_56.png",
        "act/music/enemy/e4bd0ef8f981043e_46_46_54_56.png",
        "act/music/enemy/e4fd0d42f8dac18c_46_46_54_56.png",
        "act/music/enemy/eaeaae8ea2e05417_46_66_54_76.png",
        "act/music/enemy/f874fa74aef88401_46_46_54_56.png",

    ]

    _boss = [
        "act/music/boss/8c8c4ea7a359a976_46_46_54_54.png",
        "act/music/boss/c1d19f4b3c643666_46_46_54_54.png",
        "act/music/boss/c1e0f0964eb3b366_46_46_54_54.png",
        "act/music/boss/d76e0c807ecf034e_46_46_54_54.png",

    ]

    def setTeamPositionToSave(self):
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerRightUp()

            time.sleep(5)
            self.leftClickPer(25, 60)
            time.sleep(15)

        return self.isInMap()
