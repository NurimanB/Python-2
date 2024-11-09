import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='qwerty',
    client_encoding='UTF8' 
)


def adding(id, username, password):
    current = config.cursor()  

    sql = '''
        INSERT INTO users (id, username, password)
        VALUES (%s, %s, %s);
    '''
    current.execute(sql, (id, username, password))  
    current.close()  
    config.commit()  
    config.close()  

print("ID:")
id = int(input())
print("Name:")
username = input()
print('Password:')
password = input()

adding(id, username, password)
