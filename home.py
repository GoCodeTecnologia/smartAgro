from tkinter import*
from tkinter import Tk, ttk
from time import strftime
from tkinter import messagebox

def time(): 
    string = strftime('%H:%M:%S %p') 
    label_quad1.config(text = string) 
    label_quad1.after(1000, time)

def notificacao():
    messagebox.showwarning("Atenção","Tela em Construção")

janela = Tk()
janela.title("SmartAgro - Soluções Inteligentes")

largura = 900
altura = 500
altura_screen = janela.winfo_screenheight()
largura_screen = janela.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.configure(bg="white")
janela.resizable(0,0)

navbar = Frame(janela, width=900,height=50,bg="green")
navbar.grid(row=0,column=0)

label_quad1 = Label(navbar,text="Bem vindo ao SmartAgro", height=1, anchor=NW, font=("Ivy 10 bold"), bg="green", fg="white")
label_quad1.place(x=50,y=15)

label_credito = Label(janela,text="Desenvolvido por GoCode Tecnologia™ - 2022", height=1, anchor=NW, font=("Ivy 10 bold"), bg="white", fg="green")
label_credito.place(x=250,y=470)

# Frame principal
quad1 = Frame(janela,width=200,height=180, bg="LimeGreen")
quad1.place(x=50,y=80)

label_quad1 = Label(quad1, height=1,
    anchor=NW, font=("Ivy 9 bold"), bg="LimeGreen", fg="white")
label_quad1.place(x=10,y=10)
time()

label_quad2 = Label(quad1,text="SÃO PAULO - SP", height=1, 
    anchor=NW, font=("Ivy 9 bold"), bg="LimeGreen", fg="white")
label_quad2.place(x=10,y=30)

label_quad3 = Label(quad1,text="25°C", height=1, 
    anchor=NW, font=("Ivy 24 bold"), bg="LimeGreen", fg="white")
label_quad3.place(x=10,y=70)

# Botões
btn_area = Button(janela, width=12, height=5, text="Área".upper(), anchor=CENTER, 
    font=("Ivy 8 bold"), fg="white", bg="DarkGreen", relief=FLAT, command=notificacao)
btn_area.place(x=50,y=280)

btn_talhao = Button(janela, width=12, height=5, text="Talhão".upper(), anchor=CENTER, 
    font=("Ivy 8 bold"), fg="white", bg="DarkGreen", relief=FLAT, command=notificacao)
btn_talhao.place(x=155,y=280)

btn_emissao = Button(janela, width=12, height=5, text="Atividades".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkGreen", relief=FLAT, command=notificacao)
btn_emissao.place(x=50,y=380)

btn_calculo = Button(janela, width=12, height=5, text="Produção".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkGreen", relief=FLAT, command=notificacao)
btn_calculo.place(x=155,y=380)

btn_cad_pragas = Button(janela, width=12, height=5, text="Frotas".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkOrange", relief=FLAT, command=notificacao)
btn_cad_pragas.place(x=270,y=80)

btn_cad_pragas = Button(janela, width=12, height=5, text="Transportes".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkOrange", relief=FLAT, command=notificacao)
btn_cad_pragas.place(x=380,y=80)

btn_cad_pragas = Button(janela, width=12, height=5, text="Edifícios".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkOrange", relief=FLAT, command=notificacao)
btn_cad_pragas.place(x=270,y=180)

btn_cad_metrica = Button(janela, width=12, height=5, text="Pragas".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="DarkOrange", relief=FLAT, command=notificacao)
btn_cad_metrica.place(x=380,y=180)

quad2 = Frame(janela,width=205,height=80, bg="MediumBlue")
quad2.place(x=490,y=80)

lbl_quad3 = Label(quad2,text="Total de Carbono Emitido CO²", height=1, 
    anchor=NW, font=("Ivy 10 bold"), bg="MediumBlue", fg="white")
lbl_quad3.place(x=5,y=8)

lbl_quad3 = Label(quad2,text="538.08 KG's", height=1, 
    anchor=NW, font=("Ivy 18 bold"), bg="MediumBlue", fg="white")
lbl_quad3.place(x=5,y=35)

quad3 = Frame(janela,width=205,height=80, bg="MediumBlue")
quad3.place(x=490,y=180)

lbl_quad3 = Label(quad3,text="Compensação em reais R$", height=1, 
    anchor=NW, font=("Ivy 8 bold"), bg="MediumBlue", fg="white")
lbl_quad3.place(x=5,y=8)

lbl_quad3 = Label(quad3,text="R$ 450,00", height=1, 
    anchor=NW, font=("Ivy 18 bold"), bg="MediumBlue", fg="white")
lbl_quad3.place(x=5,y=35)

btn_cad_metrica = Button(janela, width=12, height=5, text="Calculadora".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="Navy", relief=FLAT, command=notificacao)
btn_cad_metrica.place(x=490,y=280)

btn_cad_metrica = Button(janela, width=12, height=5, text="Cálculos".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="Navy", relief=FLAT, command=notificacao)
btn_cad_metrica.place(x=600,y=280)

btn_cad_metrica = Button(janela, width=12, height=5, text="Gráficos".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="Navy", relief=FLAT, command=notificacao)
btn_cad_metrica.place(x=490,y=380)

btn_cad_metrica = Button(janela, width=12, height=5, text="Relatórios".upper(), anchor=CENTER,
    font=("Ivy 8 bold"), fg="white", bg="Navy", relief=FLAT, command=notificacao)
btn_cad_metrica.place(x=600,y=380)

janela.mainloop()