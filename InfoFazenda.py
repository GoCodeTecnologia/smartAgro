from tkinter import*
from tkinter import Tk,font, ttk
from tkinter import messagebox

from DcCommand import*

def infoFazenda():
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
    
        

    # ==========================================================================================================
    # Informações
    lbl_title = Label(container,text="Total de Emissão por Veiculos ",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=20)
    lbl_subtitle_veiculo = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_subtitle_veiculo.place(x=10,y=50)

    lbl_title = Label(container,text="Total de Emissão da Fazenda ",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=80)
    lbl_subtitle_fazenda = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_subtitle_fazenda.place(x=10,y=110)

    lbl_title = Label(container,text="Total de Emissão da Plantação ",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=140)
    lbl_subtitle_plantacao = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_subtitle_plantacao.place(x=10,y=170)

    lbl_title = Label(container,text="Árvores para compensar ",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=200)
    lbl_arv_compensa = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_arv_compensa.place(x=10,y=230)

    lbl_title = Label(container,text="Consumo Total de Kwh",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=290)
    lbl_total_kwh = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_total_kwh.place(x=10,y=320)

    lbl_title = Label(container,text="Consumo Total em R$",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=10,y=350)
    lbl_total_dinheiro = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_total_dinheiro.place(x=10,y=380)

    # ====== lado direito
    lbl_title = Label(container,text="Emissão por Diesel",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=20)
    lbl_emissao_diesel = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_diesel.place(x=350,y=50)

    lbl_title = Label(container,text="Emissão por Flex ",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=80)
    lbl_emissao_flex = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_flex.place(x=350,y=110)

    lbl_title = Label(container,text="Emissão por Gasolina",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=140)
    lbl_emissao_gasolina = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_gasolina.place(x=350,y=170)

    lbl_title = Label(container,text="Emissão por GNV",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=200)
    lbl_emissao_gnv = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_gnv.place(x=350,y=230)

    lbl_title = Label(container,text="Emissão por Calcário",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=290)
    lbl_emissao_calcario = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_calcario.place(x=350,y=320)

    lbl_title = Label(container,text="Emissão por Uréia",font=("Ivy 15 bold"),fg=principal)
    lbl_title.place(x=350,y=350)
    lbl_emissao_ureia = Label(container,font=("Ivy 12 bold"),fg=secundaria)
    lbl_emissao_ureia.place(x=350,y=380)
    # ==========================================================================================================
    # Executando as querys de SELECT
    with conn:
        # Emissão total veiculo
        cur_ems_veiculo = conn.cursor()
        query_total_emissao_veiculo = "SELECT SUM(total_emissao) FROM tb_emissao_veiculo;"
        cur_ems_veiculo.execute(query_total_emissao_veiculo)
        total_emissao_veiculo = cur_ems_veiculo.fetchall()
        lbl_subtitle_veiculo.config(text=total_emissao_veiculo)
        # Emissão total fazenda
        cur_ems_fazenda = conn.cursor()
        query_total_emissao_fazenda = "SELECT SUM(total_emissao) FROM tb_emissao_fazenda;"
        cur_ems_fazenda.execute(query_total_emissao_fazenda)
        total_emissao_fazenda = cur_ems_fazenda.fetchall()
        lbl_subtitle_fazenda.config(text=total_emissao_fazenda)
        # Emissão total plantacao
        cur_ems_plantacao = conn.cursor()
        query_total_emissao_plantacao = "SELECT SUM(total_emissao) FROM tb_emissao_plantacao;"
        cur_ems_plantacao.execute(query_total_emissao_plantacao)
        total_emissao_plantacao = cur_ems_plantacao.fetchall()
        lbl_subtitle_plantacao.config(text=total_emissao_plantacao)
        # Total arvores compensar
        cur_total_compensa = conn.cursor()
        query_total_compensa = "SELECT SUM(total_compensa) FROM tb_emissao_veiculo;"
        cur_total_compensa.execute(query_total_compensa)
        total_compensa = cur_total_compensa.fetchall()
        lbl_arv_compensa.config(text=total_compensa)
        # Total consumo kwh
        cur_consumo_khw = conn.cursor()
        query_consumo_khw = "SELECT SUM(tipo_consumo) FROM tb_emissao_fazenda;"
        cur_consumo_khw.execute(query_consumo_khw)
        consumo_khw = cur_consumo_khw.fetchall()
        lbl_total_kwh.config(text=consumo_khw)
        # Total consumo dinheiro
        cur_consumo_dinheiro = conn.cursor()
        query_consumo_dinheiro = "SELECT SUM(tipo_consumo) FROM tb_emissao_fazenda WHERE tipo_consumo = 'Dinheiro';"
        cur_consumo_dinheiro.execute(query_consumo_dinheiro)
        consumo_dinheiro = cur_consumo_dinheiro.fetchall()
        lbl_total_dinheiro.config(text=consumo_dinheiro)
        # Total consumo diesel
        cur_consumo_diesel = conn.cursor()
        query_consumo_diesel = "SELECT SUM(combustivel) FROM tb_emissao_veiculo WHERE combustivel = 'Diesel';"
        cur_consumo_diesel.execute(query_consumo_diesel)
        consumo_diesel = cur_consumo_diesel.fetchall()
        lbl_emissao_diesel.config(text=consumo_diesel)
        # Total consumo flex
        cur_consumo_flex = conn.cursor()
        query_consumo_flex = "SELECT SUM(combustivel) FROM tb_emissao_veiculo WHERE combustivel = 'Flex';"
        cur_consumo_flex.execute(query_consumo_flex)
        consumo_flex = cur_consumo_flex.fetchall()
        lbl_emissao_flex.config(text=consumo_flex)
        # Total consumo flex
        cur_consumo_gasolina = conn.cursor()
        query_consumo_gasolina = "SELECT SUM(combustivel) FROM tb_emissao_veiculo WHERE combustivel = 'Gasolina';"
        cur_consumo_gasolina.execute(query_consumo_gasolina)
        consumo_gasolina = cur_consumo_gasolina.fetchall()
        lbl_emissao_gasolina.config(text=consumo_gasolina)
        # Total consumo flex
        cur_consumo_gnv = conn.cursor()
        query_consumo_gnv = "SELECT SUM(combustivel) FROM tb_emissao_veiculo WHERE combustivel = 'Gnv';"
        cur_consumo_gnv.execute(query_consumo_gnv)
        consumo_gnv = cur_consumo_gnv.fetchall()
        lbl_emissao_gnv.config(text=consumo_gnv)
        # Total consumo calcario
        cur_consumo_calcario = conn.cursor()
        query_consumo_calcario = "SELECT SUM(tipo_fertilizante) FROM tb_emissao_plantacao WHERE tipo_fertilizante = 'Calcário';"
        cur_consumo_calcario.execute(query_consumo_calcario)
        consumo_calcario = cur_consumo_calcario.fetchall()
        lbl_emissao_calcario.config(text=consumo_calcario)
        # Total consumo ureia
        cur_consumo_ureia = conn.cursor()
        query_consumo_ureia = "SELECT SUM(tipo_fertilizante) FROM tb_emissao_plantacao WHERE tipo_fertilizante = 'Uréia';"
        cur_consumo_ureia.execute(query_consumo_ureia)
        consumo_ureia = cur_consumo_ureia.fetchall()
        lbl_emissao_ureia.config(text=consumo_ureia)

    lbl_credits = Label(janela,text="GoCode Tecnologia, 2022",fg=secundaria,bg="white")
    lbl_credits.place(x=400,y=570)