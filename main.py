import os
import oracledb
import pandas as pd


def sair_programa():
    print("Fechando o programa...")
    exit()


def bancodedados():
    # Try para tentativa de Conexão com o Banco de Dados
    try:
        # Efetua a conexão com o Usuário no servidor
        conn = oracledb.connect(user='rm560575', password="fiap24", dsn='oracle.fiap.com.br:1521/ORCL')
        # Cria as instruções para cada módulo
        inst_cadastro = conn.cursor()
        inst_consulta = conn.cursor()
        inst_exclusao = conn.cursor()

    except Exception as e:
        # Informa o erro
        print("Erro: ", e)
        # Flag para não executar a Aplicação
        conexao = False
    else:
        # Flag para executar a Aplicação
        conexao = True
    while conexao:
        os.system('cls')
        print("---MENU DO BANCO DE DADOS---\n")
        while True:
            try:
                print("\nDigite a oppção desejada:\n"
                      "1) Adcionar registro\n"
                      "2) listar registro\n"
                      "3) excluir registro\n"
                      "4) excluir tudo\n"
                      "0) Sair do progrma\n")
                opcao2 = int(input("Digite a opção escolhida: "))
            except ValueError:
                print("Digite um valor valido")
            else:
                if opcao2 == 1:
                    try:
                        # pergunta os valores para cadastro
                        ph = float(input("Digite o valor do ph: "))
                        potassio = int(input("Possui potassio? 1 = Sim || 2 = Não: "))
                        fosforo = int(input("Possui fosforo? 1 = Sim || 2 = Não: "))
                        bomba_ligada = int(input("Bomba estava ligada? 1 = Sim || 2 = Não: "))
                        # Monta a instrução SQL de cadastro em uma string
                        cadastro = f""" INSERT INTO farmtech (valor_ph, valor_potassio, valor_fosforo, bomba_ligada) 
                        VALUES ('{ph}', {potassio}, {fosforo}, {bomba_ligada}) """
                        # Executa e grava o Registro na Tabela
                        inst_cadastro.execute(cadastro)
                        conn.commit()
                    except:
                        print("Erro na transação do BD")
                    else:
                        print("\nDados gravados\n")
                    input("Presione ENTER")

                elif opcao2 == 2:
                    lista_dados = []
                    inst_consulta.execute('SELECT * FROM farmtech')
                    data = inst_consulta.fetchall()
                    for dt in data:
                        lista_dados.append(dt)
                    lista_dados = sorted(lista_dados)
                    dados_df = pd.DataFrame.from_records(lista_dados,
                                                         columns=['id', 'valor_ph', 'valor_potassio', 'valor_fosforo',
                                                                  'bomba_ligada'])
                    if dados_df.empty:
                        print(f"Não há dados no banco")
                    else:
                        print(dados_df)

                elif opcao2 == 3:
                    # EXCLUIR UM REGISTRO
                    lista_dados = []  # Lista para captura de dados da tabela
                    registro_id = input("Escolha um Id: ")  # Permite o usuário escolher um Pet pelo ID
                    if registro_id.isdigit():
                        reg_id = int(registro_id)
                        consulta = f""" SELECT * FROM farmtech WHERE id = {registro_id}"""
                        inst_consulta.execute(consulta)
                        data = inst_consulta.fetchall()

                        # Insere os valores da tabela na lista
                        for dt in data:
                            lista_dados.append(dt)

                        # Verifica se o registro está cadastrado
                        if len(lista_dados) == 0:
                            print(f"Não há um registro com o ID = {registro_id}")
                        else:
                            # Cria a instrução SQL de exclusão pelo ID
                            exclusao = f"DELETE FROM farmtech WHERE id={registro_id}"
                            # Executa a instrução e atualiza a tabela
                            inst_exclusao.execute(exclusao)
                            conn.commit()
                            print("\nregistro apagado")  # Exibe mensagem caso haja sucesso
                    else:
                        print("O Id não é numérico!")
                    input("Pressione ENTER")  # Pausa o loop para a leitura da mensagem

                elif opcao2 == 4:
                    # EXCLUIR TODOS OS REGISTROS

                    print("\nExlcuir todos os registros?\n")
                    confirma = input("CONFIRMA A EXCLUSÃO DE TODOS OS REGISTROS?[S]im ou [N]ÃO?")
                    if confirma.upper() == "S":
                        # Apaga todos os registros
                        exclusao = "DELETE FROM farmtech"
                        inst_exclusao.execute(exclusao)
                        conn.commit()

                        # Depois de excluir todos os registros ele zera o ID
                        data_reset_ids = """ ALTER TABLE farmtech MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                        inst_exclusao.execute(data_reset_ids)
                        conn.commit()

                        print("\nTodos os registros foram excluídos!")
                    else:
                        print("Operação cancelada pelo usuário!")
                    input("Pressione ENTER")  # Pausa o loop para a leitura da men

                elif opcao2 == 0:
                    sair_programa()
                else:
                    print("Digite um valor valido ")


bancodedados()

