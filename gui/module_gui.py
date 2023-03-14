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
@file: module_gui.py
@date: 2023/1/6 13:23
"""

""" 输入参数获取 """

def main(window):
    def choiceFile1():
        # 第一个文件选择
        # print("choice")
        seleFilePath1 = filedialog.askopenfilename()
        selectFile1.set(seleFilePath1)


    def choiceFile2():
        # 第二个文件选择
        # print("choice")
        seleFilePath2 = filedialog.askopenfilename()
        selectFile2.set(seleFilePath2)

    def choiceFile3():
        # 第二个文件选择
        # print("choice")
        seleEXERoute = filedialog.askopenfilename()
        selectRoute.set(seleEXERoute)
        # 将其安装路径保存在txt中
        __console = sys.stdout
        sys.stdout = open('route.txt', mode='w', encoding='utf-8')
        ClustalRoute = InputBox3.get()
        print(ClustalRoute)
        print("此文件存储Clustal_W安装路径，请勿删除")
        sys.stdout = __console

    """ 运行对应的py文件 """


    def run():
        # 运行
        # 修改管道，将参数写入txt
        __console = sys.stdout
        sys.stdout = open('enter.txt', mode='w', encoding='utf-8')
        input1 = InputBox1.get()
        input2 = InputBox2.get()
        print(input1, input2, end=" ")
        if num == 1 or num == 4 or num == 3:
            pass
        else:
            input3 = InputBox3.get()
            print(input3, end=" ")
            if num == 2 or num == 8:
                # print(num)
                input4 = InputBox4.get()
                input5 = InputBox5.get()
                if num == 2:
                    print(",", input4, ",", input5)
                else:
                    print(input4 + ":" + input5)
        sys.stdout = __console
        """ 按照num的值import对应的py文件 """
        sys.path.append("..\script")
        if num == 1:
            import fasta2csv
            fasta2csv.main()
        elif num == 2:
            import csv2fasta
            csv2fasta.main()
        elif num == 3:
            import Bio_clustalw2
            Bio_clustalw2.main()
        elif num == 4:
            import aln2enc
            aln2enc.main()
        elif num == 5:
            import modl
            modl.main()
        elif num == 6:
            import train
            train.main()
        elif num == 7:
            import predict
            predict.main()
        else:
            import explain
            explain.main()


    # 这里添加第二个页面的代码
    """ 确定选中的模块是什么 """
    # 获取选中的模块的num
    # num = int(input())

    file = open("choice.txt", encoding="utf-8")
    num = int(file.read())
    # 关闭文件，避免后续报错
    file.close()
    os.remove("choice.txt")

    # num = 1
    # print(num)

    # 先确定选中的模块
    module_ = ['fasta2csv', 'csv2fasta', 'Clustal_W2', 'aln2enc', 'modlamp', 'Train', 'Predict', 'X-model']
    modulename = module_[num - 1]
    # print(type(modulename))
    # print(num)
    """*******************************************************************************************************"""
    # 输入框内容
    if num == 1:
        Input_ = ['input_filename', 'output_filename']
        # print(Input_[0])

    elif num == 2:
        Input_ = ['input_filename', 'output_filename', 'sequence_column', 'begin_index', 'end_index']

    elif num == 3:
        Input_ = ['Name', 'FileName', 'Clustal_W2路径']

    elif num == 4:
        Input_ = ['aln_file', 'encode_csv']

    elif num == 5:
        Input_ = ['csv_file', 'column', 'mode']

    elif num == 6:
        Input_ = ['input_trainfile', 'parameter_file', 'model_name']

    elif num == 7:
        Input_ = ['input_model_file', 'input_predict_file', 'output_predict_result']

    else:
        Input_ = ['model_name', 'train_set_csv', 'interpreter', 'mode', 'parameter_list']

    """**************************************************************************"""
    # 创建窗口
    win2 = tk.Toplevel()
    # 初始化Entry控件的textvariable属性值
    selectFile1 = tk.StringVar()
    selectFile2 = tk.StringVar()
    selectRoute = tk.StringVar()
    '''**************************************************************************************************'''
    # 使页面清晰
    # 告诉操作系统使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # 获取屏幕的缩放因子
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # 设置程序缩放
    win2.tk.call('tk', 'scaling', ScaleFactor / 75)

    # 变量.title
    win2.title(modulename)

    # 设置窗口大小
    win2.geometry('800x240')
    # 防止用户调整尺寸
    # win.resizable(0, 0)

    # IntVar() 用于处理整数类型的变量
    v = tk.IntVar()

    '''
        下面开始写组件
        1-5只有一个输入文件
        6-8两个输入文件
    '''
    """ 输入框，一共要设计三种 """
    # 默认一个个输入框后面有选择文件的按钮
    # 2，3，5
    InputHead1 = tk.Label(win2, text=Input_[0]).grid(row=0, column=0)
    InputBox1 = tk.Entry(win2, textvariable=selectFile1)
    InputBox1.grid(row=0, column=1, columnspan=3)
    ''' 文件选择1 '''
    ChoiceFile = tk.Button(win2, text="Choice File", command=choiceFile1)
    ChoiceFile.grid(row=0, column=6)

    InputHead2 = tk.Label(win2, text=Input_[1]).grid(row=1, column=0)
    InputBox2 = tk.Entry(win2, textvariable=selectFile2)
    InputBox2.grid(row=1, column=1, columnspan=3)
    # 4,6-8的第二个输入框后面也有选择文件
    if num > 5 or num == 4:
        ChoiceFile = tk.Button(win2, text="Choice File", command=choiceFile2)
        ChoiceFile.grid(row=1, column=6)

    # 后续参数输入框
    if num == 1 or num == 4:
        # print(num)
        row_ = 1
        pass
    else:
        InputHead3 = tk.Label(win2, text=Input_[2]).grid(row=2, column=0)
        InputBox3 = tk.Entry(win2, textvariable=selectRoute)
        InputBox3.grid(row=2, column=1, columnspan=3)
        row_ = 2
        if num == 3:
            ChoiceFile = tk.Button(win2, text="Choice route", command=choiceFile3)
            ChoiceFile.grid(row=2, column=6)
            ClustalRoute = tk.Label(win2, text="首次使用请输入Clustal_W的安装路径").grid(row=3, column=1)
            row_ = 3
        if num == 2 or num == 8:
            # print(num)
            InputHead4 = tk.Label(win2, text=Input_[3]).grid(row=3, column=0)
            InputBox4 = tk.Entry(win2)
            InputBox4.grid(row=3, column=1, columnspan=3)
            InputHead5 = tk.Label(win2, text=Input_[4]).grid(row=4, column=0)
            InputBox5 = tk.Entry(win2)
            InputBox5.grid(row=4, column=1, columnspan=3)
            row_ = 4

    # 运行button
    choice_button = tk.Button(win2, text='Run', command=run, font=('Arial', 15))
    # choice_button = tk.Button(win2, text='Run', font=('Arial', 15))
    choice_button.grid(row=row_ + 1, column=0)

    # 返回主页面
    # choice_button = tk.Button(win2, text='Close', command=goback, font=('Arial', 15))
    # choice_button = tk.Button(win2, text='Close', command=win2.destroy ,font=('Arial', 15))
    # choice_button.grid(row=row_ + 1, column=1)

    win2.lift()
    win2.attributes('-topmost', True)
    win2.after_idle(win2.attributes, '-topmost', False)
    # 变量.mainloop就是使页面保持显示
    win2.mainloop()
