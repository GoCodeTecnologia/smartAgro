from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

def calcFazenda():
    janela = Toplevel()
    janela.title("SmartAgro - Emissão CO² Fazenda")
    # janela.iconbitmap('assets/icon.ico')

    def calcEmissaoFazenda():
        try:
            tipo = input_tipo_calculo.get()
            mes = int(input_qtd_mes.get())
            valor = float(input_qtd_valor.get())

            if mes <0:
                messagebox.showerror("Erro","Insira uma quantidade válida")
            
            co2Kwh   = 0.1355
            co2Reais = co2Kwh / 0.347

            if (tipo == "Dinheiro"):
                value = valor
                valueTratado = value
                if (valueTratado < 100):
                    result = (valueTratado * co2Reais)
                    resultadoEnergia = ((valueTratado * co2Reais) * mes)
                else:
                    result = (valueTratado * co2Reais)
                    resultadoEnergia = (((valueTratado * co2Reais) * mes) / 100)
                lbl_valor.config(text="R$ {} reais".format(valor))
                
            elif (tipo == "Kwh"):
                value = valor
                result = (value * co2Kwh)
                resultadoEnergia = ((value * co2Kwh) * mes)
                lbl_valor.config(text="{} kws".format(valor))

            lbl_resultado_carbono.config(text="Emissão em Kg de CO2e: {}".format(round(resultadoEnergia, 2)))
            lbl_mes.config(text="{} mes(es)".format(mes))
            lbl_tipo.config(text="Tipo de cálculo escolhido: {}".format(tipo))

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

    lbl_title_parameter = Label(container,text="Calcular emissão de CO² - Fazenda",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=840,height=420,bg="white")
    boxBtn.place(x=20,y=50)

    lstTipo = ["Dinheiro","Kwh"]
    # Formulario de calculo
    lbl_tipo_calculo = Label(boxBtn,text="Informe o tipo do cálculo",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_tipo_calculo.place(x=20,y=10)
    input_tipo_calculo = ttk.Combobox(boxBtn, width=45, values=lstTipo, state="readonly")
    input_tipo_calculo.place(x=20,y=40)

    lbl_qtd_valor = Label(boxBtn,text="Informe o valor",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_qtd_valor.place(x=20,y=90)
    input_qtd_valor = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_qtd_valor.place(x=20,y=120)
    input_qtd_valor.config(highlightbackground=principal, highlightcolor=principal)

    lbl_qtd_mes = Label(boxBtn,text="Informe a quantidade de meses",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_qtd_mes.place(x=20,y=170)
    input_qtd_mes = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_qtd_mes.place(x=20,y=220)
    input_qtd_mes.config(highlightbackground=principal, highlightcolor=principal)

    btn_calcular = Button(boxBtn,width=22, height=1, text="Calcular", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcEmissaoFazenda)
    btn_calcular.place(x=20,y=360)

    # Resultado dos cálculos
    lbl_title_resultado = Label(boxBtn,text="Total de emissão do carbono",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=10)
    lbl_resultado_carbono = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado_carbono.place(x=350,y=40)

    lbl_title_resultado = Label(boxBtn,text="Informações",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=130)

    lbl_valor = Label(boxBtn,
        font=("Nunito 15 bold"),fg=secundaria,bg="white")
    lbl_valor.place(x=350,y=160)

    lbl_mes = Label(boxBtn,
        font=("Nunito 15 bold"),fg=secundaria,bg="white")
    lbl_mes.place(x=350,y=190)

    lbl_tipo = Label(boxBtn,
        font=("Nunito 15 bold"),fg=secundaria,bg="white")
    lbl_tipo.place(x=350,y=220)

    # Texto de footer
    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=350,y=570)