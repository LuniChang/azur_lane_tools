import win32api
import win32gui
import win32con
import time
import tkinter as tk


from control.reply_hongran_d3 import ReplyHongranD3

from control.reply_spc_essex import ReplySpcEssexD3

from control.reply_map_8_1 import ReplyMap81
from control.reply_map_7_2 import ReplyMap72

from control.reply_map_activity_music_sp5 import ReplyMapActivity

import common.screen as screen




# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名


handle = screen.getWinHandle()
main = tk.Tk()

replyHongRanD3 = ReplyHongranD3(handle, 2)
replySpcEssex = ReplySpcEssexD3(handle, 5)
replyMap81= ReplyMap81(handle, 2)
replyMapActivity= ReplyMapActivity(handle, 2)

def resetHandle():
    handle = screen.getWinHandle()
    replyHongRanD3.handle = handle
    replySpcEssex.handle = handle
    replyMap81.handle = handle

main.title("碧蓝航线工具")
main.geometry("480x780")

fm1 = tk.Frame(main)
fm1.pack()


tk.Label(fm1, text="模拟器分辨率1024*576").grid(row=0, column=2, columnspan=3)


tk.Button(fm1, text="重设窗口句柄", width=10, height=1,
          command=resetHandle).grid(row=1, column=1)


tk.Button(fm1, text="开始红染D3", width=10, height=1,
          command=replyHongRanD3.start).grid(row=2, column=1)
tk.Button(fm1, text="结束红染", width=10, height=1,
          command=replyHongRanD3.stop).grid(row=2, column=2)


tk.Label(fm1,text="0自动1234EX按顺序").grid(row=3,column=0)
assignLevel=tk.IntVar()
assignLevel.set(0)
def startSpcEssex():
    replySpcEssex.assignLevel=int(assignLevel.get())
    replySpcEssex.start()
    
tk.Entry(fm1,textvariable=assignLevel,width=10).grid(row=3,column=1)

tk.Button(fm1, text="开始特别演戏-埃塞克斯", width=20, height=1,
          command=startSpcEssex).grid(row=3, column=2)
tk.Button(fm1, text="结束特别演戏-埃塞克斯", width=20, height=1,
          command=replySpcEssex.stop).grid(row=3, column=3)


tk.Button(fm1, text="开始8-1", width=20, height=1,
          command=replyMap81.start).grid(row=4, column=1)
tk.Button(fm1, text="结束8-1", width=20, height=1,
          command=replyMap81.stop).grid(row=4, column=2)



def initAct():
    team1BattleMaxCount=tk.IntVar()
    team1BattleMaxCount.set(5)
    team2BattleMaxCount=tk.IntVar()
    team2BattleMaxCount.set(1)


   
    tk.Label(fm1,text="1队打小怪数").grid(row=5,column=0) 
    tk.Entry(fm1,textvariable=team1BattleMaxCount,width=10).grid(row=5,column=1)
    tk.Label(fm1,text="2队打小怪数").grid(row=6,column=0) 
    tk.Entry(fm1,textvariable=team2BattleMaxCount,width=10).grid(row=6,column=1)
    def startAct():
        replyMapActivity.team1BattleMaxCount=int(team1BattleMaxCount.get())
        replyMapActivity.team2BattleMaxCount=int(team2BattleMaxCount.get())
        replyMapActivity.start()


    model = tk.IntVar()
    model.set(0)
    def toChangeModel():
        replyMapActivity.setFindEnemysMode(model.get())  


    tk.Checkbutton(fm1,text="拖拽敌人模式",variable=model,onvalue=1,offvalue=0,command=toChangeModel).grid(row=7,column=0)
    
    tk.Button(fm1, text="开始活动图SP5", width=20, height=1,
            command=startAct).grid(row=7, column=1)
    tk.Button(fm1, text="结束活动图", width=20, height=1,
            command=replyMapActivity.stop).grid(row=7, column=2)

initAct()          


def iniMap72():
    replyMapActivity= ReplyMap72(handle, 2)
    team1BattleMaxCount=tk.IntVar()
    team1BattleMaxCount.set(5)
    team2BattleMaxCount=tk.IntVar()
    team2BattleMaxCount.set(0)
    tk.Label(fm1,text="1队打小怪数").grid(row=8,column=0) 
    tk.Entry(fm1,textvariable=team1BattleMaxCount,width=10).grid(row=8,column=1)
    tk.Label(fm1,text="2队打小怪数").grid(row=9,column=0) 
    tk.Entry(fm1,textvariable=team2BattleMaxCount,width=10).grid(row=9,column=1)
    def startAct():
        replyMapActivity.team1BattleMaxCount=int(team1BattleMaxCount.get())
        replyMapActivity.team2BattleMaxCount=int(team2BattleMaxCount.get())
        replyMapActivity.start()


    tk.Button(fm1, text="开始7-2", width=20, height=1,
            command=startAct).grid(row=10, column=1)
    tk.Button(fm1, text="结束7-2", width=20, height=1,
            command=replyMapActivity.stop).grid(row=10, column=2)

iniMap72()        




tk.Label(main, text="工具操作").pack()




# fmTools=tk.Frame(main).pack()
tk.Button(main, text="窗口截图",
          width=10, height=1,
          command=lambda: screen.grabCaptureDef(hwnd=handle, needShow=True)).pack()


tk.Label(main, text="左X百分比").pack()
xLeft = tk.Entry(main, textvariable=float)
xLeft.pack()

tk.Label(main, text="左Y百分比").pack()
yLeft = tk.Entry(main)
yLeft.pack()

tk.Label(main, text="右X百分比").pack()
xRight = tk.Entry(main)
xRight.pack()

tk.Label(main, text="右Y百分比").pack()
yRight = tk.Entry(main)
yRight.pack()
btnPerCap = tk.Button(main, text="百分比截图",
                      width=10, height=1,
                      command=lambda: screen.grabCaptureRectPerHash(
                          hwnd=handle, tLeft=xLeft.get(), tTop=yLeft.get(), tRight=xRight.get(), tBottom=yRight.get(), needShow=True))
btnPerCap.pack()

tk.Label(main, text="取图片哈希路径").pack()
textPath = tk.Entry(main)
textPath.pack()
texthash = tk.Entry(main)
texthash.pack()
hashBtn = tk.Button(main, text="取图片哈希", width=10, height=1, command=lambda: texthash.insert(
    index=0, string=screen.getImgHashByPath(path=textPath.get())))
hashBtn.pack()


# 进入消息循环
main.mainloop()


exit(0)
