from flask import Flask, send_file, render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

import json
import requests


import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

import mysql.connector as connection
import pandas as pd

from com.mysqlcon import mysqlCon

fig, ax = plt.subplots(figsize=(6, 6))
ax = sns.set_style(style="darkgrid")

x = [i for i in range(100)]
y = [i for i in range(100)]

mysql_status = ''

app = Flask(__name__)


@app.route('/')
def home():
    list_test = mysqlCon.MySqlCon.selectMysql()
    data1 = {'userName': 'admin123', 'userPassword': 'admin@pass'}
    headers = {'Content-type': 'application/json'}
    response = requests.post('https://jwtauthenicate.herokuapp.com/api/auth/authenticate', json.dumps(data1), headers=headers)
    res = ''
    if response.status_code == 200:
        print('response Code ' + str(response.status_code))
        sampl = json.loads(response.text)
        headers = {'Authorization': 'Bearer ' + sampl["jwtToken"], "Content-Type": "text/html"}
        payload = {}
        response = requests.get('https://jwtauthenicate.herokuapp.com/api/auth/forAdmin', headers=headers, data=payload)
        print(44)
        print(response.text)
        if response.status_code == 200:
            res = str(response.text)

    return render_template('index.html', values=list_test,
                           prediction_text='Employee Salary should be  ' + res)
    # return render_template('index.html')


@app.route('/visualize')
def visualize():
    sns.lineplot(x=x, y=y)
    canvas = FigureCanvas(fig)
    plt.xlabel('salary')
    plt.ylabel('age')
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')


if __name__ == "__main__":
    app.run(debug=True)


def selectMysql():
    result_dataFrame = ''
    # try:
    #     mydb = connection.connect(host="204.11.58.86", database='panicdis_upgrad', user="panicdis_admin",
    #                               passwd="Madhu@1959", use_pure=True)
    #     query = "select * from advertising;"
    #     result_dataFrame = pd.read_sql(query, mydb)
    #     print(result_dataFrame.head(10))
    #     # disconnect from server
    #     mydb.close()
    # except Exception as e:
    #     mydb.close()
    #     print(str(e))
    return result_dataFrame
