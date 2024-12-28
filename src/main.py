# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from tkinter import Tk

from content.header import header
from content.content import content
from content.footer import footer, footer_copyright

from settings import TITLE, WIDTH, HEIGHT, PRIMARY

from os import path as ospath
from sys import path as syspath
from sys import platform
syspath.append(__file__)


# ------------ SOFTWARE ------------

root = Tk()

# CENTER WINDOW
x = (root.winfo_screenwidth() - WIDTH) // 2
y = (root.winfo_screenheight() - HEIGHT) // 2

# Settings
root.configure(background=PRIMARY)
if platform == "win32":
    root.iconbitmap(ospath.abspath("favicons.ico"))

root.title(TITLE)
root.geometry(f"{ WIDTH }x{ HEIGHT }+{ x }+{ y }")
root.resizable(False, False)  # fixed: WIDTH, HEIGHT

# Content : HEADER
func_header = header(root)
frame_header = func_header[0]
header_height = func_header[1]

# Content : CONTENT
content(root, frame_header)

# Content : FOOTER
func_footer = footer(root)
frame_footer = func_footer[0]
footer_height = func_footer[1]
footer_copyright(frame_footer, footer_height)

# Run
root.mainloop()

# ----------------------------------
