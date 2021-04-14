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
        dm_ret = dm.FindColor(470, 334, 780, 583,"d4ad6b-000000|c1996b-000000", 0.9, 5, 0, 0)
        print(dm_ret)
        dm.MoveTo(dm_ret[1], dm_ret[2])
        time.sleep(3)

