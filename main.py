import streamlit as st

import page.insert as insert
import page.select as select

st.header('Sistema CRUD Básico')
st.sidebar.title('Menu')
selectbox = st.sidebar.selectbox('Cadastrar', ['Funcionário', 'Paciente'])

selectbox2 = st.sidebar.selectbox('Usuarios', ['Exibir todos'])

if selectbox == 'Funcionário':
    insert.inserir_funcionario()
if selectbox == 'Paciente':
    insert.inserir_paciente()

if selectbox2 == 'Exibir todos':
    select.exibir_dados()

    

