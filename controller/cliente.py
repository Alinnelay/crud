#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir_funcionario(email, senha, cpf, nome, telefone, idade, cargos):
    db.cur.execute("""
                   INSERT into tbusuarios (email, senha, CPF)
                   VALUES ('%s','%s','%d')
                   """ % (email, senha, cpf))
    db.cur.execute("""
                  SELECT id_user FROM tbusuarios
                  WHERE CPF = ('%d')
                  """ %(cpf))
    id_user = db.cur.fetchall()
    id = id_user[0]
    id_funcionario = id[0]

    db.cur.execute("""
                  INSERT into tbfuncionarios (id_funcionario, nome, telefone, idade, cargo)
                   VALUES ('%d', '%s','%d','%d', '%s')
                   """ % (id_funcionario, nome, telefone, idade, cargos))         
    db.con.commit()

def incluir_paciente(email, senha, cpf, nome, telefone, idade):
    db.cur.execute("""
                   INSERT into tbusuarios (email, senha, CPF)
                   VALUES ('%s','%s','%d')
                   """ % (email, senha, cpf))
    db.cur.execute("""
                  SELECT id_user FROM tbusuarios
                  WHERE CPF = ('%d')
                  """ %(cpf))
    id_user = db.cur.fetchall()
    id = id_user[0]
    id_paciente = id[0]

    db.cur.execute("""
                  INSERT into public.tbpacientes (id_paciente, nome, telefone, idade)
                   VALUES ('%d', '%s','%d','%d')
                   """ % (id_paciente, nome, telefone, idade))         
    db.con.commit()
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbusuarios
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

# função para selecionar apenas um registros no banco de dados
def selecionar_id (id):
  db.cur.execute("""
           SELECT * FROM tbusuarios WHERE id = '%s'
   """ % (id))
  recset = db.cur.fetchall()
  rows = []
  for rec in recset:
    rows.append(rec)
  return rows

# função para excluir registros no banco de dados
def excluir (id):
  db.cur.execute("""
                  DELETE FROM tbfuncionarios WHERE id_funcionario = '%s'
                  """ % (id))
  db.cur.execute("""
                  DELETE FROM tbpacientes WHERE id_paciente = '%s'
                  """ % (id))
  db.cur.execute("""
           DELETE FROM tbusuarios WHERE id_user = '%s'
   """ % (id))
  data = db.con.commit()
  return data
