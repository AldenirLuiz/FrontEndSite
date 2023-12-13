# Importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd 

# Importando pillow
from PIL import ImageTk, Image

# CORES
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#e5e5e5" # Grey
co3 = "#00a095" # Verde
co4 = "#403d3d" # Letra
co5 = "#003452" # Azul
co6 = "#ef5350"  # Vermelho
co7 = "#038cfc" # Azul
co8 = "263238"  # + Verde
co9 = "#e9edf5" # cinza claro


# Criando Janela

janela = Tk()
janela.title("LOGIN")
janela.geometry('850x620')
janela.config(background=co1)
janela.resizable(False, False)

#Criando um estilo
Style = Style(janela)
#new_theme = 'xpnative'
#print(Style.theme_names())
Style.theme_use("clam") # aqui chamos o tema para ser usado que no caso é o clam



# CRIANDO OS FRAMES DA JANELA
# FRAME LOGO
frame_logo = Frame(janela, width=850, height=52, bg=co7)
frame_logo.pack(expand=True, fill='both', padx=4, pady=2)   

ttk.Separator(janela, orient=HORIZONTAL).pack(expand=True, fill='x')    # Linha que separa 

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.pack(expand=True, fill='both', padx=4, pady=2)   

ttk.Separator(janela, orient=HORIZONTAL).pack(expand=True, fill='x')    # Linha que separa 

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.pack(expand=True, fill='both', padx=4, pady=2)   
#frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

# Cria frame Tabelas
frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.pack(side='left', expand=True, fill='both', padx=4, pady=2) 

# Trabalhando no frame Logo
app_lg = Image.open('siteicon.png')
app_lg = app_lg.resize((60,60))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, text = "Cadastro de Alunos", width=850, compound=LEFT,relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co7, fg=co1 ) 
app_logo.place(x=0, y=0)

#Criar funcao para cadastrar aluno
def alunos():
    print('Aluno')

# Funcao para adicionar Series e Turmas
def adicionar():
    # Criando frames para tabelas
    frame_tabela_serie = Frame(frame_tabela, width=300, height=200, bg=co0)
    frame_tabela_serie.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co9)
    frame_tabela_linha.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co0)
    frame_tabela_turma.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')

    l_nome = Label(frame_detalhes, text="Série", height=1, anchor=NW, font=('Ivy 12 bold'),bg=co1, fg=co4)
    l_nome.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')
    e_nome_serie = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_nome_serie.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')
    
    #botao_carregar = Button(frame_detalhes, image=app_img_salvar, text = "Salvar".upper(), width=62, height=26, compound=LEFT, overrelief=RIDGE, font=('Ivy 10 bold'), bg=co3, fg=co0 ) 
    botao_carregar = Button(frame_detalhes, anchor="center", text='Salvar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg="green", fg=co0)
    botao_carregar.pack(side='left', expand=False, fill='x', padx=4, pady=2, anchor='nw')   

    botao_carregar = Button(frame_detalhes, anchor="center", text='Atualizar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg="orange", fg=co0)
    botao_carregar.pack( side="left", expand=False, fill='x', padx=4, pady=2, anchor='nw')   

    botao_carregar = Button(frame_detalhes, anchor="center", text='Deletar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg="red", fg=co0)
    botao_carregar.pack(side="left", expand=False, fill='x', padx=4, pady=2, anchor='nw')   


#FUncao para salvar
def salvar():
    print('Salvar')

# CRiando uma funcao de controle de cadastro de estudante
def control(i):
    #cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a funcao alunos
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()

         # chamando a funcao adicionar
        adicionar()

        # chamando a funcao salvar
    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a funcao salvar
        salvar() 



# Criando os botoes (botao cadastro)
app_img_cadastro = Image.open('siteicon.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text = "Cadastro", width=100, height=26, compound=LEFT, overrelief=RIDGE, font=('Ivy 12'), bg=co1, fg=co0 ) 
app_cadastro.place(x=10, y=30) # Aqui direcionamos o botao para direita e esquerda, cima e para baixo , 

# Criando os botoes (botao Adicionar)
app_img_adicionar = Image.open('siteicon.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text = "Adicionar", width=100, height=26, compound=LEFT, overrelief=RIDGE, font=('Ivy 12'), bg=co1, fg=co0 ) 
app_adicionar.place(x=120, y=30) # Aqui direcionamos o botao para direita e esquerda, cima e para baixo , 

# Criando os botoes (botao Salvar)
app_img_salvar = Image.open('siteicon.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text = "Salvar", width=100, height=26, compound=LEFT, overrelief=RIDGE, font=('Ivy 12'), bg='#cc0000', fg=co0 ) 
app_salvar.place(x=230, y=30) # Aqui direcionamos o botao para direita e esquerda, cima e para baixo , 



janela.mainloop()