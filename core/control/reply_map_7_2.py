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
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(35, 35)
        self.resetCusor()

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(70, 68)
        self.resetCusor()

    def isAtHome(self):
        return screen.autoCompareResImgHash(self.handle, "map7/on_map_0_0_30_20.png", 0.4)

    def isAtInMapReady(self):
        return screen.autoCompareResImgHash(self.handle, "map7/ready_20_30_80_50.png")

    _mapPoints = [
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

   
    def getEnemyLocation(self):

        imgs = self._enemys
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.8)
            if len(xylist) > 0:
                return xylist

        return []


    def setTeamPositionToSave(self): 
        if self.isInMap():
            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.8):
                winHash = screen.winScreenHash(self.handle)
                self.dragPerRightUp()

            time.sleep(5)
            self.leftClickPer(30, 60)
            time.sleep(15)

        return  self.isInMap() 
        

    def clickPoint(self):
        imgs = self._mapPoints
       
        for i in range(len(imgs)):
            xylist = screen.matchResImgInWindow(
                self.handle, imgs[i], 0.8)
            if len(xylist) > 0:
                x, y = xylist[0]
                self.leftClick(x, y)
                time.sleep(10)
                if self.onGetItems():#防止点错
                    self.battleContinue()
                    time.sleep(4)    
        

   
