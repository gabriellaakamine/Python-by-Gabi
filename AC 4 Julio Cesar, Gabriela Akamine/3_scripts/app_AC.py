import streamlit as st
import pandas as pd
from datetime import date 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as srn

st.title('API AC 4')




dados = pd.read_csv('../1_bases_tratadas/base2.csv', sep=',', encoding='utf-8')



average = dados['net_worth'].mean()

fig = plt.figure(figsize=(10, 6))
srn.histplot(dados['Age'], bins=80,kde=True)
st.plotly_chart(fig)


fig2 = px.histogram( data_frame= dados.age)
st.plotly_chart(fig2)



fig3 = plt.figure(figsize=(10, 6))
dados3 = plt.scatter(x='age', y='net_worth', data=dados)
st.plotly_chart(fig3)

    
fig4 = px.pie(dados, names='industry', title='Gráfico de Pizza')
st.plotly_chart(fig4)