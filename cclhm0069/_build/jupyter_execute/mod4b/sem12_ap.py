#!/usr/bin/env python
# coding: utf-8

# # Python do Zero I
# 
# <small>Material para o Live Coding 1, 26/01/2022, referente à [semana 12 do curso](https://ericbrasiln.github.io/intro-historia-digital/mod4b/sem12.html#)</small>
# 
# O objetivo desse encontro virtual é tirar dúvidas quanto à instalação do Python e do Visual Studio Code e apresentar alguns conceitos básicos de programação.

# 
# 
# ![python](https://cdn.pixabay.com/photo/2017/01/31/23/21/animal-2028134_960_720.png)
# 
# ---
# 
# **OBS:**
# 
# Trechos e exemplos foram retirados dos seguintes  materiais:
# 
# * [Introductions to cultural analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/index.html) de [Melanie Walsh](https://melaniewalsh.org/);
# * [Python Basics 1-3](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-1.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless;
# * [Pense Python 2ª edição](https://penseallen.github.io/PensePython2e/) de Allen Downey.

# ## Pq Python?
# 
# [Python](https://docs.constellate.org/key-terms/#python) é uma das linguagens de programação que mais crescem no mundo. Aprender Python] é uma ótima escolha pois é uma linguagem:
# 
# * amplamente adotada nas humanidades digitais e ciência de dados;
# * que tem uma curva de aprendizado menor do que outras linguagens; 
# * flexível, possuíndo amplo suporte para lidar com dados numéricos e textuais;
# * que lembra o inglês e é legível para quem sabe esse idioma.

# ## Anatomia de um script Python
# Adaptado do curso [Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/03-Anatomy-Python-Script.html) de Melanie Walsh.
# 
# Geralmente, o código escrito em Python para executar alguma função, salvo em um arquivo com a extensão *.py*, chamdo **script** possui uma estrutura que segue certo padrão. Ou melhor, possui um conjunto de elementos básicos e lógicos.
# 
# Vamos olhar o script abaixo e entender cada trecho.
# 

# In[ ]:


'''
Esse script pretende ser um exemplo de como se
estrutura um script Python.
'''

# Importando bilbiotecas
import time

# cria variável com o dia e hora atual
now = time.strftime("%d/%m/%Y %H:%M:%S")

#print() é uma função para imprimir um valor na tela
print(now)

# input() é uma função para receber um valor digitado pelo usuário  
name = input("Digite seu nome: ")

print('\nOlá, ' + name + '!')
# fim do script


# ## Terminal 
# 
# Além de poder executar comandos de Python no Jupyter Notebook, podemos e comumente vamos executar comandos e scripts diretamente através de linhas de comando no terminal.
# 
# ```
# python3 <nome-do-script>.py
# 
# ``` 
# 
# Ou ainda, você pode acessar o python em seu terminal e executar comandos de forma interativa executando o comando:
# 
# ```
# python3
# ```
# 

# ## Operadores Aritméticos
# 
# [Python Basics 1](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-1.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# |Operador| Operação| Exemplo | Resultado |
# |---|----|---|---|
# |\*\*| Potência| 3 ** 3 | 27 |
# |%| Resto da divição| 34 % 6 | 4 |
# |/| Divisão | 30 / 6 | 5|
# |//| Divisão inteira | 27 // 6 | 4 |
# |\*| Multiplicação | 7 * 8 | 56 |
# |-| Subtração | 18 - 4| 14|
# |+| Adição | 4 + 3 | 7 |

# ## Operadores relacionais
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# |Operador|Significado|
# |---|---|
# |==|Igual|
# |!=|diferente|
# |<|Menor que|
# |>|Maior que|
# |<=|Menor ou igual que|
# |>=|Maior ou igual que|

# ## Operadores Booleanos (and/or/not)
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# ### and
# 
# ```True and True = True```

# ### or
# 
# |Expressão|Avaliação|
# |---|---|
# |True or True|True|
# |True or False|True|
# |False or True|True|
# |False or False|False|
# 

# ## Variáveis
# Traduzido de [Variables](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/04-Variables.html) Melanie Walsh.
# 
# As variáveis são um dos blocos de construção fundamentais do Python. Uma variável é como um pequeno contêiner onde você armazena valores e dados, como nomes de arquivos, palavras, números, coleções de palavras e números e muito mais.

# ### Definindo variáveis
# 
# O nome da variável apontará para um valor que você "atribui" a ele. Você pode pensar em atribuição de variável como colocar um valor "dentro" da variável, como se a variável fosse uma pequena caixa 🎁
# 
# Você atribui variáveis com um sinal de igual `=`. Em Python, um único sinal de igual `=` é o "operador de atribuição". Um sinal de igual duplo `==` é o sinal de igual "real".

# In[ ]:


# criar uma variável
nome = 'Maria'
#imprimir o valor da variável
print(nome)


# In[ ]:


2+2 == 4


# ### Nomeando variáveis
# 
# Os nomes das variáveis podem ser tão longos ou curtos quanto você quiser e podem incluir:
# - letras maiúsculas e minísculas (A-Z)
# - dígitos (0-9)
# - underscores (_)
# 
# No entanto, os nomes das variáveis * não podem * incluir:
# - ❌ outras pontuações (-.!?@)
# - ❌ spaces ( )
# - ❌ uma palavra reservada do Python
# 
# Variáveis claras e nomeadas com precisão irão:
# 
# * tornar seu código mais legível (para você e para outras pessoas)
# * reforçar sua compreensão do Python e do que está acontecendo no código
# * esclarecer e fortalecer seu pensamento
# 
# Para maiores informações veja o [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

# ### Palavras-chave do Python
# Retirado de [Pense Python](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html) de Allen Downey, capítulo 2.
# 
# O interpretador usa palavras-chave para reconhecer a estrutura do programa e elas não podem ser usadas como nomes de variável.
# 
# O Python 3 tem estas palavras-chave:
# 
# ```
# and         del         from        None        True
# as          elif        global      nonlocal    try
# assert      else        if          not         while
# break       except      import      or          with
# class       False       in          pass        yield
# continue    finally     is          raise
# def         for         lambda      return
# ```
# 
# Você não precisa memorizar essa lista. Na maior parte dos ambientes de desenvolvimento, as palavras-chave são exibidas em uma cor diferente; se você tentar usar uma como nome de variável, vai perceber.

# ### Redefinindo variáveis
# 
# As variáveis não são fixas, é possível atribuir novos valores a uma varivável que já havia sido definida anteriormente.

# In[ ]:


nome = 'Eric'
print(nome)


# ## Tipos de Dados
# 

# Existem quatro tipos essenciais de dados Python com diferentes poderes e capacidades:
# 
# - Strings (texto)
# - Inteiros (números inteiros)
# - Floats (números decimais)
# - Booleans (verdadeiro / falso)

# 
# |Tipo | Explicação | Exemplo |
# |---|---|---|
# |integer|número inteiro| -3, 0, 2, 534|
# |float|número decimal | 6.3, -19.23, 5.0, 0.01|
# |string|texto| 'Hello world', '1700 butterflies', '', '1823'|
# |boolean|Verdadeiro ou Falso| True/False|
# 

# Você pode verificar o tipo de dados de qualquer valor usando a função `type ()`.

# In[ ]:


type(nome)


# ### print() input() e format()
# 
# Para imprimir na tela um valor devemos utilizar a função `print()`.
# 
# Para receber um valor de entrada do usuário, usamos a função `input()`.
# 
# Usamos format() para formatar strings.

# In[ ]:


print(nome)

new_name = input('Digite seu nome: ')
print(new_name)

print(f'Olá, {new_name}! Como vai?')


# ### Strings

# Uma *string* é um tipo de dados Python que é tratado como texto, mesmo que contenha um número. As strings são sempre colocadas entre aspas simples `'isto é uma string'` ou aspas duplas `"isto é uma string"`.
# 
# Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):
# 
# >Strings não são como números inteiros, de ponto flutuante ou booleanos. Uma string é uma sequência, ou seja, uma coleção ordenada de outros valores. (...) Uma string é uma sequência de caracteres.

# É possível acessar um caracter específico da string com o operador []
# 
# A expressão entre colchetes chama-se índice. O índice aponta qual caractere da sequência você quer
# 
# ---

# **Vamos usar um exemplo que preste**
# 
# <img src="https://www.beyonce.com/uploads/2021/09/090821_valentinojeans_02_ekpqrul_gen.gif" alt="queen bey" width="200">

# In[ ]:


music = 'Formation'
music[1]


# **Opa! o caractere na posição 1 da string music não deveria ser 'U'?**
# 
# A contagem de índices no Python começa em `0`, ou seja, o primeiro caractere é na posição 0.
# 
# A indexação é baseada na distância do ponto de partida e como o primeiro elemento está a uma distância *zero* do ponto de partida, seu índice é `0`.

# In[ ]:


music[0]


# E pra acessar o último elemento da string, você pode usar índices negativos.

# In[ ]:


music[-1]


# #### len()
# 
# len() é uma função que retorna o número de caracteres de uma string.

# In[ ]:


len(music)


# In[ ]:


another_music = 'Mood 4 eva'
len(another_music)


# #### Manipulando *strings*

# ##### Fatiamento de strings
# 
# Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):
# 
# >O operador [n:m] retorna a parte da string do “enésimo” caractere ao “emésimo” caractere, incluindo o primeiro, mas excluindo o último. Este comportamento é contraintuitivo, porém pode ajudar a imaginar os índices que indicam a parte entre os caracteres.

# In[ ]:


old_music = 'Crazy in love'


# In[ ]:


old_music[2:5]


# In[ ]:


old_music[:5] # se omitir o primeiro número, ele começa no início da string


# In[ ]:


old_music[3:] # se omitir o último número, a fatia vai até o final da string


# In[ ]:


old_music[3:3] # Se o primeiro índice for maior ou igual ao segundo, o resultado é uma string vazia, representada por duas aspas


# ##### Concatenando strings

# In[ ]:


nome = 'Beyoncé'
nome_completo = nome + ' ' + 'Knowles'
print(nome_completo)


# ##### Métodos de strings

# In[ ]:


# lower() converte todas as letras para minusculas
nome_completo = nome_completo.lower()
print(nome_completo)


# In[ ]:


# upper() converte todas as letras para maiusculas
nome_completo = nome_completo.upper()
print(nome_completo)


# In[ ]:


# replace - substitui uma string por outra
nome_completo = nome_completo.replace('KNOWLES', 'KNOWLES-CARTER')
print(nome_completo)


# In[ ]:


# split - divide uma string em várias strings
f_name, l_name = nome_completo.split(' ')
print(f_name)
print(l_name)


# In[ ]:


# find - encontra a posição de uma string dentro de outra
nome_completo.find('KNOWLES')


# In[ ]:


# rfind - encontra a posição de uma string dentro de outra, mas começa a busca pelo final
nome_completo.rfind('K')


# In[ ]:


# count - conta quantas vezes uma string aparece dentro de outra
nome_completo.count('E')


# In[ ]:


# strip - remove os espaços em branco no início e no final da string
movie = ' Lion King             '
movie.strip()


# #### Saiba mais sobre strings
# 
# [ABZ-Aaron](https://github.com/ABZ-Aaron) criou um repositório no Github com cheat sheets para os métdoso de strings. Lś você também encontra cheat sheets sobre listas e dicionários. 
# 
# Veja o [repositório](https://github.com/ABZ-Aaron/CheatSheets).

# ## Listas

# Allen Downey define uma lista em Python:
# 
# >Como uma string, uma lista é uma sequência de valores. Em uma string, os valores são caracteres; em uma lista, eles podem ser de qualquer tipo. Os valores em uma lista são chamados de elementos, ou, algumas vezes, de itens.
# 
# >Há várias formas para criar uma lista; a mais simples é colocar os elementos entre colchetes ([ e ])

# Listas são mutáveis. Podem conter elementos de qualquer tipo.

# In[ ]:


musics = ['Lemonade', 'Halo', 'Freedom','Flawless']
years = [2000, 2019, 2016, 2013]
empty = []
multi = ['singer', 1.70, ['jay-z', 'blue ivy']]


# In[ ]:


years[1] = 2016
years


# In[ ]:


len(musics)


# Índices de listas funcionam da mesma forma que os índices de strings

# ### Métodos de listas

# In[ ]:


# append - adiciona um elemento ao final de uma lista
musics.append('Formation')


# In[ ]:


# extend toma uma lista como argumento e adiciona todos os elementos
new_songs = ['Crazy in love', 'Hold up']
musics.extend(new_songs)
print(musics)


# In[ ]:


# sort - ordena uma lista
musics.sort()


# In[ ]:


musics.sort(reverse=True)


# In[ ]:


musics.append('Artpop')
print(musics)


# In[ ]:


#pop - remove um elemento da lista
musics.pop() # remove o ultimo elemento da lista
print(musics)


# In[ ]:


# del - remove um elemento da lista
del musics[0]


# In[ ]:


# remove - remove um elemento da lista
musics.remove('Halo')
print(musics)


# In[ ]:


# transformar uma lista em uma string
# join - separa os elementos da lista com o separador passado
str_musics = ', '.join(musics)
print(str_musics)


# ## Controle de fluxo
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# ### Tipos de controle de fluxo
# 
# 
# |Declaração|Significado|Condição de execução|
# |---|---|---|
# |`if`|se|se a condição for atendida|
# |`elif`|senão se|se nenhuma condição anterior for atendida *e* esta condição for atendida|
# |`else`|senão|se nenhuma condição for atendida (nenhuma condição é fornecida para uma instrução `else`)|
# |`while`|enquanto|enquanto a condição for verdadeira|
# |`for`|para|executar em um loop um quantidade de vezes|
# |`try`|tentar|tente isso e execute o código `except` se ocorrer um erro|

# ### Criando iterações for
# 
# É fundamental entender a estrutura de iteração, realizar um loop com python.
# 
# Iterar é a capacidade de executar um bloco de instruções repetidamente.

# In[ ]:


# utilizar for para percorrer a lista musics
for music in musics:
    length_music = len(music)
    print(f'A música é {music} e ela possui {length_music} letras.\n')


# In[ ]:


# utilizar range para percorrer um intervalo de valores
for i in range(0, len(musics)):
    print(f'A música é {musics[i]} e ela possui {len(musics[i])} letras.\n')
    


# In[ ]:


# create a list
list_names = []
# input the names of the students
for i in range(1,6):
    name = input(f'Digite o nome do estudante número {i}: ')
    list_names.append(name)
    


# In[ ]:


# loop na lista musics e salva cada item em um arquivo txt
for music in musics:
    # abre o arquivo txt
    file = open(music + '.txt', 'w') # w = write
    # escreve o valor usando format
    file.write(str(f'A música é {music} e ela possui {len(music)} letras.\n'))
    file.close() # fecha o arquivo


# ### while
# 
# Fluxo de execução para uma instrução while:
# 
# 1. Determine se a condição é verdadeira ou falsa.
# 
# 1. Se for falsa, saia da instrução while e continue a execução da próxima instrução.
# 
# 1. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

# In[ ]:


# criar uma lista de uma contagem de 10 até 0
import time
count = 10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Ok, Ladies, now let's get in formation!")


# ### if / elif / else
# 
# Operações condicionais

# In[ ]:


number = int(input('Digite um número: '))


# In[ ]:


if number > 0:
    print('positive')


# In[ ]:


if number < 0:
    print('negative')


# In[ ]:


if number == 0:
    print('zero')


# In[ ]:


if number > 0:
    print(f'o número {number} positivo')
else:
    print(f'o número {number} negativo')


# In[ ]:


if number > 0:
    print(f'o número {number} positivo')
elif number == 0:
    print(f'o número {number} é zero')
else:
    print(f'o número {number} negativo')


# ---
