from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

def calcPlantacao():
    janela = Toplevel()
    janela.title("SmartAgro - Emissão CO² Plantação")
    # janela.iconbitmap('assets/icon.ico')

    def calcEmissaoPlantacao():
        try:
            area = float(input_area.get())
            sementes = float(input_qtd_sementes.get())
            if area <0:
                messagebox.showerror("Erro","Insira uma quantidade válida")
            elif sementes<0:
                messagebox.showerror("Erro","Insira uma quantidade válida")

            fatorSemente = 0.92
            resultadoSemente = (area * sementes * fatorSemente)

            lbl_resultado.config(text="Emissão em de CO2e: {} kg's".format(round(resultadoSemente, 3)))
            lbl_area.config(text="Área de plantio: {} metros".format(area))
            lbl_sementes.config(text="Quantidade média de sementes: {}".format(sementes))

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
    lbl_subtitle = Label(janela,text="Soluções Agrônomo Inteligente",fg=secundaria,bg="white")
    lbl_subtitle.place(x=10,y=55)

    # Corpo da aplicação
    container = Frame(janela,width=880,height=490)
    container.place(x=10,y=80)

    lbl_title_parameter = Label(container,text="Calcular emissão de CO² - Plantação",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=840,height=420,bg="white")
    boxBtn.place(x=20,y=50)

    lbl_area = Label(boxBtn,text="Informe a área de plantio",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_area.place(x=20,y=10)
    input_area = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_area.place(x=20,y=40)
    input_area.config(highlightbackground=principal, highlightcolor=principal)

    lbl_qtd_sementes = Label(boxBtn,text="Informe a quantidade média de sementes",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_qtd_sementes.place(x=20,y=70)
    input_qtd_sementes = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_qtd_sementes.place(x=20,y=100)
    input_qtd_sementes.config(highlightbackground=principal, highlightcolor=principal)

    btn_calcular = Button(boxBtn,width=22, height=1, text="Calcular", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcEmissaoPlantacao)
    btn_calcular.place(x=20,y=360)

    # Resultado dos cálculos
    lbl_title_resultado = Label(boxBtn,text="Total de emissão do carbono",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=10)
    lbl_resultado = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado.place(x=350,y=40)

    lbl_title_resultado = Label(boxBtn,text="Informações",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=130)

    lbl_area = Label(boxBtn,
        font=("Nunito 15 bold"),fg=secundaria,bg="white")
    lbl_area.place(x=350,y=160)

    lbl_sementes = Label(boxBtn,
        font=("Nunito 15 bold"),fg=secundaria,bg="white")
    lbl_sementes.place(x=350,y=190)

    # Texto de footer
    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=350,y=570)