from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
import tkinter.messagebox
import sqlite3                    #for Database

root=Tk()
root.geometry("500x590")
root.title("Registration Form")

imge=Image.open("man1.png")
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()

fn=StringVar()
ln=StringVar()
bob=StringVar()
var=StringVar()
var_c1="Java"
var_c2="Python"
radio_var=StringVar()
#-----------------------Fanction that print the values of user----------------------------
def printt():
	first=fn.get()
	sec=ln.get()
	bob1=bob.get()
	var1=var.get()
	va3=var_c1
	var3=var_c2
	var4=radio_var.get()
	print(f"Your Fullname Is {first}{sec}")
	print(f"Your Age Is {bob1}")
	print(f"Your Country Is {var1}")
	print(f"Your Program Language Is {var3}")
	print(f"Your Gender Is {var4}")
	tkinter.messagebox.showinfo("Welcome", 'User is successfully signed up !!')

#------------------------Fanction that exit with the button-------------------------------
def exit1():
	exit()

#-------------------Fanction that show a message when you press About from menu-----------
def abt():
	tkinter.messagebox.showinfo("Welcome to authors", "This is demo for menu fields")

#-----------------------Fanction that opening another window-----------------------------
def sec_win():
	window=Tk()
	window.title("Welcome to second window")
	window.geometry('250x200')
	label_02=Label(window,text='Registration Completed', relief='solid',font=('arial',12,'bold')).place(x=30,y=70)
	but_02=Button(window,text="Exit",width=12,fg='white',bg='brown',command=exit1).place(x=80,y=110)


def database():
	name1=fn.get()
	last1=ln.get()
	date=bob.get()
	country=var.get()
	Prog=var_c2
	Gender=radio_var.get()
	conn=sqlite3.connect("Form.db")
	with conn:
		cursor=conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Last TEXT,DOB TEXT,country TEXT,Programming TEXT,Gender TEXT)')
	cursor.execute('INSERT INTO Student(Name,Last,DOB,country,Programming,Gender) VALUES (?,?,?,?,?,?)',(name1,last1,date,country,Prog,Gender))
	conn.commit()
	conn.close()

#-----------------Creating the buttons,droplist,checkbutton------------------------------
label1=Label (root,text="Registration Form",width=20,font=("arial",19,"bold"))
label1.place(x=90,y=150)

entry_1=Entry(root, textvar=fn)
entry_1.place(x=240,y=242)

label2=Label (root,text="First Name :",width=20,font=("bold",10))
label2.place(x=80,y=240)

entry_2=Entry(root, textvar=ln)
entry_2.place(x=240,y=282)

label3=Label (root,text="Last Name :",width=20,font=("bold",10))
label3.place(x=80,y=280)

label4=Label (root,text="Country :",width=20,font=("bold",10))
label4.place(x=75,y=370)

entry_3=Entry(root, textvar=bob)
entry_3.place(x=240,y=320)

label5=Label (root,text="bob :",width=20,font=("bold",10))
label5.place(x=65,y=320)

list1=['Greece','Germany','Canada','India']
droplist=OptionMenu(root,var,*list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=230,y=370)

label4=Label (root,text="Prog Lang :",width=20,font=("bold",10))
label4.place(x=80,y=420)

c1=Checkbutton(root, text="Java",variable=var_c1)
c1.place(x=235,y=420)
c1=Checkbutton(root, text="Python",variable=var_c2)
c1.place(x=290,y=420)

r1=Radiobutton(root, text="Male",variable=radio_var,value="Male")
r1.place(x=230,y=460)

r2=Radiobutton(root, text="Female",variable=radio_var,value="Female")
r2.place(x=290,y=460)


label4=Label (root,text="Gender :",width=20,font=("bold",10))
label4.place(x=73,y=459)

#-------------------------Create a Button----------------------------------
button_singup=Button(root,text="Signup",width=12,fg='white',bg='brown',command=database).place(x=130,y=515)
root.bind("<Return>", database)

button_exit=Button(root,text="Exit",width=12,fg='white',bg='brown',relief=RAISED,command=exit1)
button_exit.place(x=280,y=515)

button_login=Button(root,text="Login",width=12,fg='white',bg='brown',command=sec_win)
button_login.place(x=208,y=560)

#--------------------Creating a menu bar----------------------------------------
menu=Menu(root)
root.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit",command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)



root.mainloop()
