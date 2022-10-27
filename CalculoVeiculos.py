from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox
import math

def calcVeiculo():
    janela = Toplevel()
    janela.title("SmartAgro - Emissão CO² Veiculo")
    # janela.iconbitmap('assets/icon.ico')

    def calcEmissaoVeiculo():
        try:
            distancia = round(float(input_distancia.get()),4)
            motor = input_tipo_motor.get()
            combustivel = input_tipo_combustivel.get()

            if distancia <0:
                messagebox.showerror("Erro","Insira uma distância real")

            lbl_km.config(text="Distância percorrida: {} Km's".format(distancia))
            lbl_motor.config(text="Tipo do motor: {}".format(motor))
            lbl_combus.config(text="Combustível selecionado: {}".format(combustivel))

            resultadoMotorComb = 0
            if (combustivel == "Diesel"):
                resultadoMotorComb = 0.2348
            else:
                resultadoMotorComb = motorComb[combustivel][motor]
            resultado = round((distancia * resultadoMotorComb) * 12, 2)
            resultadoParcial(resultado)
        except:
            messagebox.showerror("Erro","Dados inválidos ou não informados")
            janela.destroy()
            
    def resultadoParcial(valor):
            resultadoFinal = round(((valor) / 1000), 2)
            if (math.isnan(resultadoFinal) == True):
                resultadoFinal = 0
            resultadoArvores = round(math.ceil((resultadoFinal*1000)/190*1.2), 0)
            resultadoReais = resultadoArvores * 15
            resultadoReais = round(resultadoReais, 2)

            if resultadoReais > 1000:
                resultadoTon = resultadoReais / 100
                lbl_resultado_carbono.config(text="{} Toneladas".format(resultadoTon))
            elif resultadoReais <= 1000:
                lbl_resultado_carbono.config(text="{} Kg's".format(resultadoReais))
                
            input_tipo_combustivel.delete(0,'end')
            input_tipo_motor.delete(0,'end')
            input_distancia.delete(0,'end')
            lbl_resultado_arvores.config(text=resultadoArvores)

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

    lbl_title_parameter = Label(container,text="Calcular emissão de CO² - Veículos",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=840,height=420,bg="white")
    boxBtn.place(x=20,y=50)

    # Dados do combo box
    lstMotor = [
        "1.0(8V)","1.0(12V)","1.0(16V)","1.3(8V)","1.4(8V)",
        "1.4(16V)","1.5(16V)","1.6(8V)","1.6(16V)","1.8(16V)",
        "2.0(16V)","2.3(16V)","2.4(16V)","2.5(16V)","3.5(24V)"]

    motorComb = {
        'Flex' : {
            '1.0(8V)'  : 0.0726,
            '1.0(12V)' : 0.0727,
            '1.0(16V)' : 0.0961,
            '1.3(8V)'  : 0.1070,
            '1.4(8V)'  : 0.1085,
            '1.4(16V)' : 0.0995,
            '1.5(16V)' : 0.1034,
            '1.6(8V)'  : 0.1108,
            '1.6(16V)' : 0.1168,
            '1.8(16V)' : 0.1185,
            '2.0(16V)' : 0.1270,
            '2.3(16V)' : 0.1554,
            '2.4(16V)' : 0.1554,
            '2.5(16V)' : 0.0822,
            '3.5(24V)' : 0.1513,
        },
        'Gasolina' : {
            '1.0(8V)'  : 0.1451,
            '1.0(12V)' : 0.1454,
            '1.0(16V)' : 0.1923,
            '1.3(8V)'  : 0.2141,
            '1.4(8V)'  : 0.2171,
            '1.4(16V)' : 0.1990,
            '1.5(16V)' : 0.2067,
            '1.6(8V)'  : 0.2217,
            '1.6(16V)' : 0.2336,
            '1.8(16V)' : 0.2371,
            '2.0(16V)' : 0.2541,
            '2.3(16V)' : 0.3108,
            '2.4(16V)' : 0.3108,
            '2.5(16V)' : 0.1644,
            '3.5(24V)' : 0.3025,
        },
        'GNV' : {
            '1.0(8V)'  : 0.1372,
            '1.0(12V)' : 0.1376,
            '1.0(16V)' : 0.1818,
            '1.3(8V)'  : 0.2024,
            '1.4(8V)'  : 0.2053,
            '1.4(16V)' : 0.1882,
            '1.5(16V)' : 0.1955,
            '1.6(8V)'  : 0.2096,
            '1.6(16V)' : 0.2209,
            '1.8(16V)' : 0.2242,
            '2.0(16V)' : 0.2403,
            '2.3(16V)' : 0.2939,
            '2.4(16V)' : 0.2939,
            '2.5(16V)' : 0.1555,
            '3.5(24V)' : 0.2861,
        }
    }

    # Formulario de calculo
    lbl_distancia = Label(boxBtn,text="Informe a distância percorrida",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_distancia.place(x=20,y=10)
    input_distancia = Entry(boxBtn,width=48,highlightthickness=1,relief=FLAT)
    input_distancia.place(x=20,y=40)
    input_distancia.config(highlightbackground=principal, highlightcolor=principal)

    lbl_tipo_motor = Label(boxBtn,text="Informe o tipo do motor",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_tipo_motor.place(x=20,y=90)
    input_tipo_motor = ttk.Combobox(boxBtn, width=45, values=lstMotor, state="readonly")
    input_tipo_motor.place(x=20,y=120)

    lbl_tipo_combustivel = Label(boxBtn,text="Informe o tipo do combustível",font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_tipo_combustivel.place(x=20,y=170)
    lstCombustivel = ["Diesel","Flex","Gasolina","GNV"]
    input_tipo_combustivel = ttk.Combobox(boxBtn, width=45, values=lstCombustivel, state="readonly")
    input_tipo_combustivel.place(x=20,y=200)

    btn_calcular = Button(boxBtn,width=22, height=1, text="Calcular", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcEmissaoVeiculo)
    btn_calcular.place(x=20,y=360)

    # Resultado dos cálculos
    lbl_title_resultado = Label(boxBtn,text="Total de emissão do carbono",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=10)
    lbl_resultado_carbono = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado_carbono.place(x=350,y=40)

    lbl_title_resultado = Label(boxBtn,text="Árvores necessárias para compensação de CO²",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=70)
    lbl_resultado_arvores = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_resultado_arvores.place(x=350,y=100)

    lbl_title_resultado = Label(boxBtn,text="Informações",
        font=("Nunito 15 bold"),fg=principal,bg="white")
    lbl_title_resultado.place(x=350,y=130)

    lbl_km = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_km.place(x=350,y=160)

    lbl_combus = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_combus.place(x=350,y=190)

    lbl_motor = Label(boxBtn,
        font=("Nunito 15 bold"),fg=textBlue,bg="white")
    lbl_motor.place(x=350,y=220)

    # Texto de footer
    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=350,y=570)