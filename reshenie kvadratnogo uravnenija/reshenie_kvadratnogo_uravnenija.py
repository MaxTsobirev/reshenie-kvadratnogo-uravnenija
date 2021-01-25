from tkinter import *
from math import *
def lahenda():
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=(-1*b_+sqrt(D))/(2*a_)
            x2_=(-1*b_-sqrt(D))/(2*a_)
            tekst=f"X1={x1_},\nX2={x2_}"
        elif D==0:
            x1_=(-1*b_)/(2*a_)
            tekst=f"X1={x1_}"
        else:
            tekst="Корней НЕТ!"
        otvetq.configure(text=f"D={D}\n {tekst}")
    else:
        if a.get()=="": 
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")


okno=Tk() #sozdanieOkna
okno.geometry("600x200")
lbl=Label(okno,text="Решение квадратного уравенения",font="Arial 26",fg="red",bg="black") #fg- perednij fon, bg- zadnij
lbl.pack()

otvetq=Label(okno,height=4,width=60,bg="lightblue") #vqsota 4 stroki, shirina 20
otvetq.pack(side=BOTTOM)

a=Entry(okno,font="Arial 26",fg="blue",bg="black",width=3) #okno dlja vvoda (ja4eika)
a.pack(side=LEFT)
x2=Label(okno,text="x**2+",font="Arial 26",fg="blue")
x2.pack(side=LEFT)#budet drug za drugom
b=Entry(okno,font="Arial 26",fg="blue",bg="black",width=3)
b.pack(side=LEFT)
x=Label(okno,text="x+",font="Arial 26",fg="blue")
x.pack(side=LEFT)
c=Entry(okno,font="Arial 26",fg="blue",bg="black",width=3)
c.pack(side=LEFT)
Rovno=Label(okno,text="=0",font="Arial 26",fg="blue")
Rovno.pack(side=LEFT)

btn=Button(okno,text="Решить",font="Arial 26",bg="blue",command=lahenda)
btn.pack(side=LEFT)

okno.mainloop()