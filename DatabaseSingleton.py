from mysql.connector import pooling
import json

class DatabaseSingleton:
    conn = None

    def __new__(cls):
        if not cls.conn:
            cls.new_conn()
        connection = cls.conn.get_connection()
        return connection

    @classmethod
    def new_conn(cls):
        connection = pooling.MySQLConnectionPool(
            pool_name="Connection_pool",
            pool_size=10,
            host=cls.readconfig("host"),
            port=cls.readconfig("port"),
            user=cls.readconfig("user"),
            password=cls.readconfig("password"),
            database=cls.readconfig("database"),
        )
        cls.conn = connection

    @classmethod
    def readconfig(cls, key):
        with open("./Cinema/appconfig.json", "r") as f:
            config = json.load(f)
            return config["database"][key]