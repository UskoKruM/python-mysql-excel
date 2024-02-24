from src.connection import get_connection


class CreatorService():

    @classmethod
    def get_creators(cls):
        try:
            connection = get_connection()
            creators = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT lastname, firstname, birthdate, genre FROM creator;')
                resultset = cursor.fetchall()
                for row in resultset:
                    creators.append(row)
            connection.close()
            return creators
        except Exception as ex:
            print("Exception: {}".format(str(ex)))
