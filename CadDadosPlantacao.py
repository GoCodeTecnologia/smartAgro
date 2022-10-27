from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

from DcCommand import*

def cadDadosPlantacao():
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

    def calcEmissaoFazenda():
        try:
            nome = input_nm_local.get().strip()
            tipo = input_tipo_consumo.get()
            mes = int(input_qtd_mes.get())
            valor = float(input_valor_consumo.get())

            if mes <0 or valor <0 or nome == "":
                messagebox.showerror("Erro","Insira uma quantidade válida")
                lbl_resultado_carbono.config(text="Dados Incorretos")
                return
            elif mes >0 or valor >0:
                
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
                    total_emissao = round(resultadoEnergia,2)
                        
                elif (tipo == "Kwh"):
                    value = valor
                    result = (value * co2Kwh)
                    resultadoEnergia = ((value * co2Kwh) * mes)
                    total_emissao = round(resultadoEnergia, 2)
                    
            lista_inserir = [nome, tipo, mes, valor, total_emissao]

            for i in lista_inserir:
                if i=='':
                    messagebox.showerror("Erro","Dados vazios")
                    return

            inserir_dados_fazenda(lista_inserir)
            mostrar()
        except:
            messagebox.showerror("Erro","Dados inválidos ou não informados")

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

    lbl_title_parameter = Label(container,text="Cadastro de Dados da Plantação",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=10)
    boxBtn = Frame(container,width=940,height=420,bg="white")
    boxBtn.place(x=20,y=50)

    # ==========================================================================================================
    # Formulário e Inputs
    lbl_nm_local = Label(boxBtn,text="Nome do Local",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_nm_local.place(x=20,y=10)
    input_nm_local = Entry(boxBtn,width=30,highlightthickness=1,relief=FLAT)
    input_nm_local.place(x=20,y=40)
    input_nm_local.config(highlightbackground=principal, highlightcolor=principal)

    lstTipo = ["Dinheiro","Kwh"]
    lbl_tipo_consumo = Label(boxBtn,text="Escolha o tipo de consumo",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_tipo_consumo.place(x=250,y=10)
    input_tipo_consumo = ttk.Combobox(boxBtn, width=25, values=lstTipo, state="readonly")
    input_tipo_consumo.place(x=250,y=40)

    lbl_valor_consumo = Label(boxBtn,text="Valor (Kwh ou R$)",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_valor_consumo.place(x=450,y=10)
    input_valor_consumo = Entry(boxBtn,width=30,highlightthickness=1,relief=FLAT)
    input_valor_consumo.place(x=450,y=40)
    input_valor_consumo.config(highlightbackground=principal, highlightcolor=principal)

    lbl_qtd_mes = Label(boxBtn,text="Quantidade de meses",font=("Nunito 10 bold"),fg=principal,bg="white")
    lbl_qtd_mes.place(x=650,y=10)
    input_qtd_mes = Entry(boxBtn,width=30,highlightthickness=1,relief=FLAT)
    input_qtd_mes.place(x=650,y=40)
    input_qtd_mes.config(highlightbackground=principal, highlightcolor=principal)

    lbl_resultado_carbono = Label(boxBtn,font=("Nunito 10 bold"),fg=textBlue,bg="white")
    lbl_resultado_carbono.place(x=20,y=70)

    # ==========================================================================================================
    # Tabela e botão cadastrar
    def mostrar():
        # Criando a tabela
        tabela_head = ['Cód.','Nome Local','Tipo (kwh/R$)','Total (kwh/R$)','Meses','Emissão CO²']
        lista_itens = ver_tabela_fazenda()

        tree = ttk.Treeview(boxBtn, selectmode="extended",
                                columns=tabela_head, show="headings")
        hsb = ttk.Scrollbar(boxBtn, orient="horizontal",command=tree.xview)
        tree.configure(xscrollcommand=hsb)
        tree.place(x=20,y=100,width=900,height=200)
        hsb.place(x=20,y=305,width=900)
        boxBtn.grid_rowconfigure(0, weight=10)

        hd = ["nw","nw","nw"]
        h = [20,100,100]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=NW)
            tree.column(col, width=h[n], anchor=hd[n])
            n+1

        for item in lista_itens:
            tree.insert('', 'end', values=item)
    mostrar()

    btn_calcular = Button(boxBtn,width=22, height=1, text="Cadastrar Dados", relief='flat',
            bg=secundaria, fg='white',font=("Nunito 15 bold"),command=calcEmissaoFazenda)
    btn_calcular.place(x=20,y=360)

    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=400,y=570)