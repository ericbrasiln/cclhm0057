#!/usr/bin/env python
# coding: utf-8

# # Passado, futuro e presente do digital na História: Fontes, método e análise
# 
# <small>Material para o Encontro Virtual 2, 03/11/2021</small>

# Nessa aula vamos debater acerca dos elementos constitutivos da disciplina História e sua relação com as transformações e continuidades na era digital.
# 
# Buscamos avaliar o papel dos profissionais da História diante da sociedade contemporânea, assim como refletir sobre as mudanças de percepção do tempo e como isso pode afetar as formas de analisar e entender o passado e impactar nas formas de ensinar e narrar a História.

# ## O historiador do futuro ou será programador ou não será?

# <img src="https://media4.giphy.com/media/Xch9I90tRezyicQgma/giphy.gif?cid=790b7611917058ce2d4fba49c611758a9bd0f87a2ea36267&rid=giphy.gif&ct=g" alt="wall-e" style="zoom:100%;" />

# FORTES, A.; ALVIM, L. G. M. Evidências, códigos e classificações: o ofício do historiador e o mundo digital. *Esboços: histórias em contextos globais*, v. 27, n. 45, p. 207–227, 19 jun. 2020. 
# 
# ### Ofício do Históriador/a 

# #### Marc Bloch (2001) e E. P. Thompson (1981)
# 
# 1. Conhecimento histórico => análise de fontes, validado pelo diálogo com a realidade, voltado para orientação da ação humana no presete (210)
# 2. Fontes sçao epistemologicamente transformadas em conhecimento histórico pela formulação de problçemas (Bloch) e perguntas que interrogam as evidências (Thompson)
# 

# #### Questões centrais da virada digital na História
# 
# 1. AMpliação de fontes + ferramentas que auxiliam em análises 'de qualidade superior'
# 2. Qual contribuição do ofício dp historiador/a para o enfrentamento dos dilemas da sociedade contemporânea marcada por Big Data, Fake news e Inteligência Artificial

# ### Codificar e classificar
# 
# > De que modo as operações congnitivas referentes à linguagem realizadas pelo historiador são afetadas pelo desenvolvimento da tecnologia digital? (212)

# #### Processamento de Linguagem Natural (*NLP*)
# 
# Computadores "lendo" e "entendendo" linguagem humana.

# ### Produção de conhecimento histórico e a relevância na era Digital
# 
# Instrumentos do historiodor/a - manipular evidências, transformar em 'informações racionalmente classificadas', escrever narrativas: é ao mesmo tempo método e técnica, mas também sensibilidade, 'intuição alta' (nas palavras de Ginzburg)
# 
# > Chegarão as máquinas a desenvolver esse tipo de “alta intuição”? Em que tipo de operação cognitiva a inteligência artificial já pode, hoje em dia, auxiliar a pesquisa histórica? (215)

# #### Possibilidades e caminhos: Inteligência Articifial, Processamento de Linguagem Natural e mais...
# 
# - Análise textual (gramática, semântica, lexicográfica, etc.)
# - NER (Name Entity Recognition) - Nomes, entidades, etc.
# - Topic modeling - Modelagem de tópicos
# - Reconhecimento de Layout
# - Análise de redes
# - Georeferenciamento

# ### Um rápido exemplo: Python e spaCy para "ler" Helena de Machado de Assis

# > Esses exemplos foram inspirados pelo material produzido por Melanie Walsh em  seu curso ["Introduction to cultural analytics & Python"](https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/Multilingual/Portuguese/00-Portuguese.html).

# In[ ]:


# Instalando spacy
get_ipython().system('pip install spacy')


# In[1]:


# importando spacy para ser usado no Python
import spacy


# In[5]:


# lendo o arquivo de texto
corpus = open('umhomemclebre.txt', 'r').read()
# carregando o modelo de linguagem
nlp = spacy.load('pt_core_news_lg')
# processando o texto
doc = nlp(corpus)


# #### Analisando as entidades do texto

# In[6]:


# para cada entidade até 20 tokens
for named_entity in doc.ents[:20]:
    # imprimindo o nome da entidade
    print(named_entity.text, named_entity.label_)


# In[7]:


spacy.displacy.render(doc,style='ent') # renderizando a entidade


# #### Analisando os `tokens`do texto

# In[8]:


# importando tokens
from spacy import tokens 


# In[9]:


# transformando em tokens
tokens = [token.orth_ for token in doc] # token.orth_ = token.text


# ##### Classes gramaticais

# In[10]:


classes = [(token.orth_, token.pos_) for token in doc] # part of speech = classes gramaticais
print(f'Classes no corpus: {classes[:50]}')


# ##### Morfologia

# In[11]:


morfologicas = [(token.orth_, token.morph) for token in doc] # morfologia de cada token
print(f'Morfologias: {morfologicas[:50]}')


# ##### Verbos

# In[12]:


lemma_tokens = [token.lemma_ for token in doc if token.pos_ == 'VERB'] # reduz a palavra para o lema, nesse caso, apenas os verbos
print(f'Verbos no corpus: {lemma_tokens[:50]}')


# ##### Apenas tokens alfabéticos

# In[13]:


alpha_tokens = [token.orth_ for token in doc if token.is_alpha]
print(f'Tokens alfa: {alpha_tokens[:50]}')


# ##### Seperar o texto em pedaços e analisar cada um

# In[14]:


# criar grupos de tokens
import math
number_of_chunks = 80  # numero de grupos

chunk_size = math.ceil(len(corpus) / number_of_chunks) # tamanho de cada grupo

text_chunks = [] # lista de grupos

for number in range(0, len(corpus), chunk_size): # para cada grupo
    text_chunk = corpus[number:number+chunk_size]
    text_chunks.append(text_chunk) 


# In[15]:


chunked_documents = list(nlp.pipe(text_chunks)) # processando cada grupo


# In[16]:


import pandas as pd # para criar um dataframe
from collections import Counter # para contar o numero de tokens por grupo


# In[17]:


# criando um dataframe com PESSOAS
people = []

for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "PER":
            people.append(named_entity.text)

people_tally = Counter(people)

df = pd.DataFrame(people_tally.most_common(), columns=['character', 'count'])
df


# In[18]:


# criando um dataframe com LOCAIS
places = []
for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "LOC":
            places.append(named_entity.text)

places_tally = Counter(places)

df = pd.DataFrame(places_tally.most_common(), columns=['place', 'count'])
df


# #### Analisar tokens em seu contexto

# In[19]:


# contexto
from IPython.display import Markdown, display
import re

def get_ner_in_context(keyword, document, desired_ner_labels= False):
    
    if desired_ner_labels != False:
        desired_ner_labels = desired_ner_labels
    else:
        desired_ner_labels = ['PER', 'ORG', 'LOC']  
        
    #Iterate through all the sentences in the document and pull out the text of each sentence
    for sentence in document.sents:
        #process each sentence
        sentence_doc = nlp(sentence.text)
        for named_entity in sentence_doc.ents:
            #Check to see if the keyword is in the sentence (and ignore capitalization by making both lowercase)
            if keyword.lower() in named_entity.text.lower()  and named_entity.label_ in desired_ner_labels:
                #Use the regex library to replace linebreaks and to make the keyword bolded, again ignoring capitalization
                #sentence_text = sentence.text
            
                sentence_text = re.sub('\n', ' ', sentence.text)
                sentence_text = re.sub(f"{named_entity.text}", f"**{named_entity.text}**", sentence_text, flags=re.IGNORECASE)

                display(Markdown('---'))
                display(Markdown(f"**{named_entity.label_}**"))
                display(Markdown(sentence_text))


# In[21]:


for document in chunked_documents:
    get_ner_in_context('Mozart', document)


# In[22]:


for document in chunked_documents:
    get_ner_in_context('Maria', document)


# #### O que dá pra fazer com isso?

# ### Big Data terá um impacto revolucionário na base epistemológica da História?
# 
# * Voltaremos a uma história quantitativa?
# * Voltaremos a uma hegemonia das fontes escritas?
# * Ou não muda nada?
# 
# > Digital approaches to the past that sit within the digital humanities use our computational power to force us to look at the materials differently, to think about them playfully, and to explore what these sometimes jarring deformations could mean. (34)

# ## Temporalidade e tecnologia digital
# 
# > Não lembro nem o que comi ontem...

# ### Ler, escrever e representar o passado: o que muda com a era digital?
# 
# 1. Temporalidade: "constitutivo e estruturados do conheciumento histórico" (159)
#    * como entender historicidade quando a orientação temporal é abalada no presente? (160)
# 2. Presente: "o tempo-espaço no qual se ministram as tensões e se fazem a gestão e o equacionamento entre passado e futuro: é o espaço das demandas e da onde emergem questões políticas que nos interpelam."
#    * Que outros 'espaços de experiência' e 'horizontes de expectativa' a tecnologia possibilita construir? (160)
# 3. Uso e problematização da tecnologia: descentralização da concepção de História como progresso linear.
