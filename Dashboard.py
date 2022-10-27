from tkinter import*
from tkinter import Tk,font

import sqlite3 as lite
conn = lite.connect('D:\SmartAgro\database\dados.db')

from CalculoFazenda import*
from CalculoPlantacao import*
from CalculoVeiculos import*
from CalculoFertilizante import*

from CadDadosFazenda import*

def dashboard():
    janela = Tk()
    janela.title("SmartAgro - Dashboard")
    # janela.iconbitmap('assets/icon.ico')

    # Cores da aplicação
    principal = "#003d59";
    secundaria = "#01826e";
    textRed = "#eb0202";
    textBlue = "#002ef4";
    bgClean = "#d4dde1";

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

    # Caixas com os resultados
    box_menu1 = Frame(container,width=200,height=100,bg=principal)
    box_menu1.place(x=20,y=20)
    lbl_title_bx1 = Label(box_menu1,text="Total de Emissões CO²",font=("Nunito 12 bold"),fg="white",bg=principal)
    lbl_title_bx1.place(x=10,y=10)
    lbl_result_bx1 = Label(box_menu1,font=("Nunito 20 bold"),fg="white",bg=principal)
    lbl_result_bx1.place(x=10,y=50)

    box_menu2 = Frame(container,width=200,height=100,bg=principal)
    box_menu2.place(x=230,y=20)
    lbl_title_bx2 = Label(box_menu2,text="Total para Compensar",font=("Nunito 12 bold"),fg="white",bg=principal)
    lbl_title_bx2.place(x=10,y=10)
    lbl_result_bx2 = Label(box_menu2,font=("Nunito 20 bold"),fg="white",bg=principal)
    lbl_result_bx2.place(x=10,y=50)

    box_menu3 = Frame(container,width=200,height=100,bg=principal)
    box_menu3.place(x=440,y=20)
    lbl_title_bx3 = Label(box_menu3,text="Emissão Total dos Veículos",font=("Nunito 10 bold"),fg="white",bg=principal)
    lbl_title_bx3.place(x=10,y=10)
    lbl_result_bx3 = Label(box_menu3,font=("Nunito 20 bold"),fg="white",bg=principal)
    lbl_result_bx3.place(x=10,y=50)

    box_menu4 = Frame(container,width=200,height=100,bg=principal)
    box_menu4.place(x=650,y=20)
    lbl_title_bx4 = Label(box_menu4,text="Status Minha Fazenda",font=("Nunito 12 bold"),fg="white",bg=principal)
    lbl_title_bx4.place(x=10,y=10)
    lbl_result_bx4 = Label(box_menu4,text="0",font=("Nunito 20 bold"),fg="white",bg=principal)
    lbl_result_bx4.place(x=10,y=50)

    lbl_title_parameter = Label(container,text="Realizar Cálculos",font=("Nunito 18 bold"),fg=principal)
    lbl_title_parameter.place(x=20,y=150)
    boxBtn = Frame(container,width=200,height=280,bg="white")
    boxBtn.place(x=20,y=190)
    boxBtn2 = Frame(container,width=620,height=280,bg="white")
    boxBtn2.place(x=230,y=190)

    with conn:
        cur = conn.cursor()
        cur_ems = conn.cursor()
        cur_ems_veiculo = conn.cursor()

        query_total_emissao = "SELECT SUM(total_emissao) FROM tb_emissao_veiculo;"
        query_total_compensa = "SELECT SUM(total_compensa) FROM tb_emissao_veiculo;"
        query_total_veiculo = "SELECT SUM(total_emissao) FROM tb_emissao_veiculo;"
        cur.execute(query_total_emissao)
        cur_ems.execute(query_total_compensa)
        cur_ems_veiculo.execute(query_total_veiculo)

        total_emissao = cur.fetchall()
        total_compensa = cur_ems.fetchall()
        total_veiculo = cur_ems_veiculo.fetchall()
        lbl_result_bx1.config(text=total_emissao)
        lbl_result_bx2.config(text=total_compensa)
        lbl_result_bx3.config(text=total_veiculo)

    btn_calcFazenda = Button(boxBtn,width=22, height=1, text="Emissão Energia Fazenda", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"),command=calcFazenda)
    btn_calcFazenda.place(x=5,y=10)

    btn_calFertilizante = Button(boxBtn,width=22, height=1, text="Emissão Fertilizante", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"),command=calcFertilizante)
    btn_calFertilizante.place(x=5,y=50)

    btn_calPlantacao = Button(boxBtn,width=22, height=1, text="Emissão Plantação", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"),command=calcPlantacao)
    btn_calPlantacao.place(x=5,y=90)

    btn_calVeiculo = Button(boxBtn,width=22, height=1, text="Emissão Veículo", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"),command=calcVeiculo)
    btn_calVeiculo.place(x=5,y=130)

    btn_calPlantacao = Button(boxBtn,width=22, height=1, text="Minha Fazenda", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 10 bold"))
    btn_calPlantacao.place(x=5,y=190)

    btn_calPlantacao = Button(boxBtn,width=22, height=1, text="Gráficos", relief='flat',
        bg=secundaria, fg='white',font=("Nunito 10 bold"))
    btn_calPlantacao.place(x=5,y=230)

    # ==================================================================================================
    btn_cadFazenda = Button(boxBtn2,width=22, height=3, text="Cadastrar Dados Fazenda", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"),command=cadDadosFazenda)
    btn_cadFazenda.place(x=10,y=10)

    btn_cadVeiculos = Button(boxBtn2,width=22, height=3, text="Cadastrar Dados Veículos", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"))
    btn_cadVeiculos.place(x=210,y=10)

    btn_cadPlantacao = Button(boxBtn2,width=22, height=3, text="Cadastrar Dados Plantação", relief='flat',
        bg=principal, fg='white',font=("Nunito 10 bold"))
    btn_cadPlantacao.place(x=10,y=90)





    # ==================================================================================================
    # Texto de footer
    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=350,y=570)