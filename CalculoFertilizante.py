from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

def calcFertilizante():
    janela = Toplevel()
    janela.title("SmartAgro - Emissão CO² Fertilizante")
    # janela.iconbitmap('assets/icon.ico')

    def calCalcario():
        try:
            klCalc = float(input_calcario.get())
            klDolomitico = float(input_dolomito.get())

            if klCalc <0:
                messagebox.showerror("Erro","Insira valores válidos")
            elif klDolomitico <0:
                messagebox.showerror("Erro","Insira valores válidos")

            fatorCalcario = 0.12
            fatorDolomitico = 0.13
            resultadoCalc = ((klCalc * fatorCalcario + klDolomitico * fatorDolomitico) * 44 / 12)
            lbl_resultado_calcario.config(text=round(resultadoCalc, 2))
            lbl_metrica_calcario.config(text="O Calcário é um insumo agrícola usado para elevar o pH\n(potencial hidrogeniônico) do solo, o que diminui a acidez")
        except:
            messagebox.showerror("Erro","Dados inválidos ou não informados")
            janela.destroy()

    def calcUreia():
        try:
            kl = float(input_ureia.get())
            if kl <0:
                messagebox.showerror("Erro","Insira valores válidos")
            fatorUreia = 0.20
            resultado = (kl * fatorUreia * 44 / 12)
            lbl_resultado_ureia.config(text=round(resultado,2))
            lbl_metrica_ureia.config(text="A Uréia é um fertilizante sólido muito utilizado para adubação\nem grandes quantidades e com grande eficácia")
        except:
            messagebox.showerror("Erro","Dados inválidos ou não informados")
            janela.destroy()

    # Cores da aplicação
    principal = "#003d59";
    secundaria = "#01826e";
    textBlue = "#002ef4";

    largura = 900
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
    # Textos de titulo e subtitulo
    lbl_title = Label(janela,text="SmartAgro",font=("Ivy 20 bold"),fg=principal,bg="white")
    lbl_title.place(x=10,y=20)
    lbl_subtitle = Label(janela,text="Soluções Agrônomas Inteligente",fg=secundaria,bg="white")
    lbl_subtitle.place(x=10,y=55)

    # Corpo da aplicação
    container = Frame(janela,width=880,height=490)
    container.place(x=10,y=80)

    # Cálculo da emissão de uréia

    lbl_title_parameter = Label(container,text="Calcular emissão de CO² - Fertilizante",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=840,height=140,bg="white")
    boxBtn.place(x=20,y=50)

    boxBtn2 = Frame(container,width=840,height=190,bg="white")
    boxBtn2.place(x=20,y=200)
    # Formulario de calculo
    lbl_ureia = Label(boxBtn,text="Calculo com Uréia",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_ureia.place(x=20,y=10)
    lbl_ureia = Label(boxBtn,text="Digite a quantidade de kilos de uréia",font=("Nunito 8"),fg=secundaria,bg="white")
    lbl_ureia.place(x=20,y=40)
    input_ureia = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_ureia.place(x=20,y=60)
    input_ureia.config(highlightbackground=principal, highlightcolor=principal)

    btn_calcular = Button(boxBtn,width=22, height=1, text="Calcular", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcUreia)
    btn_calcular.place(x=20,y=90)
    # Resultado dos cálculos
    lbl_title_resultado = Label(boxBtn,text="Total de emissão do carbono da uréia",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=10)
    lbl_resultado_ureia = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado_ureia.place(x=350,y=40)
    lbl_metrica_ureia = Label(boxBtn,
        font=("Nunito 10 bold"),fg=textBlue,bg="white",justify=LEFT)
    lbl_metrica_ureia.place(x=350,y=70)
    
    # =====================================================================================================
    # Calculo de emissão do calcário
    # Formulario de calculo
    lbl_calcario = Label(boxBtn2,text="Calculo com Calcário",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_calcario.place(x=20,y=10)
    lbl_calcario = Label(boxBtn2,text="Digite a quantidade de quilos de calcário",font=("Nunito 9"),fg=secundaria,bg="white")
    lbl_calcario.place(x=20,y=40)
    input_calcario = Entry(boxBtn2,width=48,highlightthickness=1,relief=FLAT)
    input_calcario.place(x=20,y=60)
    input_calcario.config(highlightbackground=principal, highlightcolor=principal)

    lbl_dolomito = Label(boxBtn2,text="Digite a quantidade de quilos de dolomito",font=("Nunito 9"),fg=secundaria,bg="white")
    lbl_dolomito.place(x=20,y=90)
    input_dolomito = Entry(boxBtn2,width=48,highlightthickness=1,relief=FLAT)
    input_dolomito.place(x=20,y=110)
    input_dolomito.config(highlightbackground=principal, highlightcolor=principal)

    btn_calcular = Button(boxBtn2,width=22, height=1, text="Calcular", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calCalcario)
    btn_calcular.place(x=20,y=140)
    # Resultado dos cálculos
    lbl_title_resultado = Label(boxBtn2,text="Total de emissão do carbono do calcário",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=10)
    lbl_resultado_calcario = Label(boxBtn2,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado_calcario.place(x=350,y=40)
    lbl_metrica_calcario = Label(boxBtn2,
        font=("Nunito 10 bold"),fg=textBlue,bg="white",justify=LEFT)
    lbl_metrica_calcario.place(x=350,y=80)

    # Texto de footer
    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=350,y=570)