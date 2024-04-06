from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from models.user import *
from models.planning import *
from models.mensual import *
from repository.repository import *
import json 

app = Flask(__name__)

# Required
app.config["MYSQL_HOST"] = "10.7.18.12"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "root2"
app.config["MYSQL_PASSWORD"] = "Credentials#0!"
app.config["MYSQL_DB"] = "ecompassdb"

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL(app)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hola mundo'

@app.route('/user')
@cross_origin()
def get_user():
    user = get_user(mysql)
    return json.dumps(user.__dict__)

@app.route('/plannings')
@cross_origin()
def get_planning():
    plannings = get_plannings(mysql)
    plannings = [planning.__dict__ for planning in plannings]
    return json.dumps(plannings)

@app.route('/mensual')
@cross_origin()
def get_mensual():
    mensuals = get_mensuals(mysql)
    mensuals = [mensual.__dict__ for mensual in mensuals]
    return json.dumps(mensuals)

@app.route('/user', methods=['POST'])
@cross_origin()
def post_user():
    #Get data from request
    data = request.json
    user = User(data['id'], "", data['save'], data['saveTotal'], data['mensualSaveEstimated'])
    #Get old user data
    oldUser = get_user(mysql)
    user.name = oldUser.name
    #Update user data
    save_user(mysql, user)

    return json.dumps(user.__dict__)

@app.route('/planning', methods=['POST'])
@cross_origin()
def post_planning():
    #Get data from request
    data = request.json
    planningToInsert = Planning(0, data['name'], data['saves'], data['savesAcu'], data['dateEnd'], data['cost'])
    #Get user data
    user = get_user(mysql)
    #Get all plannings
    plannings = get_plannings(mysql)
    #Calculate total saves
    totalSaves = 0
    for planning in plannings:
        totalSaves += planning.saves
    if totalSaves + planningToInsert.saves > user.save:
        return json.dumps({"error": "Te estas excediendo del ahorro total"})
    #Save planning
    save_planning(mysql, planningToInsert)

    return json.dumps(planning.__dict__)

@app.route('/mensual', methods=['POST'])
@cross_origin()
def post_mensual():
    #Get data from request
    data = request.json
    mensual = Mensual(0, data['save'], data['date'], data['notes'])
    #Save mensual
    save_mensual(mysql, mensual)

    return json.dumps(mensual.__dict__)

@app.route('/planning', methods=['PUT'])
@cross_origin()
def put_planning():
    #Get data from request
    data = request.json
    planning = Planning(data['id'], data['name'], data['saves'], data['savesAcu'], data['dateEnd'], data['cost'])
    #Update planning
    update_planning(mysql, planning)

    return json.dumps(planning.__dict__)

@app.route('/mensual', methods=['PUT'])
@cross_origin()
def put_mensual():
    #Get data from request
    data = request.json
    mensual = Mensual(data['id'], data['save'], data['date'], data['notes'])
    #Update mensual
    update_mensual(mysql, mensual)

    return json.dumps(mensual.__dict__)

@app.route('/dbtest')
def dbtest():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    rv = cur.fetchall()
    user = User(rv[0][0], rv[0][1], rv[0][2], rv[0][3], rv[0][4])
    return json.dumps(user.__dict__)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')