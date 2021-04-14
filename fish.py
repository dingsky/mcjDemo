# 钓鱼脚本

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

        # 按8触发钓鱼
        dm.KeyPressChar('8')
        time.sleep(1)

        # 捕捉浮漂
        x = y = 0
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "pic\mark.bmp", "000000", 0.9, 0,  x, y)
        print('dm_ret', dm_ret[1], dm_ret[2])
        if dm_ret[1] != -1 and dm_ret[2] != -1:
            dm.MoveTo(dm_ret[1], dm_ret[2])
            time.sleep(1)
        else:
            print("does not found war")
            continue

        # 等待上鱼
        while True:
            shape = dm.GetCursorShape()
            if shape == 1053591638:
                dm.RightClick()
                time.sleep(1)
                break

