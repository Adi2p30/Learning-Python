import random
import datetime
from webbrowser import *
import openpyxl
import xlrd
functions = ["inputa","para","predict"]
mode = "normal"
while chat != "quit":
    chat = input()
    if chat in functions :
        eval(chat + "()")

