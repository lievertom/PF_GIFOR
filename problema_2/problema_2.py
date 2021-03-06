'''
Problema 2:
Dado um arquivo csv com delimitador ';' 
e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registros ordenados por nome.
'''

# Para resolução deste problema decidi utilizar orientação a objetos.
# Devido se tratar de dados uniformes, vou usar uma classe
# para poder modelar os dados referentes às pessoas ,e assim,
# resolver o problema de forma mais elegante.

class Pessoa:
    '''
    Modelo para representar uma pessoa

    atributos:
              id: identificador da pessoa
            nome: nome da pessoa
        telefone: telefone da pessoa
           idade: idade da pessoa 
    '''
    # Obs.: de forma a manter a coerência dos dados,
    #       a melhor formar de resgatar a idade de uma
    #       pessoa seria guardar a data de nascimento,
    #       logo que a idade deriva da data de nascimento. 

    # Contrutor da classe
    def __init__(self, id, nome, telefone, idade):
        self.id = int(id)
        self.nome = nome
        self.telefone = int(telefone)
        self.idade = int(idade)

    # Esse método é usado para representação do obejo como uma string,
    # ele também permite a formatação da string 
    def __repr__(self):
        return repr((self.id, self.nome, self.telefone, self.idade)) # representação do objeto como tupla
        # return '\n%s;%s;%s;%s' % (self.id, self.nome, self.telefone, self.idade) # representação do objeto como linha do csv
        # return "\n{'id': %s, 'nome': '%s', 'telefone': %s, 'idade': %s}" % (self.id, self.nome, self.telefone, self.idade) # representação do objeto como dicionário

    # Esse método retorna o nome e é usado como argumento para ordenação 
    def get_nome(self):
        return self.nome

# Esse método lê os dados do arquivo csv e os transforma em uma lista de pessoas
def ler_csv (arquivo, delimitador):
    '''
    Método para ler informações do arquivo csv

    atributo:
        arquivo: caminho do arquivo csv com as 
                    informações das pessoas.
    '''

    # abre o arquivo no modo leitura
    arquivo_csv = open(arquivo, 'r')

    # descarta  a primeira linha
    arquivo_csv.readline() 

    #Carrega os registros
    dados = arquivo_csv.readlines()

    # Declara uma lista vazia 
    pessoas = []

    # Pecorre cada linha dos dados pegando cada atributo necessário para construir um objeto
    for linha in dados:
        # o método split retona uma lista de strings
        valor = linha.split(sep=delimitador)
        # verificação da quantidade de argumentos para a criação do objeto
        if len(valor) == 4:
            id = int(valor[0])
            nome = valor[1]
            telefone = int(valor[2])
            idade = int(valor[3])

            # Construção do objeto 
            pessoa = Pessoa(id, nome, telefone, idade)
            # Adição do objeto pessoa na lista de pessoas
            pessoas.append(pessoa)

    # fecha o arquivo
    arquivo_csv.close()

    # retornada uma lista de pessoas
    return pessoas

# Essé método contém valores padrões caso o usuário não passe os argumentos para função
def registros_ordenados (arquivo= 'arquivo_teste.csv', delimitador= ';'):
    '''
    Método para resgatar os registros ordenados pelo nome

    Atributos:
            arquivo: caminho do arquivo csv com as
                     informações das pessoas
        delimitador: delimitador do arquivo csv
    '''
    
    # Chama a função ler_cvs para para obter os registros  
    pessoas = ler_csv(arquivo, delimitador)

    # Ordena  os registros
    pessoas.sort(key=Pessoa.get_nome)

    # retorna os registros ordenados
    return pessoas

# Execução do problema:
registros_ordenados_nome = registros_ordenados()

#imprme a lista com os registros ordenados pelo nome
print(registros_ordenados_nome)