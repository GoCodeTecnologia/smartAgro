from tkinter import*
from tkinter import Tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

janela = Tk()
janela.title("SmartAgro - Soluções Inteligentes")

largura = 427
altura = 250
altura_screen = janela.winfo_screenheight()
largura_screen = janela.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.configure(bg="white")
janela.resizable(0,0)

def show():
    messagebox.showinfo("Sucesso","Carregamento concluído")

def bar():
    l4 = Label(janela,text="Carregando aplicação...",fg="DarkGreen",bg="white")
    l4.place(x=0,y=210)
    import time
    r=0
    for i in range(100):
        progress['value']=r
        janela.update_idletasks()
        time.sleep(0.03)
        r=r+1
    janela.destroy()
    show()

progress = Progressbar(janela,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=-10,y=235)

lbl_title = Label(janela,text="SmartAgro",font=("Ivy 20 bold"),fg="DarkGreen",bg="white")
lbl_title.place(x=140,y=80)

lbl_subtitle = Label(janela,text="Soluções Agrônomo Inteligente",font=("Ivy 10 bold"),fg="DarkGreen",bg="white")
lbl_subtitle.place(x=110,y=115)

btn = Button(janela, width=10, height=1, text="Acessar", 
    command=bar, relief='flat', bg="DarkGreen", fg='white',font=("Ivy 10 bold"))
btn.place(x=170,y=180)

janela.mainloop()