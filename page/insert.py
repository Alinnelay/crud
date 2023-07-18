import streamlit as st

import controller.cliente as cliente

def inserir_funcionario():
    st.title('Cadastrar Funcionario')
    cargos = ['Recepcionista', 'Dentista', 'Faxineira', 'Auxiliar de dentista']
    
    with st.form(key='insert_funcionario'):
    
        input_email = st.text_input(label='Email:')
        input_senha = st.text_input(label='Senha:')
        input_cpf = st.number_input(label='Cpf:', format='%d', step=1)
        input_nome = st.text_input(label='Nome:')
        input_telefone = st.number_input(label='Telefone:', format='%d', step=1)
        input_idade  = st.number_input(label='Idade:', format='%d', step=1)
        input_cargo = st.selectbox(label='Cargo', options=cargos)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir_funcionario(input_email, input_senha, input_cpf, input_nome, input_telefone, input_idade, input_cargo)
            st.success('Funcionario incluido com sucesso') 

        
def inserir_paciente():
    st.title('Cadastrar Paciente')

    
    with st.form(key='insert_paciente'):
        input_email = st.text_input(label='Insira o email:')
        input_senha = st.text_input(label='Insira a senha:')
        input_cpf = st.number_input(label='Insira o cpf:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome:')
        input_telefone = st.number_input(label='Insira o telefone:', format='%d', step=1)
        input_idade  = st.number_input(label='Insira a idade:', format='%d', step=1)


        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir_paciente(input_email, input_senha, input_cpf, input_nome, input_telefone, input_idade)
            st.success('Paciente incluido com sucesso') 

