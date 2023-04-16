from tkinter import *
from tkinter import messagebox
import mysql.connector

######## FUNÇÕES DOS BOTÕES ########

# Conexão do MySQL no botão CREATE
def click_create():
	Nome = nome_resp.get()
	Idade = idade_resp.get()
	conexao = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "123456",
		database = "primeiro_programa_bd",
	)

	cursor = conexao.cursor()

	# VERIFICAÇÃO SE O NOME JÁ EXISTE #
	comando = f'SELECT (Idade) FROM cadastro WHERE Nome LIKE ("{Nome}") '
	cursor.execute(comando)
	resultado = cursor.fetchall()
	###################################
	
	if resultado != []:
		messagebox.showinfo("Mensagem", f"Já existe um cadastro no Banco de Dados com o nome {Nome}.")
		nome_resp.delete(0, END)
		idade_resp.delete(0, END)
	elif Idade == "" or Nome == "":
		messagebox.showinfo("Mensagem", "Por favor, preencha todos os campos.")
		nome_resp.delete(0, END)
		idade_resp.delete(0, END)
	else:
		comando = f'INSERT INTO cadastro (Nome, Idade) VALUES ("{Nome}", {Idade})'
		cursor.execute(comando)
		conexao.commit()

		# Limpar campos
		nome_resp.delete(0, END)
		idade_resp.delete(0, END)

		messagebox.showinfo("Mensagem", f"{Nome} foi inserido com sucesso no Banco de Dados.")

	cursor.close()
	conexao.close()

# Conexão do MySQL no botão READ
def click_read():
	Nome = ler_nome_resp.get()
	conexao = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "123456",
		database = "primeiro_programa_bd",
	)

	cursor = conexao.cursor()

	comando = f'SELECT (Idade) FROM cadastro WHERE Nome LIKE ("{Nome}") '
	cursor.execute(comando)
	resultado = cursor.fetchall()
	
	resposta = []
	for record in resultado:
		resposta.append(record)

	if Nome == "":
		imprime_idade['text'] = "Por favor, insira um nome para consulta.\n"
	elif resposta == []:
		imprime_idade['text'] = "O nome inserido não consta no Banco de Dados.\n"
	else:
		imprime_idade['text'] = f"Nome = {Nome}\n Idade = {resposta[0][0]}"
	
	# Limpar campos
	ler_nome_resp.delete(0, END)


	cursor.close()
	conexao.close()

# Conexão do MySQL no botão UPDATE
def click_update():
	Nome = ler_nome_update_resp.get()
	Idade = ler_idade_update_resp.get()
	conexao = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "123456",
		database = "primeiro_programa_bd",
	)

	cursor = conexao.cursor()

	# VERIFICAÇÃO SE O NOME EXISTE #
	comando = f'SELECT (Idade) FROM cadastro WHERE Nome LIKE ("{Nome}") '
	cursor.execute(comando)
	resultado = cursor.fetchall()
	###################################

	if Nome == "" or Idade == "":
		messagebox.showinfo("Mensagem", "Por favor, preencha todos os campos.")
		ler_nome_update_resp.delete(0, END)
		ler_idade_update_resp.delete(0, END)
	elif resultado == []:
		messagebox.showinfo("Mensagem", "O nome inserido não consta no Banco de Dados.")
		ler_nome_update_resp.delete(0, END)
		ler_idade_update_resp.delete(0, END)
	else:
		comando = f'UPDATE cadastro SET Idade = {Idade} WHERE Nome = "{Nome}" '
		cursor.execute(comando)
		conexao.commit()

		# Limpar campos
		ler_nome_update_resp.delete(0, END)
		ler_idade_update_resp.delete(0, END)

		messagebox.showinfo("Mensagem", f"A idade de {Nome} foi alterada para {Idade}.")

	cursor.close()
	conexao.close()

# Conexão do MySQL no botão DELETE
def click_delete():
	Nome = ler_nome_delete_resp.get()
	conexao = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "123456",
		database = "primeiro_programa_bd",
	)

	cursor = conexao.cursor()

	# VERIFICAÇÃO SE O NOME EXISTE #
	comando = f'SELECT (Idade) FROM cadastro WHERE Nome LIKE ("{Nome}")'
	cursor.execute(comando)
	resultado = cursor.fetchall()
	###################################

	if Nome == "":
		messagebox.showinfo("Mensagem", "Por favor, preencha o campo indicado.")
		ler_nome_delete_resp.delete(0, END)
	elif resultado == []:
		messagebox.showinfo("Mensagem", "O nome inserido não consta no Banco de Dados.")
		ler_nome_delete_resp.delete(0, END)
	else:
		comando1 = f'DELETE FROM cadastro WHERE Nome = "{Nome}"'
		comando2 = 'SET  @num := 0'
		comando3 = 'UPDATE cadastro SET id = @num:= (@num+1)'
		comando4 = 'ALTER TABLE cadastro AUTO_INCREMENT =1'
		cursor.execute(comando1)
		conexao.commit()
		cursor.execute(comando2)
		conexao.commit()
		cursor.execute(comando3)
		conexao.commit()
		cursor.execute(comando4)
		conexao.commit()

		# Limpar campos
		ler_nome_delete_resp.delete(0, END)

		messagebox.showinfo("Mensagem", f"{Nome} foi deletado com sucesso do Banco de Dados.")

	cursor.close()
	conexao.close()

######## JANELA E FUNCIONALIDADES ########

janela = Tk()
janela.title("CONTROLE DE CADASTROS")
janela.geometry("332x510")
janela.minsize(332, 510)
janela.maxsize(332, 510)
img = PhotoImage(file='C:\\Users\\rafae\\Documents\\RAFAEL\\ESTUDOS TI\\Estudos_programas\\Tkinter CRUD\\icone_cadastro.png')
janela.iconphoto(False, img)
janela.configure(background='#ADD8E6') 

titulo = Label(janela, text = "\n        CADASTRO DE PESSOAS        \n", bg = '#B0C4DE')
titulo.grid(row = 1, column = 2, columnspan = 2)

linha_separa_titulo = Label(janela, text = "__________________________________________________________________ ", bg = '#ADD8E6')
linha_separa_titulo.grid(row = 2, column = 1, columnspan = 4)

linha_separa_create = Label(janela, text = "  ", bg = '#ADD8E6')
linha_separa_create.grid(row = 5, column = 2)

linha_separa_read = Label(janela, text = "  ", bg = '#ADD8E6')
linha_separa_read.grid(row = 9, column = 2)

linha_abaixo_read = Label(janela, text = "  ", bg = '#ADD8E6')
linha_abaixo_read.grid(row = 11, column = 2, columnspan = 4)

linha_separa_update = Label(janela, text = "  ", bg = '#ADD8E6')
linha_separa_update.grid(row = 15, column = 2)

linha_separa_delete = Label(janela, text = "  ", bg = '#ADD8E6')
linha_separa_delete.grid(row = 19, column = 2)


# Nome dos campos CREATE
nome = Label(janela, text = "Nome: ", bg = '#ADD8E6')
nome.grid(row = 3, column = 2)

idade = Label(janela, text = "Idade: ", bg = '#ADD8E6')
idade.grid(row = 4, column = 2)

# Input dos campos CREATE
nome_resp = Entry(janela, width = 20)
nome_resp.grid (row = 3, column = 3)

idade_resp = Entry(janela, width = 20)
idade_resp.grid(row = 4, column = 3)

# Botão e linha separadora
botao_create = Button(janela, text = "CRIAR", command = click_create, bg = 'white', borderwidth = 4, width = 10, height = 1)
botao_create.grid(row = 6, column = 2, columnspan = 4)

linha_separa1 = Label(janela, text = "__________________________________________________________________", bg = '#ADD8E6')
linha_separa1.grid(row = 7, column = 1, columnspan = 4)



# Nome do campo READ
ler_nome = Label(janela, text = "Nome da pessoa a saber a idade: ", bg = '#ADD8E6')
ler_nome.grid(row = 8, column = 2)

# Input do campo READ  
ler_nome_resp = Entry(janela, width = 20)
ler_nome_resp.grid(row = 8, column = 3)

# Botão e linha separadora
botao_read = Button(janela, text = "LER", command = click_read, bg = 'white', borderwidth = 4, width = 10, height = 1)
botao_read.grid(row = 10, column = 2, columnspan = 4)

imprime_idade = Label(janela, text = "  \n  ", bg = '#ADD8E6')
imprime_idade.grid(row = 11, column = 2, columnspan = 2)

linha_separa1 = Label(janela, text = "__________________________________________________________________", bg = '#ADD8E6')
linha_separa1.grid(row = 12, column = 1, columnspan = 4)



# Nome dos campos UPDATE
ler_nome_update = Label(janela, text = "Nome da pessoa a alterar a idade: ", bg = '#ADD8E6')
ler_nome_update.grid(row = 13, column = 2)

ler_idade_update = Label(janela, text = "Qual a nova idade: ", bg = '#ADD8E6')
ler_idade_update.grid(row = 14, column = 2)

# Input dos campos UPDATE
ler_nome_update_resp = Entry(janela, width = 20)
ler_nome_update_resp.grid(row = 13, column = 3)

ler_idade_update_resp = Entry(janela, width = 20)
ler_idade_update_resp.grid(row = 14, column = 3)

# Botão e linha separadora
botao_update = Button(janela, text = "ATUALIZAR", command = click_update, bg = 'white', borderwidth = 4, width = 10, height = 1)
botao_update.grid(row = 16, column = 2, columnspan = 4)

linha_separa1 = Label(janela, text = "__________________________________________________________________", bg = '#ADD8E6')
linha_separa1.grid(row = 17, column = 1, columnspan = 4)


# Nome do campo DELETE
ler_nome_delete = Label(janela, text = "Qual nome deletar: ", bg = '#ADD8E6')
ler_nome_delete.grid(row = 18, column = 2)

# Input do campo DELETE
ler_nome_delete_resp = Entry(janela, width = 20)
ler_nome_delete_resp.grid(row = 18, column = 3)

# Botão e linha separadora
botao_delete = Button(janela, text = "DELETAR", command = click_delete, bg = 'white', borderwidth = 4, width = 10, height = 1)
botao_delete.grid(row = 20, column = 2, columnspan = 4)

linha_separa1 = Label(janela, text = "  ", bg = '#ADD8E6')
linha_separa1.grid(row = 21, column = 2)


janela.mainloop()