import mysql.connector
from mysql.connector import Error

import env as v

def query(query):
    results = []
    try:
        con = mysql.connector.connect(host=v.DB_HOST, database=v.DB_DATABASE, user=v.DB_USER, password=v.DB_PASS)
        cursor = con.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

    if con.is_connected():
        con.close()
        cursor.close()
    return results

def execute_query(execute):
    con = mysql.connector.connect(host=v.DB_HOST, database=v.DB_DATABASE, user=v.DB_USER, password=v.DB_PASS)
    cursor = con.cursor()
    try:
        cursor.execute(execute)
        con.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def get_job_db(NOME_JOB):
    return query(f'''SELECT * FROM ctrl_jenkins_jobs 
        WHERE nome_job = '{NOME_JOB}'
    ''')

def insert_repo_db(NOME_JOB, ID = v.ID_JENKINS):
    query = f'''INSERT INTO ctrl_jenkins_jobs 
        (nome_job, jenkins) VALUES 
        ('{NOME_JOB}', '{ID}')
    '''
    print("Executando => ")
    print(query)
    return execute_query(query)

def desable_job(ID):
    query = f'''UPDATE ctrl_jenkins_jobs j 
    SET j.ativo = 'N' WHERE j.id_job = {ID}'''

    print("Executando => ")
    print(query)
    return execute_query(query)