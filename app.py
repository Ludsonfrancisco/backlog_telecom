import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path

st.set_page_config(
    layout='wide'
)

pasta = Path('datasets')
item = os.listdir(pasta)
caminho = (f'{pasta}/{item[0]}')

df_producao = pd.read_csv(
     caminho,
     sep='|', 
     decimal=',',
     encoding='latin1')

df_producao_filtrado = df_producao.loc[
    (df_producao['ARMARIO']  != 'ESSEA_G1I02') &
    (df_producao['ARMARIO']  != 'ESSEA_G1M10') &
    (df_producao['ARMARIO']  != 'ESSEA_G1M11') &
    (df_producao['ARMARIO']  != 'ESSEA_G1M03') &
    (df_producao['ARMARIO']  != 'ESSEA_G1N08') &
    (df_producao['ARMARIO']  != 'ESSEA_G1N06') &
    (df_producao['ARMARIO']  != 'ESSEA_G1N09') ]

df_producao_filtrado = df_producao_filtrado[~df_producao_filtrado['DETAIL'].str.startswith('PREV')]

col_status = df_producao_filtrado['STATUS_REASON'].unique()
status_selecionado = st.sidebar.multiselect('Selecione um status', col_status, col_status)
df_status_filtro1 = df_producao_filtrado[df_producao_filtrado['STATUS_REASON'].isin(status_selecionado)]


col_tecnologia = df_producao_filtrado['PHYSICAL_LINK_MEDIA_TYPE'].unique()
status_tecnologia = st.sidebar.selectbox('Selecione uma Tecnologia', col_tecnologia, index=0)
df_tecnoligia_filtro2 = df_status_filtro1[df_status_filtro1['PHYSICAL_LINK_MEDIA_TYPE'] == status_tecnologia]

col_preventiva = df_tecnoligia_filtro2['DETAIL'].unique()




col1, col2, col3 = st.columns(3)



soma_da_coluna = df_tecnoligia_filtro2['CITY'].value_counts().sum()
col2.subheader(f'{soma_da_coluna} - BACKLOG GERAL')

fig = px.bar(df_tecnoligia_filtro2['CITY'].value_counts().sort_index(),text='value')
st.plotly_chart(fig)


