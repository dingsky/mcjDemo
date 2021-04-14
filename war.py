# 战场挂机脚本

import time
import win32com.client

if __name__=="__main__":
    # 创建大漠对象
    dm = win32com.client.Dispatch('dm.dmsoft')

    # 设置全局目录
    dm.SetPath('F:\Golang\gocode\src\mcjDemo')

    # 查找名为魔兽世界的窗口
    hwnd = dm.FindWindow('', "魔兽世界")
    print('hwnd:', hwnd)

    # 选中窗口
    x1 = y1 = x2 = y2 =0
    dm_ret = dm.GetWindowRect(hwnd, x1, y1, x2, y2)
    dm.MoveTo(dm_ret[1], dm_ret[2])
    dm.LeftClick()

    # 每五秒跳一次
    while True:
        dm.KeyPress(32)
        time.sleep(1)

        # 按9弹出战场界面
        dm.KeyPressChar('9')
        time.sleep(1)

        # 点击激情战场
        x = y = 0
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\war.bmp|pic\war1.bmp", "000000", 0.9, 0,  x, y)
        print('dm_ret', dm_ret[1], dm_ret[2])
        if dm_ret[1] != -1 and dm_ret[2] != -1:
            dm.MoveTo(dm_ret[1], dm_ret[2])
            time.sleep(1)
            dm.LeftClick()
            time.sleep(1)
        else:
            print("does not found war")
            exit(1)

        # 点击战场入口
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\lxwar.bmp|pic\zgwar.bmp", "000000", 0.9, 0,  x, y)
        print('dm_ret', dm_ret)
        if dm_ret[1] != -1 and dm_ret[2] != -1:
            dm.MoveTo(dm_ret[1], dm_ret[2])
            time.sleep(1)
            dm.LeftClick()
            time.sleep(1)
        else:
            print("does not found war into")

        # 点击战场入口
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\ok.bmp", "000000", 0.9, 0,  x, y)
        print('dm_ret', dm_ret)
        if dm_ret[1] != -1 and dm_ret[2] != -1:
            dm.MoveTo(dm_ret[1], dm_ret[2])
            time.sleep(1)
            dm.LeftClick()
            time.sleep(1)
        else:
            print("does not found war into")

        # 点击进入战场
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\goinwar.bmp", "000000", 0.9, 0,  x, y)
        print('dm_ret', dm_ret)
        if dm_ret[1] != -1 and dm_ret[2] != -1:
            dm.MoveTo(dm_ret[1], dm_ret[2])
            time.sleep(1)
            dm.LeftClick()
            time.sleep(1)
            while True:     # 直到退出战场
                dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\exit.bmp", "000000", 0.9, 0, x, y)
                print('dm_ret', dm_ret)
                if dm_ret[1] != -1 and dm_ret[2] != -1:
                    dm.MoveTo(dm_ret[1], dm_ret[2])
                    time.sleep(1)
                    dm.LeftClick()
                    time.sleep(2)
                    break
                else:
                    dm.KeyPress(32)
                    time.sleep(5)
        else:
            print("does not found goin war")
        time.sleep(5)

