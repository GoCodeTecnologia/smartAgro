from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox
import math

from DcCommand import*

def cadDadosVeiculo():
    janela = Toplevel()
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

    def calcEmissaoVeiculo():
        try:
            tipo_veiculo = input_tipo_veiculo.get()
            distancia = round(float(input_distancia.get()),4)
            motor = input_tipo_motor.get()
            combustivel = input_tipo_combustivel.get()

            if distancia <0:
                    messagebox.showerror("Erro","Insira uma distância real")

            resultadoMotorComb = 0
            if (combustivel == "Diesel"):
                resultadoMotorComb = 0.2348
            else:
                resultadoMotorComb = motorComb[combustivel][motor]
            resultado = round((distancia * resultadoMotorComb) * 12, 2)

            resultadoFinal = round(((resultado) / 1000), 2)
            if (math.isnan(resultadoFinal) == True):
                resultadoFinal = 0
            resultadoArvores = round(math.ceil((resultadoFinal*1000)/190*1.2), 0)
            resultadoReais = resultadoArvores * 15
            resultadoReais = round(resultadoReais, 2)

            lista_inserir = [tipo_veiculo, distancia, motor, combustivel, resultadoReais, resultadoArvores]

            for i in lista_inserir:
                if i=='':
                    messagebox.showerror("Erro","Dados vazios")
                    return

            inserir_dados_veiculo(lista_inserir)
            mostrar()             
        except:
            messagebox.showerror("Erro","Dados inválidos ou não informados")

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

    lbl_title_parameter = Label(container,text="Cadastro de Dados dos Veículos",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=940,height=420,bg="white")
    boxBtn.place(x=20,y=50)

    # ==========================================================================================================
    # Formulário e Inputs
    lstTipo = ["Carro","Caminhão","Trator","Pulverizador","Colhedor de Cana"]
    lbl_tipo_veiculo = Label(boxBtn,text="Tipo Veiculo",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_tipo_veiculo.place(x=20,y=10)
    input_tipo_veiculo = ttk.Combobox(boxBtn, width=25, values=lstTipo, state="readonly")
    input_tipo_veiculo.place(x=20,y=40)

    lstTipo = ["Dinheiro","Kwh"]
    lbl_dstancia = Label(boxBtn,text="Distancia",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_dstancia.place(x=250,y=10)
    input_distancia =Entry(boxBtn,width=25,highlightthickness=1,relief=FLAT)
    input_distancia.place(x=250,y=40)
    input_distancia.config(highlightbackground=principal, highlightcolor=principal)

    lbl_tipo_motor = Label(boxBtn,text="Motor",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_tipo_motor.place(x=450,y=10)
    input_tipo_motor = ttk.Combobox(boxBtn, width=25, values=lstMotor, state="readonly")
    input_tipo_motor.place(x=450,y=40)

    lbl_tipo_combustivel = Label(boxBtn,text="Combustível",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_tipo_combustivel.place(x=650,y=10)
    lstCombustivel = ["Diesel","Flex","Gasolina","GNV"]
    input_tipo_combustivel = ttk.Combobox(boxBtn, width=25, values=lstCombustivel, state="readonly")
    input_tipo_combustivel.place(x=650,y=40)

    lbl_resultado_carbono = Label(boxBtn,font=("Nunito 10 bold"),fg=textBlue,bg="white")
    lbl_resultado_carbono.place(x=20,y=70)

    # ==========================================================================================================
    # Tabela e botão cadastrar
    def mostrar():
        # Criando a tabela
        tabela_head = ['Cód.','Tipo Veiculo','Distancia Percorrida','Tipo do Motor','Combustível','Emissão CO²','Total para Compensar']
        lista_itens = ver_tabela_veiculo()

        tree = ttk.Treeview(boxBtn, selectmode="extended",
                                columns=tabela_head, show="headings")
        hsb = ttk.Scrollbar(boxBtn, orient="horizontal",command=tree.xview)
        tree.configure(xscrollcommand=hsb)
        tree.place(x=20,y=100,width=900,height=200)
        hsb.place(x=20,y=305,width=900)
        boxBtn.grid_rowconfigure(0, weight=10)

        hd = ["nw","nw","nw"]
        h = [10,80,80]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=NW)
            tree.column(col, width=h[n], anchor=hd[n])
            n+1

        for item in lista_itens:
            tree.insert('', 'end', values=item)
    mostrar()

    btn_calcular = Button(boxBtn,width=22, height=1, text="Cadastrar Dados", relief='flat',
            bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcEmissaoVeiculo)
    btn_calcular.place(x=20,y=360)

    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=400,y=570)