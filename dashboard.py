from tkinter import*
from tkinter import Tk, StringVar, ttk

# Tela Area
def dashboardScreen():
    newWindow = Toplevel()
    global tree
    largura = 800
    altura = 410
    altura_screen = newWindow.winfo_screenheight()
    largura_screen = newWindow.winfo_screenwidth()

    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2

    newWindow.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
    newWindow.resizable(0,0)

    # Criando os frames
    frame_cima = Frame(newWindow, width=800, height=50, bg="green", relief=FLAT)
    frame_cima.grid(row=0,column=0)

    frame_meio = Frame(newWindow, width=800, height=120, bg="white", relief=FLAT)
    frame_meio.grid(row=1,column=0)

    frame_baixo = Frame(newWindow, width=800, height=230, bg="white",relief=FLAT)
    frame_baixo.grid(row=2,column=0)

    # Logo parte superior da tela
    logo_app = Label(frame_cima, text='Cadastro de Áreas', 
        width=900, relief=FLAT, anchor=NW, font=("Verdana 15 bold"),bg="green",fg="white")
    logo_app.place(x=5,y=10)

    # Elementos e inputs do lado esquerdo
    l_nome = Label(frame_meio,text="Nome da área *", height=1, anchor=NW, font=("Ivy 10 bold"), bg="white", fg="green")
    l_nome.place(x=10,y=20)

    inp_area = Entry(frame_meio, width=30, justify='left', relief=SOLID)
    inp_area.place(x=150,y=20)

    l_tipo = Label(frame_meio,text="Metragem *", height=1, anchor=NW, font=("Ivy 10 bold"), bg="white", fg="green")
    l_tipo.place(x=10,y=50)

    inp_metragem = Entry(frame_meio, width=30, justify='left', relief=SOLID)
    inp_metragem.place(x=150,y=50)

    # Botões do lado direito
    btn_cad = Button(frame_meio, width=12, text="Cadastrar".upper(), anchor=CENTER,
        font=("Ivy 8 bold"), fg="white", bg="green", relief=FLAT)
    btn_cad.place(x=10,y=80)

    btn_edita = Button(frame_meio, width=12, text="Editar".upper(), anchor=CENTER,
        font=("Ivy 8 bold"), fg="white", bg="green", relief=FLAT)
    btn_edita.place(x=350,y=20)

    btn_exclui = Button(frame_meio, width=12, text="Excluir".upper(), anchor=CENTER,
        font=("Ivy 8 bold"), fg="white", bg="green", relief=FLAT)
    btn_exclui.place(x=350,y=50)

    btn_limpar = Button(frame_meio, width=12, text="Limpar".upper(), anchor=CENTER,
        font=("Ivy 8 bold"), fg="white", bg="green", relief=FLAT)
    btn_limpar.place(x=350,y=80)

    frame_area = Frame(frame_meio, width=150, height=85, bg="green")
    frame_area.place(x=460,y=20)

    lbl_titulo = Label(frame_area, text="Área Total* m²",
        height=1, font=("Ivy 10 bold"), bg="green", fg="white")
    lbl_titulo.place(x=30,y=5)

    lbl_soma = Label(frame_area, text="1500",
        height=1, font=("Ivy 15 bold"), bg="green", fg="white")
    lbl_soma.place(x=50,y=30)

    def mostrar():
        # Criando a tabela
        tabela_head = ['Cód.','Nome','Metragem m²']
        lista_itens = [(1,'Area 1',200),(2,'Area 2',300),(3,'Area 3',400)]

        tree = ttk.Treeview(frame_baixo, selectmode="extended",
                            columns=tabela_head, show="headings")
        hsb = ttk.Scrollbar(frame_baixo, orient="horizontal",command=tree.xview)
        tree.configure(xscrollcommand=hsb)
        tree.place(x=20,y=10,width=750,height=200)
        hsb.place(x=20,y=215,width=750)
        frame_baixo.grid_rowconfigure(0, weight=10)

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