import psycopg2

while True:
    get_event = input('Если хотите увидеть список событий, введите "start": ')
    if get_event.lower() == 'stop':
        break
    try:
        data = 'https://www.afisha.uz/ru/cinema'.info()

        event_name = data['div'][0]['h4']
        event_days = data['div'][0]['mt4']
        event_link = data['div'][0]['href']
        print(f"""Не забудьте посетить {event_name} {event_days}!
Подробнее: {event_link}""")

    database = psycopg2.connect(
        database='cinema_events',
        host='localhost',
        user='postgres',
        password='123456'
    )

    cursor = database.cursor()

    cursor.execute('''
            INSERT INTO cinema_events(event_name, event_days, event_link)
            VALUES (%s, %s, %s)
            ''', (event_name, event_days, event_link))
    database.commit()
    database.close()







