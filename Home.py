from tkinter import*
from tkinter import Tk,font
from tkinter.ttk import Progressbar

from Dashboard import*

janela = Tk()
janela.title("SmartAgro - Soluções Inteligentes")
# janela.iconbitmap('assets/icon.ico')

# Cores da aplicação
principal = "#003d59";
secundaria = "#01826e";
textRed = "#eb0202";
textBlue = "#002ef4";

largura = 450
altura = 300
altura_screen = janela.winfo_screenheight()
largura_screen = janela.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.configure(bg="white")
janela.resizable(0,0)

janela.defaultFont = font.nametofont("TkDefaultFont")
janela.defaultFont.configure(family="Nunito Sans", 
                                   size=10, 
                                   weight=font.BOLD)
def bar():
    l4 = Label(janela,text="Carregando aplicação...",fg=principal,bg="white")
    l4.place(x=50,y=210)
    import time
    r=0
    for i in range(100):
        progress['value']=r
        janela.update_idletasks()
        time.sleep(0.02)
        r=r+1
    janela.destroy()
    dashboard()

progress = Progressbar(janela,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=-10,y=235)

lbl_title = Label(janela,text="SmartAgro",font=("Ivy 20 bold"),fg=principal,bg="white")
lbl_title.place(x=50,y=80)

lbl_subtitle = Label(janela,text="Soluções Agrônomas Inteligente",fg=secundaria,bg="white")
lbl_subtitle.place(x=50,y=115)

lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
lbl_credits.place(x=140,y=270)

btn = Button(janela, width=10, height=1, text="Acessar", 
    command=bar, relief='flat', bg=principal, fg='white')
btn.place(x=50,y=180)

janela.mainloop()