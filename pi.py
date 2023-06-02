
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import pi
import streamlit as st

df = pd.read_csv('Pokedex_Ver_SV2.csv').drop_duplicates(subset='Original_Name').reset_index(drop=True)

categorias = ['HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']
N = 6
angulos = [n / float(N) * 2 * pi for n in range(N)]
angulos.append(angulos[0])

st.header('Pokédex')

i=1

col1, col2 = st.columns(2)
with col1:
  valores = df.loc[i][['HP', 'Attack', 'Defense', 'SP_Attack', 'SP_Defense', 'Speed']].values.tolist()
  valores.append(valores[0])
  fig, ax = plt.subplot(111, polar=True)
  plt.xticks(angulos[:-1], categorias, color='grey', size=8)
  ax.set_rlabel_position(0)
  plt.yticks([64,128,192], ["64","128","192"], color="grey", size=7)
  plt.ylim(0,255)
  ax.plot(angulos, valores, linewidth=1, linestyle='solid')
  ax.fill(angulos, valores, 'b', alpha=0.1)
  plt.title(f'{df.at[i,"Original_Name"]}')
  st.pyplot(fig)

  

  

