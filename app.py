from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',prediction_text='Employee Salary should be')



if __name__ == "__main__":
    app.run(debug=True)