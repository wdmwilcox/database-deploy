import pyodbc
import os
import logging

logging.basicConfig(filename='database-deploy.log', level=logging.INFO)

BASE_DIR = os.getcwd()
deploy_path = os.path.join(BASE_DIR, 'deploy')
revert_path = os.path.join(BASE_DIR, 'revert')

logging.info(f'connection is {connection}')

def deploy_script(script, database=None):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=' + database + ';UID=PythonService;PWD=PythonService')
    if 'database' in script:
        connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(script)
    if connection.autocommit == False:
        connection.commit()
    return None

def main():
    for root, directories, files in os.walk(deploy_path):
        for file in files:
            logging.info(f'file is {file}')
            with open(root + '\\' + file, 'r') as file:
                logging.info(f'file is {file}')
                script = file.read()
                if 'database' in script:
                    deploy_script(script, database='master')
                else:
                    deploy_script(script, database='test_db')

if __name__ == '__main__':
    main()
