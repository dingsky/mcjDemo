# 钓鱼脚本

from function import myTime
import win32com.client

if __name__ == "__main__":
    # 创建大漠对象
    dm = win32com.client.Dispatch('dm.dmsoft')

    hwnd = dm.FindWindow('', "mcjDemo")
    print('hwnd:', hwnd)
    dm_ret = dm.GetWindowRect(hwnd, 0, 0, 0, 0)
    print(dm_ret)

    # 移动鼠标
    print(myTime.getLocalTime())
    for xPos in range(dm_ret[1], dm_ret[3], 10):
        for yPos in range(dm_ret[2], dm_ret[4], 10):
            dm.MoveTo(xPos, yPos)
    print(myTime.getLocalTime())

