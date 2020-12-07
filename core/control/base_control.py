import win32api
import win32gui
import win32con
import common.screen as screen
import threading
import time


class BaseControl:

    handle = 0
    interval = 5
    _team1BattleCount = 0
    _team2BattleCount = 0
    _team1MoveCount = 0
    _team2MoveCount = 0
    _teamNum = 1
    _isRun = False

    _pause = False

    def __init__(self):
        pass


    def pause(self):
        self._pause=True
    # def recovery(self):
    #     self._pause=False


    def stop(self):
        self._isRun = False

    def start(self):
        self._pause=False
        if self._isRun:
            return
        self._isRun = True
        t = threading.Thread(target=self.run)
        t.start()

    def getPosX(self, srcPer):
        srcPer = srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        width = wRight-wLeft
        return int(wLeft+(width*srcPer))

    def getPosY(self, srcPer):
        srcPer = srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        height = wBottom-wTop
        return int(wTop+(height*(srcPer)))

    def onGetItems(self):
        onGetItems = self.autoCompareResImgHash(
            "on_get_item_40_20_60_40.png") or self.matchResImgInWindow("on_get_item2_40_30_60_35.png")
        print("onGetItems", onGetItems)
        return onGetItems

    def dragPer(self, x, y, toX, toY):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.3)

        moveToX = int(self.getPosX(toX)*(65535/win32api.GetSystemMetrics(0)))
        moveToY = int(self.getPosY(toY)*(65535/win32api.GetSystemMetrics(1)))
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE +
                             win32con.MOUSEEVENTF_MOVE, moveToX, moveToY, 0, 0)

        time.sleep(0.6)
        win32api.SetCursorPos((moveToX, moveToY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.resetCusor()

    def drag(self, x, y, toX, toY):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.3)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        moveToX = int(toX*(65535/sw))
        moveToY = int(toY*(65535/sh))
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE +
                             win32con.MOUSEEVENTF_MOVE, moveToX, moveToY, 0, 0)
        time.sleep(0.6)
        win32api.SetCursorPos((moveToX, moveToY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def leftClick(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.resetCusor()

    def leftClickPer(self, x, y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        self.resetCusor()

    def clickNeedLeaderCat(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(95), self.getPosY(35)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.resetCusor()

    def clickOnGetItems(self):
        screen.setForegroundWindow(self.handle)
        self.leftClick(self.getPosX(50), self.getPosY(65))

    def battleContinue(self):
        screen.setForegroundWindow(self.handle)
        self.leftClick(self.getPosX(85), self.getPosY(90))
        self.resetCusor()

    def closeNewMission(self):
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(99, 99)
        self.resetCusor()

    def switchTeam(self):
        print("switchTeam")
        screen.setForegroundWindow(self.handle)
        # self.leftClickPer(99, 99)#防止任务弹出
        time.sleep(0.5)
        self.leftClickPer(82, 96)
        time.sleep(3)
        self.resetCusor()

    def resetTeamLocation(self, t=3):
        print("resetTeamLocation")
        screen.setForegroundWindow(self.handle)
        # self.leftClickPer(99, 99)#防止任务弹出
        # time.sleep(0.5)
        self.leftClickPer(82, 96)
        time.sleep(t)
        self.leftClickPer(82, 96)
        # time.sleep(t)
        self.resetCusor()

    def moveLeft(self, num=1):
        print("moveLeft")
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(50-num*10, 50)
        self.leftClickPer(50-num*10, 50)
        time.sleep(num)
        self.resetCusor()

    def moveLeftDrag(self, num=1):
        x = self.getPosX(50-num*10)
        y = self.getPosY(50)
        cx = self.getPosX(50)
        cy = self.getPosY(50)
        self.drag(x, y, cx, cy)
        self.drag(x, y, cx, cy)
        time.sleep(2)
        self.leftClickPer(50, 50)
        time.sleep(num)
        self.resetCusor()

    def moveRight(self, num=1):
        print("moveRight")
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(50+num*10, 50)
        self.leftClickPer(50+num*10, 50)
        time.sleep(num)
        self.resetCusor()

    def moveRightDrag(self, num=1):
        x = self.getPosX(50+num*10)
        y = self.getPosY(50)
        cx = self.getPosX(50)
        cy = self.getPosY(50)
        self.drag(x, y, cx, cy)
        self.drag(x, y, cx, cy)
        time.sleep(2)
        self.leftClickPer(50, 50)
        time.sleep(num)
        self.resetCusor()

    def moveUp(self, num=1):
        print("moveUp")
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(50, 50-num*13)
        self.leftClickPer(50, 50-num*13)
        time.sleep(num)
        self.resetCusor()

    def moveUpDrag(self, num=1):
        x = self.getPosX(50)
        y = self.getPosY(50-num*13)
        cx = self.getPosX(50)
        cy = self.getPosY(50)
        self.drag(x, y, cx, cy)
        self.drag(x, y, cx, cy)
        time.sleep(2)
        self.leftClickPer(50, 50)
        time.sleep(num)
        self.resetCusor()

    def moveDown(self, num=1):
        print("moveDown")
        screen.setForegroundWindow(self.handle)
        self.leftClickPer(50, 50+num*15)
        self.leftClickPer(50, 50+num*15)
        time.sleep(num)
        self.resetCusor()

    def moveDownDrag(self, num=1):
        x = self.getPosX(50)
        y = self.getPosY(50+num*15)
        cx = self.getPosX(50)
        cy = self.getPosY(50)
        self.drag(x, y, cx, cy)
        self.drag(x, y, cx, cy)
        time.sleep(2)
        self.leftClickPer(50, 50)
        time.sleep(num)
        self.resetCusor()

    def resetCusor(self):
        time.sleep(0.5)
        win32api.SetCursorPos((0, 0))

    def onBattleEnd(self):
        return self.autoCompareResImgHash("on_battle_end_10_10_90_30.png") \
            or self.autoCompareResImgHash("battle_end1_30_80_50_95.png")
        # return self.matchResImgInWindow("on_battle_end_10_10_90_30.png") \
        #     or self.matchResImgInWindow( "battle_end1_30_80_50_95.png")

    def onBattleEndCount(self):
        onBattleEndCount = self.matchResImgInWindow("battle_end_68_86_92_96.png",0.7)\
            or self.matchResImgInWindow("battle_end2_78_90_90_96.png",0.7)
        print("onBattleEndCount", onBattleEndCount)
        return onBattleEndCount

    def isInMap(self):
        return self.autoCompareResImgHash("in_map_65_90_100_100.png")

    def onGetSR(self):

        onGetSR = screen.autoCompareResImgHashValue(
            self.handle, "on_get_sr_70_20_95_60.png") > 0.2
        print("onGetSR", onGetSR)
        return onGetSR

    def onGetSSR(self):
        onGetSSR = screen.autoCompareResImgHashValue(
            self.handle, "on_get_ssr_70_10_90_50.png") > 0.2
        print("onGetSSR", onGetSSR)
        return onGetSSR

    def clickOnGetSR(self):
        self.leftClickPer(98, 98)

    def clickToFire(self):
        xylist = screen.matchResImgInWindow(
            self.handle, "to_fire_80_85_95_95.png", 0.8)
        if len(xylist) > 0:
            x, y = xylist[0]
            self.leftClick(x, y)

    def isNewMission(self):  # TODO 待优化

        isNewMission = self.matchResImgInWindow("new_mission_28_26_70_76.png", 0.5) \
            or self.matchResImgInWindow("newtask_28_26_70_30.png") \
            or self.matchResImgInWindow("newtask_30_68_66_76.png")

        print("isNewMission", isNewMission)
        return isNewMission

    def onSelectTeam(self):
        onSelectTeam = self.autoCompareResImgHash(
            "on_select_team_78_80_92_88.png")
        print("onSelectTeam", onSelectTeam)
        return onSelectTeam

    def onSelectTeamByMatch(self):  # 这种方式在地图会有问题
        print("onSelectTeamByMatch")
        return self.matchResImgInWindow("on_select_team_78_80_92_88.png")

    def intoMap(self):
        screen.setForegroundWindow(self.handle)
        self.leftClick(self.getPosX(80), self.getPosY(85))

    def atTeamIntoMap(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(80), self.getPosY(85)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.resetCusor()

    def matchResImgInWindow(self, imgName, threshold=0.8):
        xylist = screen.matchResImgInWindow(self.handle, imgName, threshold)
        if len(xylist) > 0:
            return True
        else:
            return False

    def autoCompareResImgHash(self, img,alikeValue=0.35):
        return screen.autoCompareResImgHash(self.handle, img,alikeValue)


    def clickMacthImg(self,imgPath,threshold=0.9):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle,imgPath,threshold)
        if len(xylist) > 0:
            x, y = xylist[0]
            self.leftClick(x, y)
            time.sleep(2)
            return True
        return False   
    # def isHpEmpty(self):
    #     return self.autoCompareResImgHash("hp_empty_10_40_90_62.png")

    _currentWinHash = ""

    def isSameWin(self):

        nowHash = screen.winScreenHash(self.handle)
        res = screen.alikeHash(self._currentWinHash,
                               nowHash, 0.6)
        self._currentWinHash = nowHash
        print("isSameWin",self._currentWinHash,nowHash)
        return res

    def commonAction(self):

        isBattleEnd = False
        # if self.onGetSR() or self.onGetSSR():
        #     time.sleep(2)
        #     self.clickOnGetSR()
        #     time.sleep(4)

        if self.onBattleEnd():
            time.sleep(2)
            self.battleContinue()
            time.sleep(4)
            # isBattleEnd = True
        if self.onGetItems():
            time.sleep(2)
            self.battleContinue()
            time.sleep(4)
            # isBattleEnd = True

        if self.onGetSR() or self.onGetSSR():
            time.sleep(2)
            self.clickOnGetSR()
            time.sleep(4)
            # isBattleEnd = True

        if self.clickMacthImg("battle_end2_78_90_90_96.png"):
            isBattleEnd = True 
            time.sleep(8)
        # if self.onBattleEndCount():
        #     time.sleep(2)
        #     self.battleContinue()
        #     time.sleep(8)
        #     isBattleEnd = True
        print("isBattleEnd", isBattleEnd)
        if isBattleEnd:
         
            if self._teamNum == 1:
                self._team1BattleCount = self._team1BattleCount+1
            else:
                self._team2BattleCount = self._team2BattleCount+1

            print("BattleCount", self._team1BattleCount, self._team2BattleCount)    

        if self.isNewMission():
            self.leftClickPer(99, 99)
            time.sleep(3)

        self.clickToFire()

    def run(self):
        pass


pass
