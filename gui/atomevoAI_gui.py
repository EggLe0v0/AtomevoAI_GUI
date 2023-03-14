#!/usr/bin/env python
# coding=utf-8

import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
import ctypes
import os

"""
@author: Le
@file: atomevoAI_gui.py
@date: 2023/1/4 15:33
"""


def change():
    # 获取选择
    choicenum = v.get()
    # print(choicenum)

    # 写入选择
    __console = sys.stdout
    sys.stdout = open('choice.txt', mode='w', encoding='utf-8')
    print(choicenum)
    sys.stdout = __console

    # 页面跳转
    # 引用第二个模块并调用
    import module_gui
    module_gui.main(win)
    """
        因为引用import只能跑一次，所以这个方法不行
        win.destroy()
        import module_gui
        print(1)
        reload()
    """


# self.choice_ = choice_
# tk.TK就是创建窗口，前面的就是给这个窗口当作一个变量，可以通过使用其他语法来对窗口进行修改
win = tk.Tk()

# 这段已经被废弃了，忘记删了，对程序运行没有影响
selectFile1 = tk.StringVar()
selectFile2 = tk.StringVar()
selectRoute = tk.StringVar()

# 使页面清晰
# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 获取屏幕的缩放因子
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 设置程序缩放
win.tk.call('tk', 'scaling', ScaleFactor / 75)

# 变量.title
win.title("AtomevoAI")

# 设置窗口大小
win.geometry('800x200')
# 防止用户调整尺寸
win.resizable(0, 0)

# 多个button选择使用的模块
site = [('fasta2csv', 1),
        ('csv2fasta', 2),
        ('Clustal_W2', 3),
        ('aln2enc', 4),
        ('modlamp', 5),
        ('Train', 6),
        ('Predict', 7),
        ('X-model', 8)]

# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
for ModuleName, num in site:
    module_button = tk.Radiobutton(win, text=ModuleName, value=num, variable=v, font=('Arial', 15))
    if num <= 4:
        module_button.grid(row=0, column=num)
        if num > 2:
            module_button.grid(row=0, column=num + 1)
    elif num > 4:
        module_button.grid(row=1, column=num - 4)
        if num - 4 > 2:
            module_button.grid(row=1, column=num - 3)

# button确定选择的模块，进入新的页面
choice_button = tk.Button(win, text='Choice', command=change, font=('Arial', 15))
choice_button.grid(row=3, column=3)

# 变量.mainloop就是使页面保持显示
win.mainloop()
