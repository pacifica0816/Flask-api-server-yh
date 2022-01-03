from flask import request
from flask_restful import Resource
from http import HTTPStatus

from mysql_connection import get_connection

# 클래스 작성 : 변수와 함수로 구성된 묶음
# 클래스는 상속이 가능하다!
# 아래 클래스는, flask_restful 라이브러리의
# Resource 클래스를 상속한 것이다.
class RecipeListResource(Resource) :
    pass