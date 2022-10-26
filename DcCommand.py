import sqlite3 as lite

conn = lite.connect('D:\SmartAgro\database\dados.db')

# with conn:
#     cur = conn.cursor()
#     query = "CREATE TABLE tb_emissao_veiculo(cd_ems_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,tipo_veiculo TEXT,distancia_perc FLOAT,tipo_motor TEXT,combustivel TEXT,total_emissao FLOAT,total_compensa FLOAT)"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     query = "DROP TABLE tb_emissao_veiculo"
#     cur.execute(query)

# with conn:
#     cur = conn.cursor()
#     query = "INSERT INTO tb_emissao_veiculo(tipo_veiculo,distancia_perc,tipo_motor,combustivel,total_emissao,total_compensa)VALUES('Carro',400,'1.6(16V)','Diesel',135,9)"
#     cur.execute(query)

with conn:
    cur = conn.cursor()
    #query = "SELECT SUM(total_compensa) FROM tb_emissao_veiculo;"
    query = "SELECT tipo_veiculo,total_emissao,total_compensa FROM tb_emissao_veiculo;"
    cur.execute(query)

    info = cur.fetchall()
    print(info)