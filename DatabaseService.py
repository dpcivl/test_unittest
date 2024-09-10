class DatabaseService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save_data(self, data):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO data_table (data) VALUES (%s)", (data,))
        self.db_connection.commit()
        return True

    def get_data(self, data_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT data FROM data_table WHERE id = %s", (data_id,))
        result = cursor.fetchone()
        return result[0] if result else None
