#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Mar 26, 2020 03:48:00 PM PDT  platform: Windows NT
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global toDisplay
    toDisplay = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def numPressed(num):
    index = w.GetEntryCursorIndex()
    w.InsertToEntryAtCursorIndex(index, num)

def clearDisplay():
    toDisplay.set(0)

def equalPressed():
    try:
        toDisplay.set(str(eval(toDisplay.get().replace("^","**"))))
    except:
        toDisplay.set("error")

def validateInput(text, actionType):
    if actionType == '1': #insert
        if text.isdigit() or text in ["+","-","*","/","^","%","()"]:
            return True
    return True

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




