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
        self.leftClickPer(70, 51)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):
        return screen.autoCompareResImgHash(self.handle, "diehai/map_0_0_30_20.png", 0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.handle, "diehai/ready_20_30_80_80.png")

    _ht6Enemys = [
        "diehai/enemy/9abb636ada8a8515_47_47_54_54.png",
        "diehai/enemy/9abb73684a8a9715_47_47_54_54.png",
        "diehai/enemy/9b80e2eca4b199fa_47_50_55_55.png",
        "diehai/enemy/9fb9795a9283a928_47_47_54_54.png",
        "diehai/enemy/96bb795ad2e1282a_47_47_54_54.png",
        "diehai/enemy/9796cc6c6d6dc301_47_47_55_55.png",
        "diehai/enemy/a47ae19936cd38c6_47_47_54_54.png",
        "diehai/enemy/a053b6cd4bca692b_47_47_54_54.png",
        "diehai/enemy/a74694287fb26d31_47_47_54_54.png",
        "diehai/enemy/b5e441ca4a1b8efa_47_47_54_54.png",
        "diehai/enemy/b278966ea152ad66_47_47_54_54.png",
        "diehai/enemy/c9c9607074f7e386_47_47_54_54.png",
        "diehai/enemy/c236e39e2d2ec82b_47_47_54_54.png",
        "diehai/enemy/c86389f247ffc441_47_47_54_54.png",
        "diehai/enemy/c1990999377625dd_47_50_55_55.png",
        "diehai/enemy/cbc16164369a9b9d_47_47_55_55.png",
        "diehai/enemy/cbcbc9617030f173_47_47_54_54.png",
        "diehai/enemy/cc8d9cb11d988dcd_47_50_55_55.png",
        "diehai/enemy/cdcdc070707273f1_47_47_55_55.png",
        "diehai/enemy/d9f0748ece646626_47_47_54_54.png",
        "diehai/enemy/d999986336319b99_47_50_55_55.png",
        "diehai/enemy/e2c2bcf0f1383993_47_50_55_55.png",
        "diehai/enemy/e805d77aa8015fba_47_50_55_55.png",
        "diehai/enemy/e857ba055fe0750a_47_50_55_55.png",
        "diehai/enemy/e897baa15ea0552e_47_50_55_55.png",
        "diehai/enemy/ea17a813d6e43ce1_47_47_54_54.png",
        "diehai/enemy/f58b5a323a2a3339_47_47_54_54.png",
        "diehai/enemy/fd26991a069e2d1b_47_47_54_54.png",
    ]

    _boss = [
        "diehai/boss/8ba97464b38bae4c_48_48_53_53.png",
        "diehai/boss/a368a268b35dae6a_47_47_54_54.png",
        "diehai/boss/a368a268b759ad6a_47_47_54_54.png",
        "diehai/boss/b04fb06bb25c947c_48_48_54_54.png",

    ]

    def getEnemyLocation(self):

        imgs = self._ht6Enemys+self._enemys

        # random.shuffle(imgs)
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.7)
            if len(xylist) > 0:
                return xylist

        return []

   