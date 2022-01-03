from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection
from mysql.connector.errors import Error

# 클래스 작성 : 변수와 함수로 구성된 묶음 
# 클래스는 상속이 가능하다!
# 아래 클래스는, flask_restful 라이브러리의
# Resource 클래스를 상속한 것이다.
class RecipeListResource(Resource) :
    def get(self):
        # 클라이언트가 GET 요청하면, 이 함수에서
        # 우리가 코드를 작성해 주면 된다.

        # 1. db 접속recipe 테이블에서 select 
        try :
            connection = get_connection()

            query = ''' select * 
                        from recipe ; '''
            
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            ### 중요. 파이썬의 시간은, JSON으로 보내기 위해서
            ### 문자열로 바꿔준다.
            i = 0
            for record in record_list:
                record_list[i]['created_at'] = record['created_at'].isoformat()
                record_list[i]['updated_at'] = record['updated_at'].isoformat()

            
        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            print('Error while connecting to MySQL', e)
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            print('finally')
            cursor.close()
            if connection.is_connected():
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')


        return {'data' :record_list} , HTTPStatus.OK