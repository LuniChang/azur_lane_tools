import win32api,win32gui,win32con
import time
import tkinter as tk


from control.reply_hongran_d3 import ReplyHongranD3

import common.screen as screen



# def MAKELPARAM(x,y):
#     return x+(y<<16)

# class MuMuClick:

# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
handle =screen.getWinHandle()



main = tk.Tk()

replyBattle= ReplyHongranD3(handle,2)

main.title("碧蓝航线工具")
main.geometry("480x780")

fm1=tk.Frame(main)
fm1.pack()




tk.Label(fm1,text="模拟器分辨率1280*720").grid(row=0,column=2,columnspan=3)



tk.Button(fm1,text="开始红染D3",width=10,height=1,command=replyBattle.start).grid(row=1,column=2)
tk.Button(fm1,text="结束红染",width=10,height=1,command=replyBattle.stop).grid(row=1,column=3)




tk.Label(main,text="工具操作").pack()

# fmTools=tk.Frame(main).pack()
tk.Button(main,text="窗口截图",\
width=10,height=1,\
command=lambda:screen.grabCaptureDef(hwnd=handle,needShow=True)).pack()


tk.Label(main,text="左X百分比").pack()
xLeft=tk.Entry(main,textvariable=float)
xLeft.pack()

tk.Label(main,text="左Y百分比").pack()
yLeft=tk.Entry(main)
yLeft.pack()

tk.Label(main,text="右X百分比").pack()
xRight=tk.Entry(main)
xRight.pack()

tk.Label(main,text="右Y百分比").pack()
yRight=tk.Entry(main)
yRight.pack()
btnPerCap=tk.Button(main,text="百分比截图",\
    width=10,height=1,\
    command=lambda:screen.grabCaptureRectPerHash(\
        hwnd=handle,tLeft=xLeft.get(),tTop=yLeft.get(), tRight=xRight.get(), tBottom=yRight.get(),needShow=True))
btnPerCap.pack()

tk.Label(main,text="取图片哈希路径").pack()
textPath=tk.Entry(main)
textPath.pack()
texthash=tk.Entry(main)
texthash.pack()
hashBtn=tk.Button(main,text="取图片哈希",width=10,height=1,command=lambda:texthash.insert(index=0,string=screen.getImgHashByPath(path=textPath.get())) )
hashBtn.pack()





# 进入消息循环
main.mainloop()




# exit()