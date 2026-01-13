import tkinter as tk
from tkinter.ttk import Label

import mysql.connector as mc
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
a=tk.Tk()
a.geometry('1600x900')
a.title('SS FOOTWEAR')
a.config(bg='ghost white')

f=tk.Frame(a)
f.pack(side=tk.LEFT,fill=tk.BOTH)
f.config(width=1400)


def clear():
    for widget in f.winfo_children():
        widget.destroy()

db = mc.connect(
    host="localhost",
    user="root",      # replace with your MySQL username
    password="sharvesh1234",  # replace with your MySQL password
    database="registration" # replace with your database name
)
cursor = db.cursor()


def register():
    username = e.get()
    gmail = e1.get()
    password=e2.get()
    mobnum1=e3.get()
    gender=e4.get()
    if username == "" or gmail == "" or password=="" or mobnum1 =="" or gender=="":
        messagebox.showerror("Error", "All fields are required")
        return
    # Check if the username already exists
    cursor.execute("SELECT * FROM details WHERE name = %s", (username,))
    if cursor.fetchall():
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new user into the database
        cursor.execute("INSERT INTO details (name,gmail,password,mobilenum,gender) VALUES (%s, %s,%s,%s,%s)", (username,gmail,password,mobnum1,gender))
        db.commit()
        messagebox.showinfo("Success", "Registration successful")


def login():
    global e_1,e_2
    lo = tk.Frame(f)
    lo.pack(side=tk.LEFT, fill=tk.BOTH)
    lo.config(width=1400)
    b2 = tk.Button(lo, text="Back", bg="grey", fg="white", font=("italic", 10),command=lambda: [(clear(), frame0())])
    b2.place(x=30, y=40)
    img1='sstop.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(lo,image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=544, y=20)
    u=tk.Label(lo,text='USERNAME',font=('aerial',15))
    u.place(x=464,y=245)
    e_1=tk.Entry(lo,width=20,font=('aerial',15))
    e_1.place(x=610,y=245)
    pw = tk.Label(lo, text='PASSWORD', font=('aerial', 15))
    pw.place(x=460, y=290)
    e_2 = tk.Entry(lo, width=20,show="*", font=('aerial', 15))
    e_2.place(x=610, y=290)
    s = tk.Button(lo, text='LOGIN', font=("aerial", 14), bg='red',fg='white', command=lambda: [(login1())])
    s.place(x=630, y=360)


def login1():
    username = e_1.get()
    password = e_2.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return
    # Check if the credentials are correct
    cursor.execute("SELECT * FROM details WHERE name = %s AND password = %s", (username, password))
    if cursor.fetchall():
        messagebox.showinfo("Success", "Login successful")
        clear()
        frame1()
    else:
        messagebox.showerror("Error", "Invalid username or password")
        login()


def frame0():
    f0 = tk.Frame(f)
    f0.pack(side=tk.LEFT, fill=tk.BOTH)
    f0.config(width=1400)

    r = tk.Label(f, text='REGISTRATION', bg='thistle4', fg='black', font=('aerial', 15))
    r.place(x=620, y=125)

    n = tk.Label(f, text='NAME', font=('aerial', 15))
    n.place(x=518, y=200)
    e = tk.Entry(f, width=20, font=('aerial', 15))
    e.place(x=600, y=200)

    g = tk.Label(f, text='GMAIL', font=('aerial', 15))
    g.place(x=512, y=245)
    e1 = tk.Entry(f, width=20, font=('aerial', 15))
    e1.place(x=600, y=245)

    pw = tk.Label(f, text='PASSWORD', font=('aerial', 15))
    pw.place(x=460, y=290)
    e2 = tk.Entry(f, width=20, show="*", font=('aerial', 15))
    e2.place(x=600, y=290)

    n = tk.Label(f, text='MOBILE NUMBER', font=('aerial', 15))
    n.place(x=410, y=330)
    e3 = tk.Entry(f, width=20, font=('aerial', 15))
    e3.place(x=600, y=330)

    ge = tk.Label(f, text='GENDER', font=('aerial', 15))
    ge.place(x=492, y=370)
    e4 = tk.Entry(f, width=20, font=('aerial', 15))
    e4.place(x=600, y=370)

    ag = tk.Label(f, text='AGE', font=('aerial', 15))
    ag.place(x=532, y=410)
    entry = tk.Spinbox(f, width=19, from_=18, to=60, font=('aerial', 15))
    entry.place(x=600, y=410)

    l = tk.Button(f, text='LOGIN', font=("bold", 10), bg='red',fg='white', command=lambda: [(clear(), login())])
    l.place(x=620, y=470)

    r1 = tk.Button(f, text='REGISTER', font=('bold', 10), bg='red',fg='white', command=lambda: [(clear(), login())])
    r1.place(x=700, y=470)


def frame1():
    frame_1 = tk.Frame(f)
    frame_1.pack(side=tk.LEFT, fill=tk.BOTH)
    frame_1.config(width=1400)


    b2 = tk.Button(frame_1, text="Back", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), login())])
    b2.place(x=30, y=40)

    men=tk.Button(frame_1,text='MEN',bg='red',fg='snow',width=15,command=lambda:[(clear(),frame2())])
    men.place(x=300,y=440)

    img1 = 'MENLOGO.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=260, y=195)

    women=tk.Button(frame_1,text='WOMEN',bg='red',fg='snow',width=15,command=lambda:[(clear(),frame3())])
    women.place(x=600,y=440)

    img1 = 'WOMANLOGO.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=560, y=195)

    kids=tk.Button(frame_1,text='KIDS',bg='red',fg='snow',width=15,command=lambda:[(clear(),frame4())])
    kids.place(x=900,y=440)

    img1 = 'KIDSLOGO.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=860, y=195)

    img1='sstop.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_1,image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=544, y=20)


def confirm_order():
    name = ea.get()
    mobile = ea1.get()
    address=ea2.get()
    if name == "" or mobile == "" or address=="":
        messagebox.showerror("Error", "All fields are required")
        return
    else:
        messagebox.showinfo("Success", "ORDER PLACED SUCCESSFULLY")
        frame1()

def cal_1():
    q1 = int(ea3.get())
    q2 = 2094
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20=tk.Label(f,text="TOTAL AMOUNT :",bg='red',fg='white',font=("italic", 13))
    c_20.place(x=900,y=330)

def address_mm1():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_1)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)


def m_1():
    global mp1
    m1 = tk.Frame(f)
    m1.pack(side=tk.LEFT, fill=tk.BOTH)
    m1.config(width=1400)

    b2 = tk.Button(m1, text="Back", bg="grey", fg="white", font=("italic", 10),command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'MM_1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(m1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(m1, text='MEN', font=('aerial', 24))
    t.place(x=640, y=25)

    mm1 = tk.Label(m1, text='Men Black Formal Moccasin',font='bold',width=50)
    mm1.place(x=630, y=150)
    mp1=tk.Label(m1,text='Rs. 2094.00',font='bold',width=50)
    mp1.place(x=630,y=200)

    pl=tk.Button(m1,text='PLACE ORDER',font=("aerial", 15),bg='red',fg='white', command=lambda: [(clear(),address_mm1())])
    pl.place(x=780,y=250)


def cal_2():
    q1 = int(ea3.get())
    q2 = 1618
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20 = tk.Label(f, text="TOTAL AMOUNT :", bg='red', fg='white', font=("italic", 13))
    c_20.place(x=900, y=330)


def address_mm2():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_2)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)


def m_2():
    global mp2
    m2 = tk.Frame(f)
    m2.pack(side=tk.LEFT, fill=tk.BOTH)
    m2.config(width=1400)

    b2 = tk.Button(m2, text="Back", bg="grey", fg="white", font=("italic", 10),command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'MM_2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(m2, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(m2, text='MEN', font=('aerial', 24))
    t.place(x=640, y=25)

    mm2 = tk.Label(m2, text='Men Black Ethnic Slippers', font='bold', width=50)
    mm2.place(x=630, y=150)

    mp2 = tk.Label(m2, text='Rs. 1618.00', font='bold', width=50)
    mp2.place(x=630, y=200)

    pl = tk.Button(m2, text='PLACE ORDER', font=("aerial", 15), bg='red',fg='white', command=lambda: [(clear(), address_mm2())])
    pl.place(x=780, y=250)


def frame2():
    frame_2 = tk.Frame(f)
    frame_2.pack(side=tk.LEFT, fill=tk.BOTH)
    frame_2.config(width=1400)

    b2 = tk.Button(frame_2, text="Back", bg="grey", fg="white", font=("italic", 10),command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    t = tk.Label(f, text='MEN',font=('aerial',24))
    t.place(x=640,y=25)

    m1=tk.Button(frame_2,text='Men Black Formal Moccasin',bg='red',fg='snow',width=26,command=lambda: [(clear(),m_1())])
    m1.place(x=270,y=440)

    img1 = 'M1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_2, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=240, y=175)

    m2 = tk.Button(frame_2, text='Men Black Ethnic Slippers', bg='red', fg='snow', width=26,command=lambda: [(clear(),m_2())])
    m2.place(x=900, y=440)

    img1 = 'M2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_2, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=860, y=175)

def cal_3():
    q1 = int(ea3.get())
    q2 = 1293
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20 = tk.Label(f, text="TOTAL AMOUNT :", bg='red', fg='white', font=("italic", 13))
    c_20.place(x=900, y=330)


def address_ww1():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_3)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)

def w_1():
    global wp1
    w1 = tk.Frame(f)
    w1.pack(side=tk.LEFT, fill=tk.BOTH)
    w1.config(width=1400)

    b2 = tk.Button(w1, text="Back", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'WW_1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(w1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(w1, text='WOMEN', font=('aerial', 24))
    t.place(x=640, y=25)

    ww1 = tk.Label(w1, text='Women Black Formal Pumps', font='bold', width=50)
    ww1.place(x=630, y=150)

    wp1 = tk.Label(w1, text='Rs. 1293.00', font='bold', width=50)
    wp1.place(x=630, y=200)

    pl = tk.Button(w1, text='PLACE ORDER', font=("aerial", 15), bg='red',fg='white', command=lambda: [(clear(), address_ww1())])
    pl.place(x=780, y=250)


def cal_4():
    q1 = int(ea3.get())
    q2 = 1094
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20 = tk.Label(f, text="TOTAL AMOUNT :", bg='red', fg='white', font=("italic", 13))
    c_20.place(x=900, y=330)


def address_ww2():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_4)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)

def w_2():
    global wp2
    w2 = tk.Frame(f)
    w2.pack(side=tk.LEFT, fill=tk.BOTH)
    w2.config(width=1400)

    b2 = tk.Button(w2, text="Back", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'WW_2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(w2, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(w2, text='WOMEN', font=('aerial', 24))
    t.place(x=640, y=25)

    ww2 = tk.Label(w2, text='Women Peach Casual Sandals', font='bold', width=50)
    ww2.place(x=630, y=150)

    wp2 = tk.Label(w2, text='Rs. 1094.00', font='bold', width=50)
    wp2.place(x=630, y=200)

    pl = tk.Button(w2, text='PLACE ORDER', font=("aerial", 15), bg='red',fg='white', command=lambda: [(clear(), address_ww2())])
    pl.place(x=780, y=250)

def frame3():
    frame_3 = tk.Frame(f)
    frame_3.pack(side=tk.LEFT, fill=tk.BOTH)
    frame_3.config(width=1400)

    b2 = tk.Button(frame_3, text="Back", bg="grey", fg="white", font=("italic", 10),command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    t = tk.Label(f, text='WOMAN',font=('aerial',24))
    t.place(x=640,y=25)

    w1 = tk.Button(frame_3, text='Women Black Formal Pumps', bg='red', fg='snow', width=26,command=lambda: [(clear(), w_1())])
    w1.place(x=270, y=440)

    img1 = 'W1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_3, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=240, y=175)

    w2 = tk.Button(frame_3, text='Women Peach Casual Sandals', bg='red', fg='snow', width=26,command=lambda: [(clear(), w_2())])
    w2.place(x=900, y=440)

    img1 = 'W2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_3, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=860, y=175)


def cal_5():
    q1 = int(ea3.get())
    q2 = 990
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20 = tk.Label(f, text="TOTAL AMOUNT :", bg='red', fg='white', font=("italic", 13))
    c_20.place(x=900, y=330)


def address_kk1():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_5)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)

def k_1():
    global kp1
    k1 = tk.Frame(f)
    k1.pack(side=tk.LEFT, fill=tk.BOTH)
    k1.config(width=1400)

    b2 = tk.Button(k1, text="Back", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'KK_1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(k1, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(k1, text='KIDS', font=('aerial', 24))
    t.place(x=640, y=25)

    kk1= tk.Label(k1, text='Boys Blue Casual Loafers', font='bold', width=50)
    kk1.place(x=630, y=150)

    kp1 = tk.Label(k1, text='Rs. 990.00', font='bold', width=50)
    kp1.place(x=630, y=200)

    pl = tk.Button(k1, text='PLACE ORDER', font=("aerial", 15), bg='red',fg='white', command=lambda: [(clear(), address_kk1())])
    pl.place(x=780, y=250)


def cal_6():
    q1 = int(ea3.get())
    q2 = 1290
    c20 = tk.Label(f, text=q1 * q2,font=("italic", 13))
    c20.pack()
    c20.place(x=1046, y=330)
    c_20 = tk.Label(f, text="TOTAL AMOUNT :", bg='red', fg='white', font=("italic", 13))
    c_20.place(x=900, y=330)


def address_kk2():
    global ea,ea1,ea2,ea3,q
    r = tk.Label(f, text='DELIVERY ADDRESS', bg='black', fg='white', font=('bold', 15))
    r.place(x=604, y=125)

    b2 = tk.Button(f, text="HOME", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    n = tk.Label(f,text='NAME', font=('aerial', 15))
    n.place(x=521, y=200)
    ea= tk.Entry(f,width=20, font=('aerial', 15))
    ea.place(x=600, y=200)

    age = tk.Label(f,text='MOBILE',  font=('aerial', 15))
    age.place(x=500, y=245)
    ea1 = tk.Entry(f,width=20, font=('aerial', 15))
    ea1.place(x=600, y=245)

    g = tk.Label(f,text='ADDRESS', font=('aerial', 15))
    g.place(x=480, y=290)
    ea2= tk.Entry(f, width=20, font=('aerial', 15))
    ea2.place(x=600, y=290)

    q = tk.Label(f, text='QUANTITY', font=('aerial', 15))
    q.place(x=474, y=330)
    ea3= tk.Spinbox(f, width=19, from_=1, to=10, font=('aerial', 15))
    ea3.place(x=600, y=330)

    t=tk.Button(f,text='TOTAL',font=('bold',8),command=cal_6)
    t.place(x=834,y=330)

    s= tk.Label(f,text='SIZE', font=('aerial', 15))
    s.place(x=528, y=370)
    ea4 = tk.Spinbox(f,width=19, from_=6, to=12, font=('aerial', 15))
    ea4.place(x=600, y=370)

    c= tk.Button(f, text='CONFIRM ORDER',font=('bold',10), bg='red',fg='white',command=lambda: [(confirm_order())])
    c.place(x=646, y=440)

def k_2():
    global kp2
    k2 = tk.Frame(f)
    k2.pack(side=tk.LEFT, fill=tk.BOTH)
    k2.config(width=1400)

    b2 = tk.Button(k2, text="Back", bg="grey", fg="white", font=("italic", 10), command=lambda: [(clear(), frame1())])
    b2.place(x=30, y=40)

    img1 = 'KK_2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)
    label0 = tk.Label(k2, image=photo1, bg="light steel blue")
    label0.image = photo1
    label0.place(x=200, y=145)

    t = tk.Label(k2, text='KIDS', font=('aerial', 24))
    t.place(x=640, y=25)

    kk2 = tk.Label(k2, text='Girls Gold Casual Ballerinas', font='bold', width=50)
    kk2.place(x=630, y=150)

    kp2 = tk.Label(k2, text='Rs. 1290.00', font='bold', width=50)
    kp2.place(x=630, y=200)

    pl = tk.Button(k2,text='PLACE ORDER',font=("aerial", 15),bg='red',fg='white',command=lambda:[(clear(),address_kk2())])
    pl.place(x=780, y=250)

def frame4():
    frame_4 = tk.Frame(f)
    frame_4.pack(side=tk.LEFT,fill=tk.BOTH)
    frame_4.config(width=1400)

    b2 = tk.Button(frame_4,text="Back",bg="grey",fg="white",font=("italic", 10),command=lambda: [(clear(),frame1())])
    b2.place(x=30, y=40)

    t = tk.Label(f,text='KIDS',font=('aerial',24))
    t.place(x=640,y=25)

    k1 = tk.Button(frame_4,text='Boys Blue Casual Loafers',bg='red',fg='snow',width=26,command=lambda:[(clear(),k_1())])
    k1.place(x=270, y=440)

    img1 = 'K1.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_4,image=photo1,bg="light steel blue")
    label0.image = photo1
    label0.place(x=240, y=175)

    k2 = tk.Button(frame_4,text='Girls Gold Casual Ballerinas', bg='red', fg='snow', width=26,command=lambda: [(clear(), k_2())])
    k2.place(x=900, y=440)

    img1 = 'K2.jpg'
    pic1 = Image.open(img1)
    photo1 = ImageTk.PhotoImage(pic1)

    label0 = tk.Label(frame_4,image=photo1,bg="light steel blue")
    label0.image = photo1
    label0.place(x=860, y=175)

r=tk.Label(f,text='REGISTRATION',bg='black',fg='white',font=('bold',15))
r.place(x=620,y=125)

n = tk.Label(f, text='NAME',font=('aerial', 15))
n.place(x=518, y=200)
e = tk.Entry(f, width=20, font=('aerial', 15))
e.place(x=600, y=200)

g = tk.Label(f, text='GMAIL',font=('aerial', 15))
g.place(x=512, y=245)
e1 = tk.Entry(f, width=20,font=('aerial', 15))
e1.place(x=600, y=245)

pw= tk.Label(f, text='PASSWORD',font=('aerial', 15))
pw.place(x=460, y=290)
e2 = tk.Entry(f, width=20, show="*",font=('aerial', 15))
e2.place(x=600, y=290)

n = tk.Label(f, text='MOBILE NUMBER',font=('aerial', 15))
n.place(x=410, y=330)
e3 = tk.Entry(f, width=20,font=('aerial', 15))
e3.place(x=600, y=330)

ge=tk.Label(f, text='GENDER',font=('aerial', 15))
ge.place(x=492,y=370)
e4=tk.Entry(f,width=20, font=('aerial', 15))
e4.place(x=600,y=370)

ag = tk.Label(f, text='AGE', font=('aerial', 15))
ag.place(x=532, y=410)
entry = tk.Spinbox(f, width=19,from_=18, to=60,font=('aerial', 15))
entry.place(x=600,y=410)

l = tk.Button(f, text='LOGIN', font=("bold", 12),bg='red',fg='white',command=lambda: [(clear(), login())])
l.place(x=620, y=470)

r1=tk.Button(f,text='REGISTER',font=('bold',12),bg='red',fg='white',command=lambda:[(register())])
r1.place(x=700, y=470)


a.mainloop()

