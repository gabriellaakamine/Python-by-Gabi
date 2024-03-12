import streamlit as st
import pandas as pd
from datetime import date 
import plotly.express as px

st.title('Furtos de celular em campinhas')

st.sidebar.header('Filtros')

dados = pd.read_csv('../1_bases_tratadas/base.csv')
dados.rename(columns={'quant_celular': 'Quantidade de celulares registrados por BO'}, inplace=True)
dados.rename(columns={'marca_celular': 'Marcas dos celulares'}, inplace=True)


lista_opcoes = ['Univariado', 'Bivariado']
escolha_tipo_analise = st.sidebar.selectbox('Escolha o tipo de analise', lista_opcoes)

if escolha_tipo_analise == 'Bivariado':
    fig = px.bar(data_frame=dados, x='Marcas dos celulares', y='Quantidade de celulares registrados por BO')
    st.plotly_chart(fig)
    st.markdown('Com a quantidade de celulares registrados nos BO´s, concluímos que a maioria foram da Samsung, seguido da motorola e outras marcas')
 

else:
    
    
    dadosesc = fig = px.pie(dados, names='solucao', values='qtdsolucao', title='Gráfico de Pizza')
    st.plotly_chart(fig)
    
    dadosesc2 = fig = px.pie(dados, names='peridoocorrencia', values='qtdperiodo', title='Gráfico de Pizza')
    st.plotly_chart(fig)
    
    