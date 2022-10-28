from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

from DcCommand import*

janela = Tk()
janela.title("SmartAgro - Emissão CO² Cadastro de Dados")
global tree

principal = "#003d59";
secundaria = "#01826e";
textBlue = "#002ef4";

largura = 1000
altura = 600
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

lbl_title = Label(janela,text="SmartAgro",font=("Ivy 20 bold"),fg=principal,bg="white")
lbl_title.place(x=10,y=20)
lbl_subtitle = Label(janela,text="Soluções Agrônomo Inteligente",fg=secundaria,bg="white")
lbl_subtitle.place(x=10,y=55)

container = Frame(janela,width=980,height=490)
container.place(x=10,y=80)

# ==========================================================================================================
# Informações
lbl_title = Label(container,text="Total de Emissão por Veiculos ",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=20)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=50)

lbl_title = Label(container,text="Total de Emissão da Fazenda ",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=80)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=110)

lbl_title = Label(container,text="Total de Emissão da Plantação ",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=140)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=170)

lbl_title = Label(container,text="Árvores para compensar ",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=200)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=230)

lbl_title = Label(container,text="Consumo Total de Kwh",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=290)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=320)

lbl_title = Label(container,text="Consumo Total em R$",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=10,y=350)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=10,y=380)

# ====== lado direito
lbl_title = Label(container,text="Emissão por Diesel",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=20)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=50)

lbl_title = Label(container,text="Emissão por Flex ",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=80)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=110)

lbl_title = Label(container,text="Emissão por Gasolina",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=140)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=170)

lbl_title = Label(container,text="Emissão por GNV",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=200)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=230)

lbl_title = Label(container,text="Emissão por Calcário",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=290)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=320)

lbl_title = Label(container,text="Emissão por Uréia",font=("Ivy 15 bold"),fg=principal)
lbl_title.place(x=350,y=350)
lbl_subtitle = Label(container,text="200 CO² ",font=("Ivy 12 bold"),fg=secundaria)
lbl_subtitle.place(x=350,y=380)
# ==========================================================================================================
lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
lbl_credits.place(x=400,y=570)

janela.mainloop()