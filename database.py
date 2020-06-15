import psycopg2
import os
##PostgreSQL connection info
host = os.environ['DB_HOST']
user = os.environ['DB_USER']
database = os.environ['DB_NAME']
port = os.environ['DB_PORT']
password = os.environ['DB_PASS']
##connects to postgreSQL server
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
##SQL commands
#executes SELECT commands
def __selectCommand(command):
    cur = conn.cursor()
    cur.execute(command)
    results = cur.fetchone()
    cur.close()
    return results
#executes commands that add/remove user ids
def __modifyCommand(command, userID):
    cur = conn.cursor()
    cur.execute(command, [userID])
    conn.commit()
    cur.close() 
#finds user in table
def __findUser(userID):
    results = __selectCommand("SELECT userid FROM users WHERE userid = {}".format(userID))
    if (results is None):
        return False
    else:
        return True
#lists users in table
def listUsers():
    cur = conn.cursor()
    cur.execute("SELECT userid FROM users")
    results = cur.fetchall()
    cur.close()
    return results
#deletes userID in the table
def deleteUser(userID):
    exists = __findUser(userID)
    if (exists):
        __modifyCommand("DELETE FROM users WHERE userid = %s", (userID))
        return 1
    else:
        return -1
#adds userID into the table
def addUser(userID):
    exists = __findUser(userID)
    if (not exists):
        __modifyCommand("INSERT INTO users (userid) VALUES (%s)", (userID))
        return 1
    else:
        return -1
