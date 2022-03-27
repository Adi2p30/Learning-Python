from googlesearch import *
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pyautogui import *
import PyPDF2
from pathlib import Path
import requests
import urllib.request
from urllib.request import Request, urlopen
pdflst = []
query = "Egypts response to covid 19" \
        " filetype:pdf"
x = 0
import wget
for j in search(query, tld="co.in", num=10, stop=4, pause=2):
    print(j)
    pdflst.append(j)
print(pdflst)
for i in pdflst:
    wget.download(i)

# pdfFileObj = open(str(x) + '.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
# pdfFileObj.close()
# print("____________________________________________________")
# print("____________________________________________________")
# print("____________________________________________________")

# creating a pdf file object
# pdfFileObj = open('example.pdf', 'rb')
# creating a pdf reader object
# printing number of pages in pdf file

# creating a page object
# extracting text from page
# closing the pdf file object


def clickpos():
    research = input("Keywords")
    keyDown("command")
    press("tab")
    keyUp("command")
    sleep(0.5)
    keyDown("command")
    press("t")
    keyUp("command")
    sleep(3)
    while True:
        sleep(0.5)
        write(research+"filetype:pdf")
        press("enter")
def bs():
    ur = 0
    # enemieslst = []
    # for i in range(0,10):
    #     enemieslst.append(input("enemy number " + str(i) + ": "))
    # print(enemieslst)
