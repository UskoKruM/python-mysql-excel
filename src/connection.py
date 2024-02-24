import pymysql


def get_connection():
    try:
        return pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='gamesfsk'
        )
    except Exception as ex:
        print("Exception: {}".format(str(ex)))
