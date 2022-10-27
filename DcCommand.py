import sqlite3 as lite

conn = lite.connect('D:\SmartAgro\database\dados.db')

# with conn:
#     cur = conn.cursor()
#     query = "CREATE TABLE tb_emissao_veiculo(cd_ems_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,tipo_veiculo TEXT,distancia_perc FLOAT,tipo_motor TEXT, combustivel TEXT, total_emissao FLOAT, total_compensa FLOAT)"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     query = "DROP TABLE tb_emissao_veiculo"
#     cur.execute(query)

# ===========================================================================================================
# Comandos banco de dados tabela fazenda
def ver_tabela_fazenda():
    ver_dados = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM tb_emissao_fazenda;"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

def inserir_dados_fazenda(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO tb_emissao_fazenda(nm_local,tipo_consumo,valor,qtd_mes,total_emissao)VALUES(?,?,?,?,?)"
        cur.execute(query,i)

# ===========================================================================================================
# Comandos banco de dados tabela veiculos
def ver_tabela_veiculo():
    ver_dados = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM tb_emissao_veiculo;"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

def inserir_dados_veiculo(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO tb_emissao_veiculo(tipo_veiculo,distancia_perc,tipo_motor, combustivel, total_emissao, total_compensa)VALUES(?,?,?,?,?,?)"
        cur.execute(query,i)

# ===========================================================================================================
# Comandos banco de dados tabela fertilizante

# with conn:
#     cur = conn.cursor()
#     query = "SELECT * FROM tb_emissao_fazenda;"
#     cur.execute(query)


# with conn:
#     cur = conn.cursor()
#     query = "CREATE TABLE tb_emissao_fazenda(cd_ems_fazenda INTEGER PRIMARY KEY AUTOINCREMENT,nm_local TEXT,tipo_consumo TEXT,valor FLOAT,qtd_mes FLOAT,total_emissao FLOAT)"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     query = "DROP TABLE tb_emissao_veiculo"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     query = "INSERT INTO tb_emissao_veiculo(tipo_veiculo,distancia_perc,tipo_motor,combustivel,total_emissao,total_compensa)VALUES('Carro',400,'1.6(16V)','Diesel',135,9)"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     #query = "SELECT SUM(total_compensa) FROM tb_emissao_veiculo;"
#     query = "SELECT tipo_veiculo,total_emissao,total_compensa FROM tb_emissao_veiculo;"
#     cur.execute(query)

#     info = cur.fetchall()
#     print(info)