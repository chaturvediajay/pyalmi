from flask import Flask, send_file, render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

import json
import requests

fig, ax = plt.subplots(figsize=(6, 6))
ax = sns.set_style(style="darkgrid")

x = [i for i in range(100)]
y = [i for i in range(100)]

app = Flask(__name__)


@app.route('/')
def home():
    data1 = {'username': 'admin', 'password': 'admin'}
    headers = {'Content-type': 'application/json'}
    response = requests.post('https://panicdirection.herokuapp.com/authenticate', json.dumps(data1), headers=headers)
    res = ''
    if response.status_code == 200:
        print('response Code ' + str(response.status_code))
        sampl = json.loads(response.text)
        print(sampl["token"])
        headers = {'Authorization': 'Bearer ' + sampl["token"], "Content-Type": "application/text"}
        payload = {}
        response = requests.get('https://panicdirection.herokuapp.com', headers=headers, data=payload)
        if response.status_code == 200:
            res = str(response.text)

    return render_template('index.html', prediction_text='Employee Salary should be  ' + res)


@app.route('/visualize')
def visualize():
    sns.lineplot(x, y)
    canvas = FigureCanvas(fig)
    plt.xlabel('salary')
    plt.ylabel('age')
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')


if __name__ == "__main__":
    app.run(debug=True)
