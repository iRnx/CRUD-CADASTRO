import mysql.connector


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='cadastro2')
        return conn
    except mysql.connector.Error as e:
        print(f'Erro ao conectar ao Servidor MySQL: {e}')


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pessoas')
    linhas = cursor.fetchall()
    if len(linhas) > 0:
        print('=' * 20)
        for linha in linhas:
            print(f'ID: {linha[0]}')
            print(f'Nome: {linha[1]}')
            print(f'Sobrenome: {linha[2]}')
            print(f'Sexo: {linha[3]}')
            print(f'Data de Nascimento: {linha[4]}')
            print(f'CPF: {linha[5]}')
            print(f'Email: {linha[6]}')
            print(f'Rua: {linha[7]}')
            print(f'Número: {linha[8]}')
            print(f'Complemento: {linha[9]}')
            print(f'Cep: {linha[10]}')
            print(f'Cidade: {linha[11]}')
            print(f'Estado: {linha[12]}')
            print('=' * 20)
    else:
        print('Tabela Vazia...')

    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    nome = str(input('Insira o Nome para o Cadastro: ')).strip().title()
    sobrenome = str(input('Insira o Sobrenome para Cadastro: ')).strip().title()
    sexo = str(input('Inser o Sexo [M/F]: ')).strip().upper()[0]
    data_nascimento = str(input('Insira sua Data de Nascimento: ')).strip()
    cpf = int(input('Digite seu CPF: '))
    email = str(input('Digite seu Email: ')).strip()
    rua = str(input('Nome da sua rua: ')).strip().title()
    numero = int(input('Número da casa: '))
    complemento = str(input('Complemento: ')).strip().upper()
    if complemento == '':
        complemento = 'Sem Complemento'
    cep = int(input('Cep: '))
    cidade = str(input('Cidade: ')).strip().title()
    estado = str(input('Estado: ')).strip().upper()
    injetar = f"""INSERT INTO pessoas
    (nome, sobrenome, sexo, data_nascimento, cpf, email, rua, numero, complemento, cep, cidade, estado) VALUES
    ('{nome}', '{sobrenome}', '{sexo}', '{data_nascimento}', '{cpf}', '{email}', '{rua}', {numero},
    '{complemento}', {cep}, '{cidade}', '{estado}')"""
    cursor.execute(injetar)
    conn.commit()

    if cursor.rowcount == 1:
        print(f'{nome} cadastrado com Sucesso!!')
    else:
        print(f'Erro ao cadastrar {nome}')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Insira o ID do Cadastro que deseja Atualizar: '))
    nome = str(input('Insira um novo Nome: ')).strip().title()
    sobrenome = str(input('Insira um novo Sobrenome: ')).strip().title()
    sexo = str(input('Insira um novo Sexo [M/F]: ')).strip()[0]
    data_nascimento = str(input('Insira a nova Data de Nascimento: ')).strip()
    cpf = int(input('Insira o novo CPF: '))
    email = str(input('Insira o novo Email: ')).strip()
    rua = str(input('Insira o novo Nome da Rua: ')).strip().title()
    numero = int(input('Insira o novo numero da casa: '))
    complemento = str(input('Insira o novo Complemento: ')).strip().upper()
    if complemento == '':
        complemento = 'Sem Complemento'
    cep = int(input('Insira o novo Cep: '))
    cidade = str(input('Insira o novo nome da Cidade: ')).strip().title()
    estado = str(input('Insira a nova Sigla do Estado: ')).strip().upper()
    att = f"""UPDATE pessoas SET nome = '{nome}', sobrenome = '{sobrenome}', sexo = '{sexo}',
    data_nascimento = '{data_nascimento}', cpf = {cpf}, email = '{email}', rua = '{rua}', numero = {numero},
    complemento = '{complemento}', cep = {cep}, cidade = '{cidade}', estado = '{estado}'
    WHERE id = {codigo}"""
    cursor.execute(att)
    conn.commit()

    if cursor.rowcount == 1:
        print('Cadastro Atualizado com Sucesso!!')
    else:
        print(f'Erro ao Atualizar o Cadastro com id: {codigo}')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Insira o Id que deseja Deletar: '))
    cursor.execute(f'DELETE FROM pessoas WHERE id = {codigo}')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Cadastro {codigo} Deletado com Sucesso: ')
    else:
        print('Erro ao Deletar Cadastro!!!')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Sair do Programa.')
        opcao = int(input('Digite um Número: '))
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                break
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')


if __name__ == '__main__':
    menu()
