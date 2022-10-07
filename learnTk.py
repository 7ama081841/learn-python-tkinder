from cProfile import label
from cgitb import text
from textwrap import fill
from tkinter import * # ta3mali imporation mn tkinter

from tkinter import ttk #  ta3mali imporation mta3 combobox

app = Tk() # na3mel var n7ot feha el class Tk

# app2 = Tk() # nejem na3mel multy windows 3ala 9adech mn var eli bech n7ot feha Tk()

app.geometry("1000x500+100+0") # t5alini na3ti el height wel width lel windows. el geometry("widthxheight+left+top")

# app.resizable(True,False) # t5alini nemna3 el user bech yet7akem bel width wel height resizable(Width , Feight") te5dem bolean lezem tkoun first letter capital

app.title("mohamed chaabani") # t5alini nbaled el title mta3 el app

app.config(background='gray') # ken n7eb nbadel el background mta3 el app yelzem n7otha fel config()

app.iconbitmap("C:\\Users\\Admin\\Desktop\\learn Desktop app with python\\learn-python-tkinder\\helmet_icon_227551.ico") # t5alini n7ot icon lel app

# app.minsize(300 , 300) # t5alini na3ti min width w min height lel app

# app.maxsize(700 , 700) # t5alini na3ti max width w max height lel app

# app.lift() # t5alili el widows pransipal

# app2.iconify() # t5ali el windows tet7al ama metothhorch

# app2.lower() # te5dem kima iconify()

# app2.state("withdrawn") # state(" normal , iconic , withdrawn ") 
# iconic => iconify() and lower()
# withdrawn => hide for windows
# moula7tha el state a5af mn lo5rin

fr1 = Frame( width='300' , height="300" , bg="royalblue" ) # el frame kima el div
fr2 = Frame( width='300' , height="300" , bg="dodgerblue2" ) 
fr3 = Frame( width='300' , height="300" , bg="dodgerblue2" ) 

fr1.place(x=0 , y=0) # ta3ti el position fel windows w lezem n7otha 
fr2.place(x=310 , y=0) 
fr3.place(x=650 , y=0) 

# var = tool( paraint  , option )
btn1 = Button(fr1 , text="button 1" , fg="black" , bg="white")
btn1.place(x=0,y=0 )

btn2 = Button(fr2, text="button 2" , bg="white" )
btn2.place(x=0 , y=0 )

# var = Label( paraint  , option )
lbl1 = Label(fr1 , text="mohamed chaabeni" , fg="red" , bg='royalblue',font=1 )
lbl1.place(x=0 , y=40 ) # el place() lezma

input_1 =  Entry(fr1 , justify='center') # el Entry() te5dem input
input_1.place(x=0 , y=65)
if(input_1=="a"):
    print(True)
input_2 = Entry(fr1 , justify='right' )
input_2.place(x=130 , y=65)

# var = ttk.Combobox(paraint , value=("opstion 1" , "opstion 2") state="readonly" ) 
selectBox = ttk.Combobox(fr1 , value=("mohamed" , "safe") , state="readonly" ) # te5dem kima selectBox 
selectBox.place(x=40 , y=90)

# var = Listbox(paraint , width="" , height="")
lst_1 = Listbox(fr1) # te5dem kima selectbox ama to93od list ma7loula

# var.insert(index de line , "text" ) 
lst_1.insert(0 , "mohamed" ) # ta3mali el opstions 
lst_1.insert(1 , "safe" ) 
lst_1.insert(2 , "yassine" ) 
lst_1.insert(3 , "oumayma" ) 
lst_1.insert(4 , "ousama" ) 
lst_1.insert(5 , "rahma" ) 
lst_1.insert(6 , "chayma" ) 

# lst_1.pack() # el pack() kima el place ama random

lst_1.place(x=40 , y=115) 

# var = ttk.Radiobutton(paraint , value=1 , text="1")
r1 = ttk.Radiobutton(fr1 , value=1 , text="1") # te5dem kima input radio
r2 = ttk.Radiobutton(fr1 , value=2 , text="2")
r3 = ttk.Radiobutton(fr1 , value=3 , text="3")
r4 = ttk.Radiobutton(fr1 , value=4 , text="4")
r5 = ttk.Radiobutton(fr1 , value=5 , text="5")

r1.place(x=0 , y=90)
r2.place(x=0 , y=115)
r3.place(x=0 , y=140)
r4.place(x=0 , y=165)
r5.place(x=0 , y=190)

scroll = Scrollbar(app , orient=VERTICAL) 
scroll.pack(side=RIGHT , fill=Y )

# var = Checkbutton(paraint , text='')
check_1 = Checkbutton(fr1 , text='mohamed') # Checkbutton te5dem kima checkbox 
check_2 = Checkbutton(fr1 , text="safe")
check_3 = Checkbutton(fr1 , text="yassine")
check_4 = Checkbutton(fr1 , text="najm eddine")

check_1.place(x=170 , y=115)
check_2.place(x=170 , y=145)
check_3.place(x=170 , y=175)
check_4.place(x=170 , y=205)

# var = Menubutton(paraint , text='' , relief=SUNKEN )
mn = Menubutton(fr1 , text='learn tkinter' , relief=SUNKEN ) # te5dem menu
mn.place(x=170 , y=235)

ss = Menu(mn) # lezemni na3mel selection lel menu eli 7ajti beha
mn["menu"] = ss # yelzemni nekteb menu kounchi metemchich
ss.add_checkbutton(label="html") # haka bech ba3mali list menu 
ss.add_checkbutton(label="css")  
ss.add_checkbutton(label="js")  
ss.add_checkbutton(label="python")  






















app.mainloop() # w ba3d n5adem el app bel mainloop() 