import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "nighty32",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres") # these could all be in a separate module as CONST values

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    #cursor.execute("SELECT version();")

    """Run the query and fetch records"""
    cursor.execute("SELECT url,username,password FROM automation_data;")
    #record = cursor.fetchone()
    record = cursor.fetchall()
    #print record
    #print (record[0])
    print (record[1])

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")