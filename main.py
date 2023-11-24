from flask import *

app = Flask(__name__)

@app.route('/')
def revenu_net():
    return render_template('revenu_net.html')

@app.route('/revenu_brut')
def revenu_brut():
    return render_template('revenu_brut.html')

@app.route('/advantage_loan')
def advantage_loan():
    return render_template('advantage_loan.html')

@app.route('/advantage_auto')
def advantage_auto():
    return render_template('advantage_auto.html')


app.run(host='0.0.0.0', port=81)
