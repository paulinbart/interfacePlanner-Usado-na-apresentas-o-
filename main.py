### IMPORTS ###
import tkinter.messagebox
from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

cor1 = '#A52A2A'
cor2 = '#FFFFFF'

### CONEXÃO COM O BANCO DE DADOS ###
def banco():
  global conexao, cursor
  conexao = sqlite3.connect('banco.db')
  cursor = conexao.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS 'pessoa' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, email TEXT, senha TEXT, telefone TEXT, nascimento TEXT)")

def Inicio():
  tela_inicio = tk.Tk()
  tela_inicio.title("Inicio")
  tela_inicio.geometry('582x358')

### IMAGENS IMPORTADAS ###
  telai = PhotoImage(file='imagens/telas/tela_inicio.png') 
  bt_log = PhotoImage(file='imagens/botões/img_btlogin.png')
  bt_cad = PhotoImage(file='imagens/botões/img_btcadastro.png')
  lab = Label(tela_inicio,image=telai)
  lab.pack()

### BOTÕES ###
  
  bt_cadastro=Button(tela_inicio,width=115, text="Cadastre-se",image=bt_cad, command=lambda:[tela_inicio.destroy(), Cadastro()])
  bt_cadastro.place(x=430,y=290)
  bt_login = Button(tela_inicio,width=115,text="Login",image=bt_log,command=lambda:[tela_inicio.destroy(),Login()])
  bt_login.place(x=270,y=290)
  tela_inicio.mainloop()

def Cadastro():
  tela_cadastro = tk.Tk()
  tela_cadastro.title("cadastro de usuário")
  tela_cadastro.config(background = cor1)
  tela_cadastro.geometry("590x360")

  telacad = PhotoImage(file='imagens/telas/img_telacadastro.png')
  cadlab = Label(tela_cadastro,image=telacad)
  cadlab.pack()
  
  nome = StringVar()
  email = StringVar()
  senha = StringVar()
  telefone = StringVar()
  nascimento = StringVar()
  
  
  txt_nome = Label(tela_cadastro, text="Nome: ", font=('courier', 7), bd=0, background=cor2)
  txt_nome.place(x= 235,y= 85)
  nome = Entry(tela_cadastro,textvariable=nome,width=15)
  nome.place(x= 235,y= 99)
  
  txt_email = Label(tela_cadastro,text="email:",font=('courier', 7),bd=0,background=cor2)
  txt_email.place(x=235,y=123)
  email = Entry(tela_cadastro,textvariable=email,width=15)
  email.place(x=235,y=137)
  
  txt_senha = Label(tela_cadastro,text="Senha:",font = ("courier",7),bd=0,background=cor2)
  txt_senha.place(x=235,y=161)
  senha = Entry(tela_cadastro,show='*',textvariable=senha,width=15)
  senha.place(x=235,y=175)
  
  txt_telefone = Label(tela_cadastro,text="Telefone:",font=("courier",7),bd=0,background=cor2)
  txt_telefone.place(x=235,y=199)
  telefone = Entry(tela_cadastro,textvariable=telefone,width=15)
  telefone.place(x=235,y=213)
  
  txt_nascimento = Label(tela_cadastro, text="Nascimento: ", font=('courier',7), bd=0, background=cor2)
  txt_nascimento.place(x=235,y= 237)
  nascimento = Entry(tela_cadastro,textvariable=nascimento,width=15)
  nascimento.place(x=235,y= 251)

  def cadastrar():
  # se houver campos em branco, exibe mensagem de erro
    if  nome.get() == "" or email.get() == ""  or senha.get() == "" or telefone.get() == "" or nascimento.get() == "":
      tkinter.messagebox.showinfo(title="Erro",message="Nenhum campo pode ficar em branco!")
  # se não, faz o registro no banco de dados
    else:
      banco()# chamar função para conectar ao banco
      cursor.execute("INSERT INTO 'pessoa' (nome, email, senha, telefone, nascimento) VALUES(?, ?, ?, ?, ?)", (str(nome.get()), str(email.get()), str(senha.get()), str(telefone.get()), str(nascimento.get())))
      conexao.commit() # validar inserção
      nome.delete(0,"end") # limpar campo nome
      email.delete(0,"end") # limpar campo e-mail
      senha.delete(0,"end") # limpar campo senha
      telefone.delete(0,"end") # limpar campo telefone
      nascimento.delete(0,"end") # limpar campo nascimento
      cursor.close() # encerrar cursor
      conexao.close() # encerrar conexão
      tkinter.messagebox.showinfo(title="Sucesso!", message="Usuário cadastrado!") # mensagem que inserção ocorreu
  
  bt_cadastrar = Button(tela_cadastro,width=10,height=2, text="Cadastrar", command=cadastrar)
  bt_cadastrar.place(x=240,y=280)
  
  bt_continuar = Button(tela_cadastro,width=10,text="Continuar",command = lambda:[tela_cadastro.destroy(),Agendamento()])
  bt_continuar.place(x=430,y=150)

  bt_voltar = Button(tela_cadastro,width=10,text="Voltar",command=lambda:[tela_cadastro.destroy(),Inicio()])
  bt_voltar.place(x=50,y=150)
  tela_cadastro.mainloop()
def Login():
  tela_login = tk.Tk()
  tela_login.title("Login")
  tela_login.config(background = cor1)
  tela_login.geometry("589x361")

  telalog = PhotoImage(file='imagens/telas/img_telalogin.png')
  labl = Label(tela_login,image=telalog)
  labl.pack()
  email = StringVar()
  senha = StringVar()
  
  
  
  txt_loginemail = Label(tela_login,text="Email:",font=("courier",7),bd=0,background=cor2)
  txt_loginemail.place(x=362,y=160)
  email = Entry(tela_login,textvariable=email,width=15)
  email.place(x=362,y=179)
  
  txt_loginsenha = Label(tela_login, text = "Senha:", font=("courier",7),bd=0,background=cor2)
  txt_loginsenha.place(x=362,y=205)
  senha = Entry(tela_login,textvariable=senha,show='*',width=15)
  senha.place(x=362,y=224)
  
  bt_continuar = Button(tela_login,width=10,text="Continuar",command=lambda:[tela_login.destroy(),Agendamento()])
  bt_continuar.place(x=375,y=255)

  bt_voltar = Button(tela_login,width=10,height=2,text="Voltar",command=lambda:[tela_login.destroy(),Inicio()])
  bt_voltar.place(x=375,y=300)
  tela_login.mainloop()

def Agendamento():
  tela_agenda = tk.Tk()
  tela_agenda.title("Agendamento")
  tela_agenda.config(background=cor1)
  tela_agenda.geometry("600x362")

  telagnd = PhotoImage(file='imagens/telas/img_telaagendamento.png')
  lab_agnd = Label(tela_agenda,image=telagnd)
  lab_agnd.pack()
  btsalv = PhotoImage(file='imagens/botões/botão_salvar.png')
  btvolt = PhotoImage(file='imagens/botões/botão_voltar.png')
  
  nomeagendamento = StringVar()
  descricao = StringVar()
  data = StringVar()
  
  nomeagendamento = Entry(tela_agenda,textvariable=nomeagendamento,width=25)
  nomeagendamento.place(x=15,y=235)

  descricao = Entry(tela_agenda,textvariable=descricao,width=25)
  descricao.place(x=15,y=155)

  data = DateEntry(tela_agenda, textvariable=data,width=25,height=3, year=2022)
  data.place(x=15,y=77)
  
  cal = Calendar(tela_agenda, selectmode='none')
  cal.place(x=300,y=50)
  ttk.Label(tela_agenda, text="deixe o mouse sobre o evento.").place(x=335,y=220)
  def Salvar():

    date = data.get_date()
    nome = nomeagendamento.get()
    descrição = descricao.get()
    
    cal.calevent_create(date, nome, 'message')
    cal.calevent_create(date, descrição, 'reminder')
    #cria um evento dentro do calendário, sendo o 'message' o nome, e o 'reminder' a descrição

    cal.tag_config('reminder', background='red', foreground='yellow')

  bt_salvaragend = Button(tela_agenda,width=150,text="Salvar",image = btsalv,command=lambda:Salvar())
  bt_salvaragend.place(x=20,y=315)

  bt_voltar = Button(tela_agenda,width=150,text="Voltar",image=btvolt,command=lambda:[tela_agenda.destroy(),Inicio()])
  bt_voltar.place(x=350,y=315)
  tela_agenda.mainloop()
Inicio()