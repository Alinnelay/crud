import streamlit as st

import controller.cliente as cliente

def exibir_dados():
    st.title('Consultar Dados')
    colunas = st.columns((1,2,1,2,1))
    campos = ['Id_user', 'EMAIL', 'SENHA', 'CPF', 'Excluir']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5 = st.columns((1,2,1,2,1))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        button_excluir = col5.empty()
        on_click_excluir = button_excluir.button('x', 'btnExcluir' + str(item[0]))
        
        if on_click_excluir:
            cliente.excluir(item[0])
            