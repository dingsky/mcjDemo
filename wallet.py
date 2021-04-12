import win32com.client
import time

dm = win32com.client.Dispatch('dm.dmsoft')
# 移动到目标程序的位置
dm.MoveTo(275,9)
time.sleep(1)

# 鼠标双机打开
dm.LeftDoubleClick()
time.sleep(3)

# 单击鼠标选择窗口
dm.LeftClick()
time.sleep(1)

# 按tab选择第一个输入框
dm.KeyPress(9)
time.sleep(1)

# 输入用户名
dm.KeyPress(16)
dm.KeyPressChar('s')
dm.KeyPressChar('u')
dm.KeyPressChar('p')
dm.KeyPressChar('e')
dm.KeyPressChar('r')
time.sleep(1)

# 按tab选择第二个输入框
dm.KeyPress(9)
time.sleep(1)

# 输入密码
dm.KeyPressChar('1')
time.sleep(1)

# 按tab选择确认按钮
dm.KeyPress(9)
time.sleep(1)

# 按回车登录
dm.KeyPress(13)
time.sleep(1)

# 设置全局路径
ret = dm.SetPath("E:\golang\gocode\src\mcjDemo")
if ret != 1:
    print('SetPath error')
    exit

# 获取窗口句柄
dm.KeyPress(9)
hwnd = dm.GetMousePointWindow()
print('hwnd',hwnd)

# 绑定窗口
ret = dm.BindWindow(hwnd, 'normal', 'normal', 'normal', 0)
if ret != 1:
    print('bindWindow error')
    exit

time.sleep(1)

# 查找钱包服务的图标位置
x,y = -1, -1
dm_ret = dm.FindPic(0,0,2000,2000,"wallet.bmp","000000",0.8,0,x,y)
if x >= 0 and y >= 0:
    dm.MoveTo(x,y)
else:
    print("does not found %d %d", x, y)
