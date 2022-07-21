from peewee import PostgresqlDatabase

postgres_db = PostgresqlDatabase(
    database="peewee_shop",
    user="myrzaiym",
    password="1",
    host="localhost",
    port="5432"
)