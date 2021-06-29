# imports
import requests
import pymysql
import json

def populate_database():  
    # api-endpoint
    URL = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1" 
    # sending get request and saving the response as response object
    r = requests.get(url = URL) #, params = PARAMS
    #print(r)
    # extracting data in json format
    data = r.json()

    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='SocialInc123',
                                    db='football_team')

        for value in data['items'] :
            name = value['name']
            position = value['position']
            nation = value['nation']['name']
            club = value['club']['name']
            x = {
            "name": name,
            "position": position,
            "nation": nation,
            "club" : club
            }
            cursor = connection.cursor()
            columns = ', '.join("`" + str(f).replace('/', '_') + "`" for f in x.keys())
            values = ', '.join("'" + str(f).replace('/', '_') + "'" for f in x.values())
            sql = "INSERT IGNORE INTO %s ( %s ) VALUES ( %s );" % ('team', columns, values)
            cursor.execute(sql)
            connection.commit()
            #print(sql)
    except ValueError as e:
        print(e)

    finally:
        # close the database connection using close() method.
        connection.close()
  


