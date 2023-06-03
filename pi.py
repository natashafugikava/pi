
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import pi
import streamlit as st
from matplotlib import image as mpimg

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv('Pokedex_Ver_SV2.csv').drop_duplicates(subset='Original_Name').reset_index(drop=True)
df = df[df['Generation']==1]

categorias = ['HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']
N = 6
angulos = [n / float(N) * 2 * pi for n in range(N)]
angulos.append(angulos[0])

st.header('Pokédex')

i = st.text_input('Digite o nome ou número do Pokémon', 'bulbasaur').title().replace('r M','r. M')
try:
  i = int(i)-1
except:
  i = int(df[df['Name']==i]['No'])-1

col1, col2 = st.columns(2)
col3, col4, col5= st.columns(1,1,2)

with col1:
  valores = df.loc[i][['HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']].values.tolist()
  valores.append(valores[0])
  ax = plt.subplot(111, polar=True)
  plt.xticks(angulos[:-1], categorias, color='grey', size=8)
  ax.set_rlabel_position(0)
  plt.yticks([64,128,192], ["64","128","192"], color="grey", size=7)
  plt.ylim(0,255)
  ax.plot(angulos, valores, linewidth=1, linestyle='solid')
  ax.fill(angulos, valores, 'b', alpha=0.1)
  plt.title(f'{df.at[i,"Original_Name"]}')
  st.pyplot(plt.show())
  
  st.bar_chart(df.loc[i][['HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']])

with col2:
  image = mpimg.imread(f"{df.at[i,'Name'].lower().replace('n ','n-').replace('r. ','r-')}.png")
  imgplot = plt.imshow(image)
  imgplot.axes.get_xaxis().set_visible(False)
  imgplot.axes.get_yaxis().set_visible(False)
  st.pyplot(plt.show())

  st.metric('Tipo 1', df.at[i,'Type1'])
  if not pd.isna(df.at[i,'Type2']):
    st.metric('Tipo 2', df.at[i,'Type2'])

with col3:
  st.metric('Altura', df.at[i,'Height'])
  st.metric('Peso', df.at[i,'Weight'])

with col4:
  st.metric('Macho', df.at[i,'Gender_Male'])
  st.metric('Fêmea', df.at[i,'Gender_Female'])
  st.metric('Desconhecido', df.at[i,'Gender_Unknown'])
  
with col5:
  st.metric('Habilidade 1', df.at[i,'Ability1'])
  if not pd.isna(df.at[i,'Ability2']):
   st.metric('Habilidade 2', df.at[i,'Ability2'])
  if not pd.isna(df.at[i,'Ability_Hidden']):
    st.metric('Habilidade oculta', df.at[i,'Ability_Hidden'])    
   

  

