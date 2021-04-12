import win32com.client

dm = win32com.client.Dispatch('dm.dmsoft')
dm.KeyPressStr("123,456", 0)
