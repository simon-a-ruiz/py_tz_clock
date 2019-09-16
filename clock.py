from tkinter import *
from datetime import datetime
import time
import pytz


def Draw():
	global label_t_local
	global label_t_utc
	global label_t_na_west
	global label_t_uk_london
	global label_t_au_sydney
	global label_d_local
	global label_d_utc
	global label_d_na_west
	global label_d_uk_london
	global label_d_au_sydney
	label_t_na_west = Label(frame2, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_t_local = Label(frame5, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_t_utc = Label(frame8, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_t_uk_london = Label(frame11, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_t_au_sydney = Label(frame14, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_d_local = Label(frame3, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_d_uk_london = Label(frame6, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_d_utc = Label(frame9, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_d_na_west = Label(frame12, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_d_au_sydney = Label(frame15, text="Loading...", background="black", fg="red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=RIGHT)
	label_t_local.pack()
	label_t_utc.pack()
	label_t_na_west.pack()
	label_t_uk_london.pack()
	label_t_au_sydney.pack()
	label_d_local.pack()
	label_d_utc.pack()
	label_d_na_west.pack()
	label_d_uk_london.pack()
	label_d_au_sydney.pack()

def Refresher():
	global label_t_local
	global label_t_utc
	global label_t_na_west
	global label_t_uk_london
	global label_t_au_sydney
	global label_d_local
	global label_d_utc
	global label_d_na_west
	global label_d_uk_london
	global label_d_au_sydney
	tz_indianapolis = pytz.timezone('America/Indiana/Indianapolis')
	tz_utc = pytz.timezone('UTC')
	tz_na_west = pytz.timezone('America/Los_Angeles')
	tz_uk_london = pytz.timezone('Europe/London')
	tz_au_sydney = pytz.timezone('Australia/Sydney')
	label_t_local.configure(text=datetime.now(tz_indianapolis).strftime("%H:%m:%S"), fg="DeepSkyBlue2")
	label_d_local.configure(text=datetime.now(tz_indianapolis).strftime("%Y/%m/%d"), fg="white")
	label_t_utc.configure(text=datetime.now(tz_utc).strftime("%H:%m:%S"), fg="DeepSkyBlue2")
	label_d_utc.configure(text=datetime.now(tz_utc).strftime("%Y/%m/%d"), fg="white")
	label_t_na_west.configure(text=datetime.now(tz_na_west).strftime("%H:%m:%S"), fg="DeepSkyBlue2")
	label_d_na_west.configure(text=datetime.now(tz_na_west).strftime("%Y/%m/%d"), fg="white")
	label_t_uk_london.configure(text=datetime.now(tz_uk_london).strftime("%H:%m:%S"), fg="DeepSkyBlue2")
	label_d_uk_london.configure(text=datetime.now(tz_uk_london).strftime("%Y/%m/%d"), fg="white")
	label_t_au_sydney.configure(text=datetime.now(tz_au_sydney).strftime("%H:%m:%S"), fg="DeepSkyBlue2")
	label_d_au_sydney.configure(text=datetime.now(tz_au_sydney).strftime("%Y/%m/%d"), fg="white")
	root.after(1000, Refresher)

root = Tk()
#root.wm_attributes('-alpha',0.6)
root.wm_minsize(width=500, height=1)
root.title(string="Timezone Clock")
root.configure(background="")

frame1 = Frame(root, width=200, height=100, background="black")
frame2 = Frame(root,width=200,height=100,background='black')
frame3 = Frame(root,width=200,height=100,background='black')
frame4 = Frame(root,width=200,height=100,background='black')
frame5 = Frame(root,width=200,height=100,background='black')
frame6 = Frame(root,width=200,height=100,background='black')
frame7 = Frame(root,width=200,height=100,background='black')
frame8 = Frame(root,width=200,height=100,background='black')
frame9 = Frame(root,width=200,height=100,background='black')
frame10 = Frame(root,width=200,height=100,background='black')
frame11 = Frame(root,width=200,height=100,background='black')
frame12 = Frame(root,width=200,height=100,background='black')
frame13 = Frame(root,width=200,height=100,background='black')
frame14 = Frame(root,width=200,height=100,background='black')
frame15 = Frame(root,width=200,height=100,background='black')

frame1.grid(row=0,column=0, sticky = W)
frame2.grid(row=0,column=1, sticky = W)
frame3.grid(row=0,column=2, sticky = E)
frame4.grid(row=1,column=0, sticky = W)
frame5.grid(row=1,column=1, sticky = W)
frame6.grid(row=1,column=2, sticky = E)
frame7.grid(row=2,column=0, sticky = W)
frame8.grid(row=2,column=1, sticky = W)
frame9.grid(row=2,column=2, sticky = E)
frame10.grid(row=3,column=0, sticky = W)
frame11.grid(row=3,column=1, sticky = W)
frame12.grid(row=3,column=2, sticky = E)
frame13.grid(row=4,column=0, sticky = W)
frame14.grid(row=4,column=1, sticky = W)
frame15.grid(row=4,column=2, sticky = E)

label_d_na_west = Label(frame1, text="NA/West", background="black", fg="white", font=('Arial', 20,"bold"), padx=20, pady=3, justify=LEFT)
label_d_local = Label(frame4, text="Indianapolis", background="black", fg="yellow", font=('Arial', 20,"bold"), padx=20, pady=3, justify=LEFT)
label_d_utc = Label(frame7, text="UTC", background="black", fg="orange red", font=('Arial', 20,"bold"), padx=20, pady=3, justify=LEFT)
label_d_uk_london = Label(frame10, text="UK/London", background="black", fg="white", font=('Arial', 20,"bold"), padx=20, pady=3, justify=LEFT)
label_d_au_sydney = Label(frame13, text="AU/Sydney", background="black", fg="white", font=('Arial', 20,"bold"), padx=20, pady=3, justify=LEFT)

label_d_local.pack(expand=True, fill='both')
label_d_utc.pack(expand=True, fill='both')
label_d_na_west.pack(expand=True, fill='both')
label_d_uk_london.pack(expand=True, fill='both')
label_d_au_sydney.pack(expand=True, fill='both')


Draw()
Refresher()
root.mainloop()
