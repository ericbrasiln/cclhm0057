#!/usr/bin/env python
# coding: utf-8

# # Algoritmos, dataficação da sociedade e o ofício de Historiadores/as: desigualdade, racismo e violências
# 
# <small>Material para o Encontro Virtual 6, 14/12/2021, referente à [semana 10 do curso](https://ericbrasiln.github.io/intro-historia-digital/mod3/sem10.html#)</small>

# O objetivo desse encontro virtual é discutir a relação entre os algortimos e a dataficação da vida social com a pesquisa e ensino de história no presente e futuro.
# 
# Para tanto vamos discutir os seguintes textos:
# 
# 1. [O'NEIL, CATHY. Componentes da bomba. O que é um modelo? In: **Algoritmos de Destruição em massa**. São Paulo: Editora Rua do Sabão, 2020. pp. 25-50](https://github.com/ericbrasiln/intro-historia-digital/blob/bc111c29d3ec6f35221358f5c4af6edcebef524d/cclhm0069/biblio/oneil.pdf)
# 2. [NOBLE, Safiya Umoja. Introdução. In: **Algoritmos da opressão**. São Paulo: Editora Rua do Sabão, 2021. pp. 7-28](https://github.com/ericbrasiln/intro-historia-digital/blob/bc111c29d3ec6f35221358f5c4af6edcebef524d/cclhm0069/biblio/noble.pdf)

# ## E esse tal de _algoritmo_?
# 
# ![math](https://raw.githubusercontent.com/ericbrasiln/ferramentas_digitais_UNILAB/master/docs/gifs/math.gif)
# 

# Um conjunto de ações lógicas para realizar uma determinada tarefa. O algoritmo (escrito por um humano) informa ao computador que passos ele deve tomar e em que ordem isso deve ser feito.
# 
# Essa lista de procedimentos é executada passo a passo até completar a ação esperada.
# 
# Os passos lógicos são encadeados, por exemplo:
# 

# `Se` tal coisa acontecer, então faça o passo 1, `senão` faça o passo 2.
# 
# ~~~
# if
# else
# ~~~
# 

# `Enquanto` tal coisa estiver acontecendo, continue com a ação.
# 
# ~~~
# while == True
# ~~~
# 

# `Tente` executar esse passo, se não funcionar, realize a `exceção` tal.
# 
# ~~~
# try:
# except:
# ~~~
# 

# ![waze](https://raw.githubusercontent.com/ericbrasiln/ferramentas_digitais_UNILAB/master/docs/gifs/waze.gif)
# 

# ~~~
# se "o carro passar de 65 km/h":
#     mostrar alerta de velocidade
# senão:
#     não mostrar nada
# ~~~
# 
# Ou ainda:
# ~~~
# se "a rua estiver engarrafada":
#     "calcule nova rota mais curta por outra rua"
#     "mostre a nova rota"
#     "informe a direção"
# senão:
#     "manter a mesma rota"
# ~~~
# 

# In[ ]:


meu_nome = str(input('Qual é o seu nome? '))

if meu_nome == 'Eric':
    print('Que nome bonito!')
else:
    print('Seu nome é tão normal!')


# In[ ]:


idade = int(input('Qual a sua idade? '))

if idade < 16:
    print('Você é tão jovem. Ainda não pode votar!')
elif idade >= 16 and idade <18:
    print('Nessa idade você tem a opção de votar.Já tirou o título de eleitor?')
elif idade >= 18 and idade < 65:
    print('Na sua idade o voto é obrigatório!')
else:
    print('Nessa idade o voto é facultativo!')


# ## Algoritmos em tudo?
# 
# <div class="center">
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Trying a horrible experiment...<br><br>Which will the Twitter algorithm pick: Mitch McConnell or Barack Obama? <a href="https://t.co/bR1GRyCkia">pic.twitter.com/bR1GRyCkia</a></p>&mdash; Tony “Abolish (Pol)ICE” Arcieri 🦀 (@bascule) <a href="https://twitter.com/bascule/status/1307440596668182528?ref_src=twsrc%5Etfw">September 19, 2020</a></blockquote>
# <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# </div>

# ![tweet](https://github.com/ericbrasiln/intro-historia-digital/blob/945a2f6528af55f0f18c59e57afcfb93566e464a/cclhm0069/images/tweet_race.jpeg?raw=true)

# ## Dataficação das relações sociais

# Quais impactos para a pesquisa histórica?

# ## A opressão dos algoritmos - Debate dos textos

# ### Cathy O'Neil e os componentes da bomba
# 
# #### O que é um modelo?
# 
# - O que é um modelo?
# - O exemplo do beisebol
# - O exemplo da alimentação de uma família (31-33)
# - Modelo é uma simplificação (33-35)
# - Sucesso? (35)
# - Racismo como modelo? (37)
# - Modelos de Reincidência e o sistema penitenciário e judiciário nos EUA (40 - 44)
#   - Retroalimentação (44)  

# #### Taxonomia de ADM (Algoritmos de Destruição em Massa)
# 
# 1. O modelo é opaco ou invisível?
# 2. É injusto? Destrói vidas?
# 3. Ganha escala?
# 
# OPACIDADE + ESCALA + DANO = ADM

# ### Noble e a opressão dos algoritmos

# - Objetivos do livro: acadêmico e político
# - O caso das "meninas negras" no Google
# - "Racismo é a API fundamental da internet" (14)

# #### Google Search
# 
# - Empresa de publicidade;
# - Implicações das tomadas de decisões algoritmicas (15);
# - São erros? 
# - Quais impactos dos vieses racistas e sexistas nesses algoritmos para a sociedade?
