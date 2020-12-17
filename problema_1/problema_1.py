'''
Problema 1
Dado uma lista de dicionários (chave/valor) Python,
verifique se existe a chave 'nome', e caso exista,
salve o valor dessa chave em uma segunda lista, de
modo que não haja repetição de valores na segunda lista.
'''

# Declaração da lista de dicionário para usar como exemplo,
# essa lista contém dados não uniformes sobre pessoas.
lista_pessoas = [
    {'nome':'Maria', 'idade':26, 'sexo':'F'},
    {'cpf':00000000000, 'idade':100, 'sexo':'M'},
    {'email': 'pedro@email.com', 'idade':55, 'sexo':'F'},
    {'nome': 'Maria', 'idade':43, 'email': 'maria@email.com'},
    {'nome': 'Raimundo', 'cidade':'Gama'},
    {'nome': 'Raimundo', 'cidade':'Gama'},
    {'id':1, 'nome':'João', 'telefone':43383832, 'idade':28},
    {'id':2, 'nome':'Maria', 'telefone':43839322, 'idade':32},
    {'matrícula': 122345, 'nome':'João'},
    {'nome': 'Felipe', 'sexo': 'M', 'email': 'felippe@email.com'},
    {'nome': 'Moraes', 'sexo': 'M', 'email': 'moraes@email.com'}
]

# Essa função é responsável por pegar cada nome disponível uma única vez
def extrai_nomes_sem_repeticao (pessoas):
    # Para cumprir a tarefa de forma simples eu uso a classe 'set'.
    # Essa classe permite construir uma coleção de elementos não ordenados,
    # porém únicos.
    nomes = set(())

    # Pecorro a lista de pessoas procurando pela chave 'nome'.
    for pessoa in pessoas:
        # Esse método permite verificar se o dicionário contém a chave 'nome'
        # e se o valor correspondente é não nulo.
        if pessoa.get('nome'):
            # A classe contém o método 'add' que adiciona um valor
            # à coleção uma única vez
            nomes.add(pessoa['nome'])

    # Neste ponto já temos uma coleção com os nomes sem repetição,
    # então converto para uma lista e retorno a mesma
    return list(nomes)


# Execução do problema:
# Passo a lista com os dados das pessoas como parametro e recebo os nomes sem repetição
nomes_sem_repeticao = extrai_nomes_sem_repeticao(lista_pessoas)

# Imprimo a lista de nomes sem repetição
print(nomes_sem_repeticao)
