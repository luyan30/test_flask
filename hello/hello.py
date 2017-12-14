# -*- coding: utf-8 -*-
import pymysql
from flask import Flask,render_template,jsonify,request
app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま

@app.route('/')
def hello():
    db=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='testdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur=db.cursor()
    sql="select * from members"
    cur.execute(sql)
    members=cur.fetchall()
    cur.close()
    db.close()

    return jsonify({'status':'OK','members':members})

@app.route('/good')
def good():
    name = "Good"
    return name


@app.route('/hi')
def hi():
    name=request.args.get('name')
    return render_template('index.html',title='flask test',name=name)

@app.route('/bye', methods=['POST'])
def bye():
    if request.method=='POST':
        name=request.form['name']
    else:
        name="no name."
    return render_template('index.html',title='flask test', name=name)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
