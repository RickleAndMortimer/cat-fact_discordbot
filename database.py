import psycopg2
##PostgreSQL connection info
host = "localhost"
user = "postgres"
database = "cat_clients"
port = "5432"
password = "cupcakes29"
##connects to postgreSQL server
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
##SQL commands
#executes PostgreSQL commands
def __executeCommand(command):
    cur = conn.cursor() 
    return cur.execute(command)
#finds user in table
def __findUser(userID):
    if (__executeCommand("SELECT userID FROM users WHERE userID = {$0.userID};".format(userID):
        return true
    else:
        return false
#lists users in 
#deletes userID in the table
def deleteUser(userID):
    exists = __findUser(userID)
    if (exists):
        __executeCommand("DELETE FROM users WHERE userID = {$0.userID};".format(userID))
        return 1
    else:
        return -1
#adds userID into the table
def addUser(userID):
    exists = __findUser(userID)
    if (not exists):
        __executeCommand("INSERT INTO users (userID) VALUES ($0.userID);".format(userID))
        return 1
    else:
        return -1
#test
executeCommand(connect(host, user, database, port, password), "SELECT version()")
