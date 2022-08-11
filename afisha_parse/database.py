import psycopg2

database = psycopg2.connect(
    database='cinema_events',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cinema_events(
    event_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_name TEXT,
    event_days TEXT,
    event_link TEXT

)
''')

database.commit()
database.close()