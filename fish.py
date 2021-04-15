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
        time.sleep(5)

        rect = dm.GetWindowRect(hwnd, 0, 0, 0, 0)
        flag = False
        for xPos in range(dm_ret[1], dm_ret[3], 10):
            if flag:
                break
            for yPos in range(dm_ret[2], dm_ret[4], 10):
                dm.MoveTo(xPos, yPos)
                shape = dm.GetCursorShape()
                if shape == 1053591638:
                    flag = True
                    break

        if flag:
            while True:
                time.sleep(0.1)
                shape = dm.GetCursorShape()
                if shape == 965986689:
                    dm.RightClick()
                    print('应该上鱼了, 等待1秒自动拾取')
                    time.sleep(1)
        else:
            print('没找到浮漂, 开始下一轮')
