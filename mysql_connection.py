import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.ce8mtmot71ct.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_user',
        password = '1234'
    )
    return connection
    