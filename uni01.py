#!/usr/bin/env python
# coding: utf-8

# # Case 1: Empresas Unicórnio

# In[205]:


# Importando Biblioteca

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings 
warnings.filterwarnings('ignore')


# In[206]:


# Importando Dados

Base_Dados = pd.read_csv('Dados/Startups in 2021 end.csv')

# Verificar Dimensões 

Base_Dados.shape


# In[207]:


# Primeiros Registros

Base_Dados.head()


# In[208]:


# Verificar Colunas existentes
Base_Dados.columns


# In[209]:


# Renomear as Colunas
Base_Dados.rename(columns={
    'Unnamed: 0' : 'ID',
    'Company' : 'Empresa', 
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'País',
    'City' : 'Cidade',
    'Industry' : 'Setor',
    'Select Investors' : 'Investidores',
}, inplace = True)


# In[210]:


# Verificar o tipo da informação

Base_Dados.info()


# In[211]:


# Verificando os campos nulos
Base_Dados.isnull().sum()


# In[212]:


# Verificando campos únicos
Base_Dados.nunique()


# In[213]:


# Valores únicos - Coluna Setor - Rank
Base_Dados['Setor'].value_counts()


# In[214]:


# Valores únicos (%) - Coluna Setor - Rank
Setor = round( Base_Dados['Setor'].value_counts( normalize=True) *100,1)
Setor


# In[215]:


plt.figure( figsize=(15,6) )
plt.title('Analise dos Setores')
plt.bar( Base_Dados['Setor'].value_counts().index, Base_Dados['Setor'].value_counts() )
plt.xticks( rotation=45, ha='right' );


# In[216]:


# Valores únicos - Coluna País - Rank
Base_Dados['País'].value_counts()


# In[217]:


# Valores únicos (%) - Coluna Setor - Rank
Analise = round(Base_Dados['País'].value_counts( normalize=True)*100,1)


# In[218]:


Analise


# In[219]:


# Plot geral dos Países (Top 10)
plt.figure( figsize=(20,35) )
plt.title('Analise dos Países geradores de Unicórnios - Top 10')
plt.pie(
    Analise.head(10),
    labels = Analise.index[0:10],
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
    
);


# In[220]:


# Conversão para Data (Pandas)
Base_Dados['Data de Adesão'] = pd.to_datetime( Base_Dados['Data de Adesão'])
Base_Dados['Data de Adesão'].head()


# In[221]:


# Extrair: Ano e o Mês
Base_Dados['Mes'] = pd.DatetimeIndex( Base_Dados['Data de Adesão']).month
Base_Dados['Ano'] = pd.DatetimeIndex( Base_Dados['Data de Adesão']).year


# In[222]:


Base_Dados.head()


# In[223]:


# Tabela Analítica
Analise_Agrupada = Base_Dados.groupby(by=['País', 'Ano', 'Mes', 'Empresa']).count()['ID'].reset_index()
Analise_Agrupada


# In[224]:


# Localizando o Brasil no Rank
Analise_Agrupada.loc[
    Analise_Agrupada['País'] == 'Brazil'
]


# In[225]:


# Transformando a coluna valor
pd.to_numeric( Base_Dados['Valor ($)'].apply( lambda Linha: Linha.replace('$','')))

Base_Dados.head()


# In[237]:


# Tabela Analítica
Analise_Pais = Base_Dados.groupby(by= ['País','Setor', 'Valor ($)']).sum(['País']).reset_index()
Analise_Pais.head(10)


# In[265]:


Analise_Valor = Analise_Pais.sort_values(by =('Valor ($)'),ascending=False)
Analise_Valor.head(10)


# In[281]:


plt.figure( figsize=(40,20))
plt.plot( Analise_Valor['Valor ($)'], Analise_Valor['País'])
plt.title('Analise do Valor por País')
plt.xticks(rotation=45, ha='right');


# In[ ]:




