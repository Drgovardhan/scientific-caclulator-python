from tkinter import*
from math import*
import parser
import tkinter.messagebox
expression=''
def press(num):
    global expression
    expression = expression + str(num) 
    equation.set(expression)
def POW():
    global expression
    l=expression.split(',')
    a=int(l[0])
    b=int(l[1])
    equation.set(int(pow(a,b)))
    epression=''
def GCD():
    global expression
    l=expression.split(',')
    a=int(l[0])
    b=int(l[1])
    c=gcd(a,b)
    for i in range(2,len(l)):
        c=gcd(c,int(l[i]))
    equation.set(int(c))
    epression=''
def equalpress():
    try:
        global expression        
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except:
        equation.set(" ERROR ") 
        expression = "" 
def sqrt_root():
    global expression 
    total =float(eval(expression))
    if total>0:
        s=sqrt(total)
        equation.set(s)
    else:
        equation.set('ERROR')
    
    expression = ""
def clear():
        global expression 
        expression = "" 
        equation.set("0")
def clear1():
        global expression 
        expression = "" 
        equation.set("")
def PI():
    global expression
    equation.set(pi) 
    expression = ""
def COS():
    global expression 
    total = eval(expression)
    equation.set(cos(total)) 
    expression=''
def TAN():
    global expression 
    total = eval(expression)
    equation.set(tan(total)) 
    expression = ""
def SIN():
    global expression 
    total = eval(expression)
    equation.set(sin(total)) 
    expression = ""
def TPI():
    global expression 
    equation.set(2*pi) 
    expression = ""
def LOG():
    global expression 
    total = eval(expression)
    equation.set(log(total)) 
    expression = ""
def EXP():
    global expression 
    total = eval(expression)
    equation.set(exp(total)) 
    expression = ""
def MOD():
    global expression 
    total = eval(expression)
    equation.set(fabs(total)) 
    expression = ""
def SINH():
    global expression 
    total = eval(expression)
    equation.set(sinh(total)) 
    expression = ""
def COSH():
    global expression 
    total = eval(expression)
    equation.set(cosh(total)) 
    expression = ""
def TANH():
    global expression 
    total = eval(expression)
    equation.set(tanh(total)) 
    expression = ""
def LOG2():
    global expression 
    total = eval(expression)
    equation.set(log2(total)) 
    expression = ""
def LOG10():
    global expression 
    total = eval(expression)
    equation.set(log10(total)) 
    expression = ""
def FACT():
    global expression 
    total = eval(expression)
    if total>0:
        x=factorial(total)
        equation.set(int(x))
    else:
        equation.set('ERROR')
    expression = ""
def ACOS():
    global expression 
    total = eval(expression)
    equation.set(acos(radians(total))) 
    expression = ""
def ASIN():
    global expression 
    total = eval(expression)
    equation.set(asin(radians(total))) 
    expression = ""
def ATAN():
    global expression 
    total = eval(expression)
    equation.set(atan(radians(total))) 
    expression = ""
    
root=Tk()
root.title('Scientific calclator')
root.iconbitmap(r'C:\Users\admin\Desktop\gova.ico')
root.configure(background='powder blue')
#root.resizable(0,0)
root.geometry('480x560+200+50')
calc=Frame(root)
calc.grid()
equation=StringVar()
t=Entry(calc,font=('arial',20,'bold'),textvariable=equation,bg='powder blue',bd=20,width=28,justify=RIGHT)
t.grid(row=0,column=0,columnspan=4,pady=1)
t.insert(0,'0')
numberpad='789456123'
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bg='powder blue',bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command']=lambda x = numberpad[i]:press(x)
        i+=1
btnCE=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='CE',
            command=clear1,bg='powder blue',bd=4).grid(row=1,column=0,pady=1)
btnC=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='C',
            command=clear,bg='powder blue',bd=4).grid(row=1,column=1,pady=1)
btnMod=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='%',
            command=lambda :press('%'),bg='powder blue',bd=4).grid(row=1,column=2,pady=1)
btndadd=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='+',
            command=lambda :press('+'),bg='powder blue',bd=4).grid(row=1,column=3,pady=1)
btnsub=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='-',
            command=lambda :press('-'),bg='powder blue',bd=4).grid(row=2,column=3,pady=1)

btnmul=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='*',
            command=lambda :press('*'),bg='powder blue',bd=4).grid(row=3,column=3,pady=1)
btndiv=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='÷',
            command=lambda :press('/'),bg='powder blue',bd=4).grid(row=4,column=3,pady=1)
btn0=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='0',
            command=lambda :press(0),bg='powder blue',bd=4).grid(row=5,column=0,pady=1)
btndot=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='.',
            command=lambda :press('.'),bg='powder blue',bd=4).grid(row=5,column=1,pady=1)
#btnPM=Button(c,width=6,height=2,font=('arial',20,'bold'),text=chr(177),
           # command=lambda :press(chr(177)),bg='powder blue',bd=4).grid(row=5,column=2,pady=1)
btnComma=Button(calc,width=6,height=2,font=('arial',20,'bold'),text=',',
            command=lambda :press(','),bg='powder blue',bd=4).grid(row=5,column=2,pady=1)
btnequal=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='=',
            command=equalpress,bg='powder blue',bd=4).grid(row=5,column=3,pady=1)

#==============================Scientific==================
btnPI=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='π',
            command=PI,bg='powder blue',bd=4).grid(row=1,column=5,pady=1)
btnCos=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='cos',
            command=COS,bg='powder blue',bd=4).grid(row=1,column=6,pady=1)
btnTan=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='tan',
            command=TAN,bg='powder blue',bd=4).grid(row=1,column=7,pady=1)
btnSin=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='sin',
            command=SIN,bg='powder blue',bd=4).grid(row=1,column=8,pady=1)
#=======================================================================
btntwo2PI=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='2π',
            command=TPI,bg='powder blue',bd=4).grid(row=2,column=5,pady=1)
btnCosh=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='cosh',
            command=COSH,bg='powder blue',bd=4).grid(row=2,column=6,pady=1)
btnTanh=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='tanh',
            command=TANH,bg='powder blue',bd=4).grid(row=2,column=7,pady=1)
btnSinh=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='sinh',
            command=SINH,bg='powder blue',bd=4).grid(row=2,column=8,pady=1)
#==========================================================================
btnLog=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='log',
            command=LOG,bg='powder blue',bd=4).grid(row=3,column=5,pady=1)
btnExp=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='exp',
            command=EXP,bg='powder blue',bd=4).grid(row=3,column=6,pady=1)
btnMod=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='mod',
            command=MOD,bg='powder blue',bd=4).grid(row=3,column=7,pady=1)
btnpow=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='pow',
            command=POW,bg='powder blue',bd=4).grid(row=3,column=8,pady=1)
#===========================================================================
btnsqrt=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='sqrt',
            command=sqrt_root,bg='powder blue',bd=4).grid(row=4,column=5,pady=1)
btnGcd=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='gcd',
            command=GCD,bg='powder blue',bd=4).grid(row=4,column=6,pady=1)
btnFact=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='factorial',
            command=FACT,bg='powder blue',bd=4).grid(row=4,column=7,pady=1)
btndAsinh=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='asinh',
            command=lambda :press('+'),bg='powder blue',bd=4).grid(row=4,column=8,pady=1)
#=============================================================================
btnLog10=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='log10',
            command=LOG10,bg='powder blue',bd=4).grid(row=5,column=5,pady=1)
btnaCos=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='acos',
            command=ACOS,bg='powder blue',bd=4).grid(row=5,column=6,pady=1)
btnaTan=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='atan',
            command=ATAN,bg='powder blue',bd=4).grid(row=5,column=7,pady=1)
btndaSin=Button(calc,width=6,height=2,font=('arial',20,'bold'),text='asin',
            command=ASIN,bg='powder blue',bd=4).grid(row=5,column=8,pady=1)
lb1display=Label(calc,text='Scientific Calculator',font=('arial',20,'bold'),justify=CENTER)

lb1display.grid(row=0,column=6,columnspan=4)

#===============MENU==================
def iexit():
    iexit=tkinter.messagebox.askyesno('Scientific calclatr','Confim if you want exit')
    if iexit>0:
        root.destroy()
        return
def Scientific():
    root.geometry('944x560')
def Standard():
    root.geometry('480x560')
menubar=Menu(calc)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Standard',command=Standard)
filemenu.add_command(label='Scientific',command=Scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=iexit)
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='cut')
editmenu.add_command(label='copy')
editmenu.add_separator()
editmenu.add_command(label='past')
helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='view help')

root.config(menu=menubar)





root.mainloop()
