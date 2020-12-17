# PF/GIFOR

Esse repositório tem como objetivo guardar minhas soluções para participação do processo seletivo para estágio na Polícia Federal no Grupo de Integração Forense da Polícia Federal, assim como, explicar como se deu a solução.

## Processo Seletivo

A primeira etapa consiste na solução de dois problemas em *Python*.

### Problema 1

Dado uma lista de dicionários (chave/valor) *Python* verifique se existe a chave __'nome'__, e caso exista salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.

#### Sobre a Solução

Devido a natureza do problema, decidi por implementar uma função que recebe uma lista de dicionários como argumento e que retorna uma lista contendo os nomes sem repetição. Essa função pecorre a lista procurando a chave __'nome'__ nos dicionários. Quando é encontrada, o valor corresponde é adicionado a uma nova lista. Para manter a lista sem valores repetidos eu uso do artifício da classe *set*, que possiblilita a construção de uma coleção com elementos únicos.

Para mais detalhes a respeito da implementação do código acesse a [solução](problema_1/problema_1.py).

### Problema 2

Dado um arquivo csv com delimitador __';'__ e com o seguinte cabeçalho: id;nome;telefone;idade. Retorne uma lista com os registros ordenados por nome.
Exemplo de arquivo:

``` txt
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12
```

Para esse problema eu descidi por fazer duas implementação. A duas seguem a mesma linha de raciocínio e paradigma, orientação a objetos. Entretanto, diferem-se na função que lê do arquivo csv. Na primeira eu utilizo apenas a *API* padrão, enquanto na segunda solução também utilizo a biblioteca [pandas](https://pandas.pydata.org/) para auxiliar na manipulação do arquivo csv.

Para modelar os registros criei uma classe chamada Pessoa, assim posso transformar cada linha de valores do arquivo em objeto contendo os campos id, nome, telefone e idade.

Após ler do arquivo e transformar o registro em uma lista de objetos(pessoas), chamo o método sort passando como chave o atributo nome.

Para mais detalhes a respeito da implementação dos códigos acesse as soluções:

- [solução 1](problema_2/problema_2.py);

- [solução 2](problema_2/problema_2_pandas.py).

## Execução do Código

Para facilitar a execução e não ser necessária a preparação do ambiente eu criei um notebook online utilizando a ferramenta [Colab](https://colab.research.google.com/notebooks/intro.ipynb).

A execução é bem simples:

- acesse o [notebook](https://colab.research.google.com/drive/1dIMh-SGwknqhFgEkwr1nIQkK55t2Zs3t?usp=sharing); e
- aperte o *play*.

### Observações

- versão do *Python*: __Python 3.5.2__;
- versão do *pandas*: __pandas 2.8.1__;
- [instalação da biblioteca pandas](https://pandas.pydata.org/getting_started.html) para execução local;
- A solução não contempla o tratamento de exceções caso o usuário passar um *path* inexistente ou se o mesmo não conter dados corentes com o formato csv válido.

## Autor

[Lieverton Santos Silva](https://lievertom.github.io/)
