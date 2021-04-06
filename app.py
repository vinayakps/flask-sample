import flask
from flask import request, jsonify
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MYSQL_HOST'] = 'sql6.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql6403507'
app.config['MYSQL_PASSWORD'] = 'MVwEwIDKPt'
app.config['MYSQL_DB'] = 'sql6403507'
mysql=MySQL(app)


 
@app.route('/api/userLogin',  methods=['POST'])
def userLogin():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", [email, password])
        account = cur.fetchone()
        mysql.connection.commit()
 
 

        if account :
            name = account[0]
            email = account[1]
            return jsonify({"name":name,"email":email})
        else:
            return jsonify({ })



 
@app.route('/api/register',  methods=['POST'])
def register():

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'name' in request.form:
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
    
        cursor = mysql.connection.cursor()

        try:
            cursor.execute('INSERT INTO users(name,email,password) VALUES ( %s, %s, %s)', (name,email, password))
            mysql.connection.commit()
            return jsonify({"result":True})
        except:
            return jsonify({"result":False})

 
@app.route('/',)
def home():
    return jsonify({"asd":"asd"})

 
app.run()
 
# app.run(ssl_context='adhoc')