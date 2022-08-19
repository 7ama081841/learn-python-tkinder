from tkinter import *
from turtle import backward # ta3mali imporation mn tkinter

app = Tk() # na3mel var n7ot feha el class Tk

app2 = Tk() # nejem na3mel multy windows 3ala 9adech mn var eli bech n7ot feha Tk()

app.geometry("500x500+300+200") # t5alini na3ti el height wel width lel windows. el geometry("widthxheight+left+top")

# app.resizable(True,False) # t5alini nemna3 el user bech yet7akem bel width wel height resizable(Width , Feight") te5dem bolean lezem tkoun first letter capital

app.title("mohamed chaabani") # t5alini nbaled el title mta3 el app

app.config(background='gray') # ken n7eb nbadel el background mta3 el app yelzem n7otha fel config()

# app.iconbitmap("C:\\Users\\Admin\\Desktop\\helmet_icon_227551.ico") # t5alini n7ot icon lel app

app.minsize(300 , 300) # t5alini na3ti min width w min height lel app

app.maxsize(700 , 700) # t5alini na3ti max width w max height lel app

app.lift() # t5alili el widows pransipal

app2.iconify() # t5ali el windows tet7al ama metothhorch



app.mainloop() # w ba3d n5adem el app bel mainloop() 