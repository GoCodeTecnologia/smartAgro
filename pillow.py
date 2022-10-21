from tkinter import*
from tkinter import Tk
from PIL import Image, ImageTk 

janela = Tk()
janela.title("SmartAgro - Soluções Inteligentes")

largura = 900
altura = 500
altura_screen = janela.winfo_screenheight()
largura_screen = janela.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.configure(bg="gray")
janela.resizable(0,0)

# Frame
lbl_nome = Label(janela,text='Nome', font=('Ivy 10 bold'),width=20)
lbl_nome.place(x=10,y=10)

lbl_nome = Entry(janela, font=('Ivy 10 bold'),width=20)
lbl_nome.place(x=180,y=10)

btn_icon = Image.open('add.png')
btn_icon = btn_icon.resize((20,20))
btn_icon = ImageTk.PhotoImage(btn_icon)

btn_cadastrar = Button(janela, image=btn_icon, width=100, text='Cadastrar', compound=LEFT,
                    anchor=CENTER)
btn_cadastrar.place(x=10,y=60)

janela.mainloop()