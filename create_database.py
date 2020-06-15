import psycopg2
##PostgreSQL connection info
host = "ec2-34-197-141-7.compute-1.amazonaws.com"
user = 'audkmixtuelimp'
database = 'de6gjcsmcppa20'
port = '5432'
password = '086c94cd8048a4716013b374afa110e50c18474af145d87534d3917e0b515276'

##code that gets server info from heroku

##connects to postgreSQL server
conn = psycopg2.connect(host=host, database=database, user=user, password=password)

cur = conn.cursor()
cur.execute("CREATE TABLE users (userid BIGINT)")
conn.commit()
print("table created successfully")
cur.close()
conn.close()
