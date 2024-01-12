import psycopg2

class DatabaseStorage:
    def __init__(self, connection_string: str):
        self.connection = psycopg2.connect(connection_string)

    def store(self, url: str, content: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO crawled_data (url, content) VALUES (%s, %s)",
                (url, content)
            )
        self.connection.commit()