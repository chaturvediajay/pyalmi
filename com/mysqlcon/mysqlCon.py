import mysql.connector as connection
import pandas as pd
import json

class MySqlCon:
    def selectMysql():
        result_dataFrame = ''
        try:
            mydb = connection.connect(host="204.11.58.86", database='panicdis_upgrad', user="panicdis_admin",
                                      passwd="Madhu@1959", use_pure=True)
            query = "select * from advertising limit 9;"
            print(mydb.is_connected())
            result_dataFrame = pd.read_sql(query, mydb)
            result_dataFrame.head(10)
            # disconnect from server
            mydb.close()
        except Exception as e:
            mydb.close()
            print(str(e))
        return result_dataFrame




