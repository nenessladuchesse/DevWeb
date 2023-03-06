from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db=SQLAlchemy(app)
#db.init_app(app)

class data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    rna_id = db.Column(db.String(30), nullable=True) 
    rna_id_ex = db.Column(db.String(30), nullable=True)
    gestion = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/assos')
def assos():
    datas = Data.query.limit(10).all()
    for data in datas:
        print(f"{data.rna_id}")
    #stmt = select(Data)
    #result = session.execute(stmt)
    #for data in result.scalars():
    #    print(f"{data.rna_id}")

    return render_template('assos.html')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '-_main_-':
    app.run()
# Ajouter cette route à votre code Flask existant
@app.route('/add_data', methods=['POST'])
def add_data():
    rna_id = request.form['rna_id']
    rna_id_ex = request.form['rna_id_ex']
    gestion = request.form['gestion']

    new_data = data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
    db.session.add(new_data)
    db.session.commit()

    return redirect(url_for('assos'))
    