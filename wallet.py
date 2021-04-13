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
x, y = 0, 0
dm_ret = dm.FindPic(0,0,2000,2000,"E:\golang\gocode\src\mcjDemo\wallet.bmp","000000",0.9,0, x, y)
print('dm_ret', dm_ret[1], dm_ret[2])
if dm_ret != -1:
    dm.MoveTo(dm_ret[1], dm_ret[2])
    time.sleep(1)
    dm.LeftClick()
    time.sleep(1)
else:
    print("does not found ", x, y)

# 按钱包创建按钮
dm.KeyPress(9)
time.sleep(1)
dm.KeyPress(13)
time.sleep(3)

# 按钱包选择下拉
dm.KeyPress(9)
time.sleep(1)
dm.KeyPress(13)
time.sleep(1)

# 选择hsm-hd钱包
dm_ret = dm.FindPic(0,0,2000,2000,"E:\golang\gocode\src\mcjDemo\hsm.bmp","000000",0.9,0, x, y)
print('dm_ret', dm_ret[1], dm_ret[2])
if dm_ret != -1:
    dm.MoveTo(dm_ret[1], dm_ret[2])
    time.sleep(1)
    dm.LeftClick()
    time.sleep(1)
else:
    print("does not found ", x, y)

# 输入钱包名称
dm.KeyPress(9)
time.sleep(1)
dm.KeyPressChar('t')
dm.KeyPressChar('e')
dm.KeyPressChar('s')
dm.KeyPressChar('x')
time.sleep(1)

# 按下一步
dm.KeyPress(9)
time.sleep(1)
dm.KeyPress(13)
time.sleep(1)

# 输入密码
dm.KeyPress(9)
time.sleep(1)
dm.KeyPressChar('1')

# 下一步
dm.KeyPress(9)
time.sleep(1)
dm.KeyPress(9)
time.sleep(1)
dm.KeyPress(13)
time.sleep(1)