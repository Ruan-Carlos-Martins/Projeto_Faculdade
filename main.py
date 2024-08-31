from PyQt6 import  uic,QtWidgets
import mysql.connector
from datetime import datetime
from PyQt6.QtWidgets import QTableWidgetItem
import locale
from PyQt6.QtWidgets import QLineEdit







# conexão com bando de dados
conexao =  mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='230499', 
            database='faculdade'
)

# FUNÇÕES DE ACESSO AS TELAS DE CADASTRO

def entrar_tela_acesso_prof():
    primeira_tela.close()
    tela_acesso_professor.show()

def entrar_tela_acesso_aluno():
    primeira_tela.close()
    tela_acesso_aluno.show()   

def entrar_login_adm():
    primeira_tela.close()
    tela_acesso_adm.show()

def entrar_matricula_aluno():
    tela_adm_cadastro.close()
    tela_cadastro_alunos.show()


def entrar_cadastra_professor():
    try: 
        query3 = """
            SELECT nome_disciplina
            FROM disciplinas
            """
        cursor.execute(query3)

        lista_disciplinas = tela_cadastro_professores.comboBoxDisciplina
        resultados = cursor.fetchall()
        for resultado in resultados:
            lista_disciplinas.addItem(f"{resultado[0]}")

    except Exception as e:
         print('erro')
    # Adicione qualquer tratamento de erro adicional aqui

    finally:
        # Fechar o cursor e a conexão
        if 'cursor' in locals():
                cursor.close()
        if 'connection' in locals() and conexao.is_connected():
                conexao.close()        

    tela_adm_cadastro.close()
    tela_cadastro_professores.show()

def voltar_tela_adm_cadastro_atualiza():
    tela_atualiza_dados_alunos.close()
    tela_adm_cadastro.show()

def voltar_tela_adm_cadastro_atualiza_professores():
    tela_atualiza_dados_professores.close()
    tela_adm_cadastro.show()          

def voltar_tela_adm_cadastro_cad():
    tela_cadastro_alunos.close()
    tela_adm_cadastro.show()     

def voltar_tela_adm_cadastro_cad_professores():
    tela_cadastro_professores.close()
    tela_adm_cadastro.show()

def voltar_atualizado_prof_para_tela_principal():
    tela_cadastroProfessor_atualizado.close()
    primeira_tela.show()
    
def fechar_tela_atualizado_cadastro_prof():
    tela_cadastroProfessor_atualizado.close()

def fechar_tela_atualizado_cadastro_aluno():
    tela_cadastro_atualizado.close()

def voltar_tela_adm_cadastro():
    # Fechar todas as telas abertas
    telas_abertas = [tela_lista_alunos,tela_lista_professores]
    for tela in telas_abertas:
        tela.close()
    
    telas_com_campos = [tela_lista_alunos,tela_lista_professores]
    for tela in telas_com_campos:
        for campo in tela.findChildren(QLineEdit):
            campo.clear()

    tela_adm_cadastro.show()

def reiniciar_sistema():
    # Fechar todas as telas abertas
    telas_abertas = [tela_acesso_professor, tela_acesso_aluno, tela_acesso_adm, tela_cadastro_alunos, 
                     tela_cadastro_professores, tela_atualiza_dados_alunos, tela_atualiza_dados_professores,
                     tela_cadastroProfessor_atualizado, tela_cadastro_atualizado,tela_lista_professores,tela_lista_alunos,tela_dados_alunos,tela_dados_professor,tela_adm_cadastro,tela_aluno_matriculado]
    for tela in telas_abertas:
        tela.close()
        
        

    # Limpar campos de entrada
    telas_com_campos = [tela_acesso_professor, tela_acesso_aluno, tela_acesso_adm, tela_cadastro_alunos, 
                     tela_cadastro_professores, tela_atualiza_dados_alunos, tela_atualiza_dados_professores]
    for tela in telas_com_campos:
        for campo in tela.findChildren(QLineEdit):
            campo.clear()

   
    # Reiniciar variáveis ​​ou estados do sistema para o estado inicial
    # Aqui você pode adicionar qualquer operação adicional necessária para reiniciar o sistema.

    # Mostrar a primeira tela
    tela_acesso_adm.acesso_invalido_adm.clear()
    tela_acesso_aluno.acesso_invalido_aluno.clear()
    tela_acesso_professor.acesso_invalido_professor.clear()
    primeira_tela.show()

# Você pode chamar essa função sempre que desejar reinicializar o sistema do zero



 
        
def entrar_atualiza_aluno():
    tela_adm_cadastro.close()    
      
    # mostra a lista de nomes dos alunos matriculados
    try: 
        query3 = """
            SELECT Nome_Aluno
            FROM cadastro_alunos
            """
        cursor.execute(query3)

        lista_nomes = tela_atualiza_dados_alunos.comboBox_3
        resultados = cursor.fetchall()
        for resultado in resultados:
            lista_nomes.addItem(f"{resultado[0]}")

    except Exception as e:
     print('erro')
    # Adicione qualquer tratamento de erro adicional aqui

    finally:
        # Fechar o cursor e a conexão
        if 'cursor' in locals():
                cursor.close()
        if 'connection' in locals() and conexao.is_connected():
                conexao.close()        

    tela_atualiza_dados_alunos.show()


def entrar_atualiza_professor():
    tela_adm_cadastro.close()
    
    
    try: 
        query3 = """
            SELECT nome_professores
            FROM cadastro_professores
            """
        cursor.execute(query3)

        lista_nomes = tela_atualiza_dados_professores.comboBoxNome
        resultados = cursor.fetchall()
        for resultado in resultados:
            lista_nomes.addItem(f"{resultado[0]}")

    except Exception as e:
     print('erro')
    # Adicione qualquer tratamento de erro adicional aqui

    finally:
        # Fechar o cursor e a conexão
        if 'cursor' in locals():
                cursor.close()
        if 'connection' in locals() and conexao.is_connected():
                conexao.close()

    try: 
        query3 = """
            SELECT nome_disciplina
            FROM disciplinas
            """
        cursor.execute(query3)

        lista_disciplinas = tela_atualiza_dados_professores.comboBoxDisciplina
        resultados = cursor.fetchall()
        for resultado in resultados:
            lista_disciplinas.addItem(f"{resultado[0]}")

    except Exception as e:
         print('erro')
    # Adicione qualquer tratamento de erro adicional aqui

    finally:
        # Fechar o cursor e a conexão
        if 'cursor' in locals():
                cursor.close()
        if 'connection' in locals() and conexao.is_connected():
                conexao.close()   

    tela_atualiza_dados_professores.show()  


def acesso_adm_cadastro():    
    tela_acesso_adm.acesso_invalido_adm.setText("") # Limpar campo de mensagem de erro
    nome_usuario_adm = tela_acesso_adm.login_adm.text()
    senha_usuario_adm = tela_acesso_adm.senha_adm.text()

    try: 
        # Verificar se a conexão está aberta e reconectá-la se necessário
        if not conexao.is_connected():
            conexao.connect()

        cursor = conexao.cursor()  # Obter um novo cursor

        query = "SELECT senha FROM acesso_adm WHERE login = %s"
        cursor.execute(query, (nome_usuario_adm, ))
        result = cursor.fetchone()

        if result:  # Verificar se há um resultado retornado da consulta
            db_senha = result[0]

            if senha_usuario_adm == db_senha:
                tela_acesso_adm.close()
                tela_adm_cadastro.show()
                return  # Sair da função após a tela ser mostrada

        tela_acesso_adm.acesso_invalido_adm.setText('Dados incorretos!!')
    except mysql.connector.Error as err:
        print("Erro MySQL:", err)
        tela_acesso_adm.acesso_invalido_adm.setText('Erro ao acessar o banco de dados: ' + str(err))
    except Exception as e:
        print('Erro:', e)
        tela_acesso_adm.acesso_invalido_adm.setText('Erro desconhecido: ' + str(e))
    finally:
        # Fechar o cursor após o uso
        if 'cursor' in locals() and cursor:
            cursor.close()



# Função para adm matricular alunos 
def matricular_alunos():
    nome_aluno = tela_cadastro_alunos.lineEdit_31.text()
    data_nascimento = tela_cadastro_alunos.lineEdit_32.text()
    data = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    endereco = tela_cadastro_alunos.lineEdit_34.text()
    cpf = tela_cadastro_alunos.lineEdit_35.text()
    sexo = tela_cadastro_alunos.comboBox_2.currentText()
    email = tela_cadastro_alunos.lineEdit_37.text()
    senha = tela_cadastro_alunos.lineEdit_39.text()
    c_senha = tela_cadastro_alunos.lineEdit_40.text()
    telefone = tela_cadastro_alunos.lineEdit_33.text()
    login = tela_cadastro_alunos.lineEdit_38.text()
    data_matricula = tela_cadastro_alunos.lineEdit_41.text()
    curso = tela_cadastro_alunos.comboBox_3.currentText()
    turno = tela_cadastro_alunos.comboBox_4.currentText()
    carga_horaria_curso = tela_cadastro_alunos.lineEdit_42.text()

    if (senha == c_senha):
        try:
            # Verifica se o CPF já existe no banco de dados
            cursor.execute("SELECT cpf FROM cadastro_alunos WHERE cpf = %s", (cpf,))
            cpf_existente = cursor.fetchone()
            
            # Verifica se o login já existe no banco de dados
            cursor.execute("SELECT login FROM cadastro_alunos WHERE login = %s", (login,))
            login_existente = cursor.fetchone()

            if cpf_existente:
                tela_cadastro_alunos.label.setText("CPF já cadastrado!")
            elif login_existente:
                tela_cadastro_alunos.label.setText("Login já cadastrado!")
            else:
                # Insere os dados no banco de dados
                query = "INSERT INTO cadastro_alunos (Nome_Aluno, Data_Nascimento,Endereco,senha,login,cpf,sexo,telefone,data_matricula,curso,turno,email,carga_horaria) VALUES ( %s,%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
                cursor.execute(query, (nome_aluno, data ,endereco, senha, login, cpf,sexo,telefone,data_matricula,curso,turno,email,carga_horaria_curso))
                conexao.commit()
                tela_cadastro_alunos.close()
                tela_aluno_matriculado.show()
                
        except mysql.connector.Error as err:
            print("Erro:", err)
            tela_cadastro_alunos.label.setText("Preencha corretamente!")

        finally:
            # Fechar o cursor e a conexão
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and conexao.is_connected():
                conexao.close()     

    else:
       tela_cadastro_alunos.label.setText("As senhas digitadas estão diferentes")



def formatar_cedula(valor):
    # Converte o valor para float, se não estiver já em formato numérico
    valor_numerico = float(valor)
    # Formata o valor como uma cédula monetária usando o locale atual
    return locale.currency(valor_numerico, grouping=True)


# função para cadastro de professores
def cadastrar_professores():
    nome_professor = tela_cadastro_professores.lineEditNome.text()
    data_nascimento = tela_cadastro_professores.lineEditNascimento.text()
    # Convertendo a data de nascimento
    data_nascimento = tela_cadastro_professores.lineEditNascimento.text()
    data = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    # Convertendo a data de admissão
    data_admissao = tela_cadastro_professores.lineEditAdmissao.text()
    data2 = datetime.strptime(data_admissao, '%d/%m/%Y').date()
    endereco = tela_cadastro_professores.lineEditEndereco.text()
    login = tela_cadastro_professores.lineEditLogin.text()
    cpf = tela_cadastro_professores.lineEditCpf.text()
    sexo = tela_cadastro_professores.comboBoxSexo.currentText()
    email = tela_cadastro_professores.lineEditEmail.text()   
    telefone = tela_cadastro_professores.lineEditTelefone.text()
    senha = tela_cadastro_professores.lineEditSenha.text()
    c_senha = tela_cadastro_professores.lineEditCsenha.text()
    salario = tela_cadastro_professores.lineEditSalario.text()
    carga_horaria = tela_cadastro_professores.lineEditCargaHoraria.text()
    disciplina = tela_cadastro_professores.comboBoxDisciplina.currentText()
    turno_aula = tela_cadastro_professores.comboBox_turno.currentText()

    if (senha == c_senha):
        try:
            # Verifica se o CPF já existe no banco de dados
            cursor.execute("SELECT cpf FROM cadastro_professores WHERE cpf = %s", (cpf,))
            cpf_existente = cursor.fetchone()
            
            # Verifica se o login já existe no banco de dados
            cursor.execute("SELECT login FROM cadastro_professores WHERE login = %s", (login,))
            login_existente = cursor.fetchone()

            if cpf_existente:
                tela_cadastro_professores.label.setText("CPF já cadastrado!")
            elif login_existente:
                tela_cadastro_professores.label.setText("Login já cadastrado!")
            else:
                # Formata o salário como uma cédula monetária
                salario_formatado = formatar_cedula(salario)
                
                # Insere os dados no banco de dados
                query = "INSERT INTO cadastro_professores (nome_professores, Data_nascimento, Endereco, senha, login, cpf, sexo, email, data_de_admissao, salario, carga_horaria, disciplina_ministrada,turno_aula,telefone) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nome_professor, data, endereco, senha, login, cpf, sexo, email, data2, salario_formatado, carga_horaria, disciplina,turno_aula,telefone))
                conexao.commit()
                tela_cadastro_professores.close()
                tela_professor_cadastrado.show()
                
        except mysql.connector.Error as err:
            print("Erro:", err)
            tela_cadastro_professores.label.setText("Preencha corretamente!")

        finally:
            # Fechar o cursor e a conexão
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and conexao.is_connected():
                conexao.close()     

    else:
       tela_cadastro_professores.label.setText("As senhas digitadas estão diferentes")


def acesso_professor():
    tela_acesso_professor.acesso_invalido_professor.setText("")
    login_professor = tela_acesso_professor.login_professor.text()
    senha_professor = tela_acesso_professor.senha_professor.text()

    try:
        query =  "SELECT senha FROM cadastro_professores WHERE login = %s"
        cursor.execute(query, (login_professor, ))  
        result = cursor.fetchone()
        db_senha = result[0]

        if senha_professor == db_senha:
            tela_acesso_professor.close()
            tela_dados_professor.show()

            cursor.execute("SELECT nome_professores FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado = result[0] 
            tela_dados_professor.label_48.setText(dado)
            
            cursor.execute("SELECT carga_horaria FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado1 = result[0] 
            tela_dados_professor.text1.setText(f" {dado1} HORAS ")

            cursor.execute("SELECT data_de_admissao FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado2 = result[0] 
            tela_dados_professor.text_2.setText(dado2)

            cursor.execute("SELECT salario FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado3 = result[0] 
            tela_dados_professor.text_3.setText(dado3)

            cursor.execute("SELECT turno_aula FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado4 = result[0] 
            tela_dados_professor.text_4.setText(dado4)
            
            cursor.execute("SELECT disciplina_ministrada FROM cadastro_professores WHERE login = %s",(login_professor,))
            result = cursor.fetchone()
            dado5 = result[0] 
            tela_dados_professor.text_5.setText(dado5)


            


        else:
            tela_acesso_professor.acesso_invalido_professor.setText('Dados incorretos!!')        

    except:
       print('ERRO AO VALIDAR O LOGIN')
       tela_acesso_professor.acesso_invalido_professor.setText('Dados incorretos!!')  

    finally:
            
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and conexao.is_connected():
                conexao.close()     
          


# tela de login e acesso de dados de alunos 
def acesso_alunos():
    tela_acesso_aluno.acesso_invalido_aluno.setText("")
    login_aluno = tela_acesso_aluno.login_aluno.text()
    senha_aluno = tela_acesso_aluno.senha_aluno.text()
    

    try: 
        
        query =  "SELECT senha FROM cadastro_alunos WHERE login = %s"
        cursor.execute(query, (login_aluno, ))  
        result = cursor.fetchone()

        db_senha = result[0]
        
        if senha_aluno == db_senha:
            tela_acesso_aluno.close()
            tela_dados_alunos.show()
            

            # BUSCANDO NOME ALUNO
            cursor.execute("SELECT Nome_Aluno FROM cadastro_alunos WHERE login = %s",(login_aluno,))
            result = cursor.fetchone()
            dado = result[0] 
            tela_dados_alunos.label_47.setText( dado)
           
            # BUSCANDO CURSO
            cursor.execute("SELECT curso FROM cadastro_alunos WHERE login = %s",(login_aluno,))
            result = cursor.fetchone()
            dado_1 = result[0] 
            tela_dados_alunos.text_curso_aluno.setText(f" {dado_1} ")
            
            #BUSCANDO CARGA HORARIA
            cursor.execute("SELECT carga_horaria FROM cadastro_alunos WHERE login = %s",(login_aluno,))
            result = cursor.fetchone()
            dado_2 = result[0] 
            tela_dados_alunos.carga_horaria_aluno.setText(f" {dado_2} HORAS")

            #BUSCANDO TURNO
            cursor.execute("SELECT turno FROM cadastro_alunos WHERE login = %s",(login_aluno,))
            result = cursor.fetchone()
            dado_3 = result[0] 
            tela_dados_alunos.turno_aluno.setText(f" {dado_3}")

            #BUSCANDO DATA MATRICULA
            cursor.execute("SELECT data_matricula FROM cadastro_alunos WHERE login = %s",(login_aluno,))
            result = cursor.fetchone()
            dado_4 = result[0] 
            tela_dados_alunos.data_matricula.setText(f" {dado_4}")
            
            if (dado_1 == 'ENGENHARIA DA COMPUTAÇÃO'):

                # Consulta para selecionar as disciplinas com ID_DISCIPLINA = 2
                query1 = """
                SELECT nome_disciplina
                FROM disciplinas
                WHERE id_curso = 2
                """
                # Executa a consulta
                cursor.execute(query1)

                # Recupera os resultados
                nomes_disciplinas = [disciplina[0] for disciplina in cursor.fetchall()]
                tela_dados_alunos.materia_1.setText(nomes_disciplinas[0])
                tela_dados_alunos.materia_2.setText(nomes_disciplinas[1])
                tela_dados_alunos.materia_3.setText(nomes_disciplinas[2])
                tela_dados_alunos.materia_4.setText(nomes_disciplinas[3])
                tela_dados_alunos.materia_5.setText(nomes_disciplinas[4])
                tela_dados_alunos.materia_6.setText(nomes_disciplinas[5])

                    
               
            elif (dado_1 == 'LETRAS'):
                query1 = """
                SELECT nome_disciplina
                FROM disciplinas
                WHERE id_curso = 3
                """
                # Executa a consulta
                cursor.execute(query1)

                # Recupera os resultados
                nomes_disciplinas = [disciplina[0] for disciplina in cursor.fetchall()]
                tela_dados_alunos.materia_1.setText(nomes_disciplinas[0])
                tela_dados_alunos.materia_2.setText(nomes_disciplinas[1])
                tela_dados_alunos.materia_3.setText(nomes_disciplinas[2])
                tela_dados_alunos.materia_4.setText(nomes_disciplinas[3])
                tela_dados_alunos.materia_5.setText(nomes_disciplinas[4])
                tela_dados_alunos.materia_6.setText(nomes_disciplinas[5])
            
            elif (dado_1 == 'EDUCAÇÃO FÍSICA'):
                query1 = """
                SELECT nome_disciplina
                FROM disciplinas
                WHERE id_curso = 4
                """
                # Executa a consulta
                cursor.execute(query1)

                # Recupera os resultados
                nomes_disciplinas = [disciplina[0] for disciplina in cursor.fetchall()]
                tela_dados_alunos.materia_1.setText(nomes_disciplinas[0])
                tela_dados_alunos.materia_2.setText(nomes_disciplinas[1])
                tela_dados_alunos.materia_3.setText(nomes_disciplinas[2])
                tela_dados_alunos.materia_4.setText(nomes_disciplinas[3])
                tela_dados_alunos.materia_5.setText(nomes_disciplinas[4])
                tela_dados_alunos.materia_6.setText(nomes_disciplinas[5])

            elif (dado_1 == 'NUTRIÇÃO'):
                query1 = """
                SELECT nome_disciplina
                FROM disciplinas
                WHERE id_curso = 5
                """
                # Executa a consulta
                cursor.execute(query1)

                # Recupera os resultados
                nomes_disciplinas = [disciplina[0] for disciplina in cursor.fetchall()]
                tela_dados_alunos.materia_1.setText(nomes_disciplinas[0])
                tela_dados_alunos.materia_2.setText(nomes_disciplinas[1])
                tela_dados_alunos.materia_3.setText(nomes_disciplinas[2])
                tela_dados_alunos.materia_4.setText(nomes_disciplinas[3])
                tela_dados_alunos.materia_5.setText(nomes_disciplinas[4])
                tela_dados_alunos.materia_6.setText(nomes_disciplinas[5])    


               

            
        else:
           tela_acesso_aluno.acesso_invalido_aluno.setText('Dados incorretos!!')        

    except:
       print('ERRO AO VALIDAR O LOGIN')
       tela_acesso_aluno.acesso_invalido_aluno.setText('Dados incorretos!!')    

    finally:
            # Fechar o cursor e a conexão
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and conexao.is_connected():
                conexao.close()     





# TELA ATUALIZA DADOS DOS ALUNOS
def atualiza_alunos_dados():
    endereco = tela_atualiza_dados_alunos.lineEdit_34.text()
    cpf = tela_atualiza_dados_alunos.lineEdit_35.text()
    email = tela_atualiza_dados_alunos.lineEdit_37.text()
    login = tela_atualiza_dados_alunos.lineEdit_38.text()
    telefone = tela_atualiza_dados_alunos.lineEdit_33.text()
    turno = tela_atualiza_dados_alunos.comboBox_4.currentText()
    senha = tela_atualiza_dados_alunos.lineEdit_39.text()
    
    # Obter o índice da chave seletora
    indice_aluno = tela_atualiza_dados_alunos.comboBox_3.currentIndex()        
    # Obter o valor da chave seletora
    nome_aluno = tela_atualiza_dados_alunos.comboBox_3.itemText(indice_aluno)

    try:       
        consulta = "UPDATE cadastro_alunos SET"

        if endereco:
            consulta += f" Endereco = '{endereco}',"
        if cpf:
            consulta += f" cpf = '{cpf}',"
        if email:
            consulta += f" email = '{email}',"
        if login:
            consulta += f" login = '{login}',"
        if telefone:
            consulta += f" telefone = '{telefone}',"
        if turno:
            consulta += f" turno = '{turno}',"
        if senha:
            consulta += f" senha = '{senha}',"

        # Remover a vírgula final, se houver
        consulta = consulta.rstrip(',')
        
        consulta += f" WHERE Nome_Aluno = '{nome_aluno}'"
        
        cursor.execute(consulta)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Dados do aluno atualizados com sucesso!")
            tela_atualiza_dados_alunos.close()
            tela_cadastro_atualizado.show()
        else:
            print("Erro ao atualizar dados do aluno.")

    except Exception as e:
        print(f'Erro ao atualizar dados: {e}')

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

def atualiza_professores_dados():
  
    endereco = tela_atualiza_dados_professores.lineEditEndereco.text()
    login = tela_atualiza_dados_professores.lineEditLogin.text()
    cpf = tela_atualiza_dados_professores.lineEditCpf.text()
    email = tela_atualiza_dados_professores.lineEditEmail.text()
    senha = tela_atualiza_dados_professores.lineEditSenha.text()
    salario = tela_atualiza_dados_professores.lineEditSalario.text()
    carga_horaria = tela_atualiza_dados_professores.lineEditCargaHoraria.text()
    disciplina = tela_atualiza_dados_professores.comboBoxDisciplina.currentText()
    telefone = tela_atualiza_dados_professores.lineEditTelefone.text()
    turno = tela_atualiza_dados_professores.comboBox_turno.currentText()
    
    #  Obter o índice da chave seletora
    indice_professor = tela_atualiza_dados_professores.comboBoxNome.currentIndex()        
    # Obter o valor da chave seletora
    nome_professor = tela_atualiza_dados_professores.comboBoxNome.itemText(indice_professor)

    # Essa modificação garantirá que apenas os campos preenchidos sejam incluídos na atualização da consulta SQL.
    try:       
        consulta = "UPDATE cadastro_professores SET"

        if endereco:
            consulta += f" Endereco = '{endereco}',"
        if cpf:
            consulta += f" cpf = '{cpf}',"
        if email:
            consulta += f" email = '{email}',"
        if login:
            consulta += f" login = '{login}',"
        if telefone:
            consulta += f" telefone = '{telefone}',"
        if turno:
            consulta += f" turno_aula = '{turno}',"
        if senha:
            consulta += f" senha = '{senha}',"
        if disciplina:
            consulta += f" disciplina_ministrada = '{disciplina}',"
        if salario:
            salario_formatado = formatar_cedula(salario)
            consulta += f" salario = '{salario_formatado}',"
        if carga_horaria:
            consulta += f" carga_horaria = '{carga_horaria}',"

        # Remover a vírgula final, se houver
        consulta = consulta.rstrip(',')
        
        consulta += f" WHERE nome_professores = '{nome_professor}'"
        
        cursor.execute(consulta)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Dados do professor atualizados com sucesso!")
            tela_atualiza_dados_professores.close()
            tela_cadastroProfessor_atualizado.show()
        else:
            print("Erro ao atualizar dados do professor.")
            tela_atualiza_dados_professores.label.setText('ERRO AO ATUALIZAR DADOS')     


    except Exception as e:
        print(f'Erro ao atualizar dados: {e}')
        tela_atualiza_dados_professores.label.setText('ERRO AO ATUALIZAR DADOS')     

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close() 

def lista_professores():
    tela_adm_cadastro.close()
    tela_lista_professores.show()
    
    try:

        if not conexao.is_connected():
            conexao.connect()

        cursor = conexao.cursor()  # Obter um novo cursor
        # Consulta SQL para selecionar os dados desejados
        query = "SELECT nome_professores, data_de_admissao, turno_aula, disciplina_ministrada,salario FROM cadastro_professores;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Populando o tableWidget com os dados
        tela_lista_professores.tableWidget.setRowCount(len(rows))
        tela_lista_professores.tableWidget.setColumnCount(5)
        headers = ["Nome", "Data de Admissão", "Turno", "Disciplina","Salário"]
        tela_lista_professores.tableWidget.setHorizontalHeaderLabels(headers)

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                tela_lista_professores.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    except Exception as e:        
        print('Erro:', e)
    finally:       
        conexao.close()


def lista_alunos():
    tela_adm_cadastro.close()
    tela_lista_alunos.show()
    try:
        if not conexao.is_connected():
            conexao.connect()

        cursor = conexao.cursor()  
        
        query1 = "SELECT Nome_aluno, data_matricula, turno, curso FROM cadastro_alunos;"
        cursor.execute(query1)
        rows = cursor.fetchall()

        # Populando o tableWidget com os dados
        tela_lista_alunos.tableWidget_2.setRowCount(len(rows))
        tela_lista_alunos.tableWidget_2.setColumnCount(4)
        headers = ["Nome", "Data de Matricula", "Turno", "curso"]
        tela_lista_alunos.tableWidget_2.setHorizontalHeaderLabels(headers)

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                tela_lista_alunos.tableWidget_2.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    except Exception as e:
        # Exibir a mensagem de erro específica
        print('Erro:', e)
    finally:
        # Fechar a conexão com o banco de dados
        conexao.close()    










app=QtWidgets.QApplication([])


# TELAS 
primeira_tela=uic.loadUi("primeira_tela.ui")
tela_acesso_professor = uic.loadUi("tela_acesso_professor.ui")
tela_acesso_aluno = uic.loadUi("tela_acesso_aluno.ui")
tela_acesso_adm = uic.loadUi("tela_acesso_adm.ui")
tela_adm_cadastro = uic.loadUi("tela_adm_cadastro.ui")
tela_cadastro_alunos = uic.loadUi("tela_cadastro_alunos.ui")
tela_cadastro_professores = uic.loadUi("tela_cadastro_professor.ui")
tela_dados_alunos = uic.loadUi("dados_aluno.ui")
tela_aluno_matriculado = uic.loadUi("tela_aluno_matriculado.ui")
tela_professor_cadastrado = uic.loadUi("tela_professor_cadastrado.ui")
tela_atualiza_dados_alunos = uic.loadUi("tela_atualiza_dados_alunos.ui")
tela_atualiza_dados_professores = uic.loadUi("tela_atualiza_dados_professores.ui")
tela_cadastro_atualizado = uic.loadUi("tela_cadastro_atualizado.ui")
tela_cadastroProfessor_atualizado = uic.loadUi("tela_cadastroProfessor_atualizado.ui")
tela_dados_professor = uic.loadUi("tela_dados_professor.ui")
tela_lista_professores = uic.loadUi("lista_professores_cadastrados.ui")
tela_lista_alunos = uic.loadUi("lista_alunos_matriculados.ui")



# BOTOES TELAS ALUNOS
tela_cadastro_alunos.botao_cadastrar_alunos.clicked.connect(matricular_alunos)
tela_acesso_aluno.botao_acesso_aluno.clicked.connect(acesso_alunos)
tela_atualiza_dados_alunos.botao_atualizar_alunos.clicked.connect(atualiza_alunos_dados)
tela_cadastro_alunos.botao_voltar.clicked.connect(voltar_tela_adm_cadastro)
tela_cadastro_professores.botao_voltar.clicked.connect(voltar_tela_adm_cadastro_cad_professores)
tela_atualiza_dados_alunos.botao_voltar.clicked.connect(voltar_tela_adm_cadastro_atualiza)
tela_cadastro_atualizado.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_cadastro_atualizado.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_lista_alunos.botao_tela_principal.clicked.connect(voltar_tela_adm_cadastro)
tela_dados_alunos.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_acesso_aluno.botao_voltar_aluno.clicked.connect(reiniciar_sistema)
tela_aluno_matriculado.botao_tela_principal.clicked.connect(reiniciar_sistema)


# BOTÕES TELA PROFESSOR
primeira_tela.botao_professor.clicked.connect(entrar_tela_acesso_prof)
primeira_tela.botao_acesso_aluno.clicked.connect(entrar_tela_acesso_aluno)
tela_cadastro_professores.botao_cadastrar_professor.clicked.connect(cadastrar_professores)
tela_atualiza_dados_professores.botao_atualizar_professores.clicked.connect(atualiza_professores_dados)
tela_acesso_professor.botao_voltar_professor.clicked.connect(reiniciar_sistema)
tela_dados_professor.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_professor_cadastrado.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_lista_professores.botao_tela_principal.clicked.connect(voltar_tela_adm_cadastro)
tela_cadastroProfessor_atualizado.botao_tela_principal.clicked.connect(reiniciar_sistema)
tela_acesso_professor.botao_acesso_professor.clicked.connect(acesso_professor)
tela_atualiza_dados_professores.botao_voltar.clicked.connect(voltar_tela_adm_cadastro_atualiza_professores)
tela_professor_cadastrado.botao_tela_principal.clicked.connect(reiniciar_sistema)

# BOTOES TELA ADM
tela_acesso_adm.botao_acesso_adm.clicked.connect(acesso_adm_cadastro)
tela_acesso_adm.botao_voltar_adm.clicked.connect(reiniciar_sistema)
primeira_tela.botao_acesso_adm.clicked.connect(entrar_login_adm)
tela_adm_cadastro.botao_matricula_aluno.clicked.connect(entrar_matricula_aluno)
tela_adm_cadastro.botao_cadastro_professor.clicked.connect(entrar_cadastra_professor)
tela_adm_cadastro.pushButton.clicked.connect(reiniciar_sistema)
tela_adm_cadastro.botao_atualiza_aluno.clicked.connect(entrar_atualiza_aluno)
tela_adm_cadastro.botao_atualiza_professor.clicked.connect(entrar_atualiza_professor)
tela_adm_cadastro.consulta_prof.clicked.connect(lista_professores)
tela_adm_cadastro.consultar_alunos.clicked.connect(lista_alunos)


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
cursor = conexao.cursor()
primeira_tela.show()
app.exec()