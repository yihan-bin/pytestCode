import pandas as pd
import win32clipboard
import pyperclip
# data=pyperclip.copy()
# print(data)

win32clipboard.OpenClipboard()
date=win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(date)
