from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from models.user import *
from models.planning import *
from models.mensual import *
from repository.repository import *
import json
import requests
from googlefinance import getQuotes

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
    user = get_user_repo(mysql, request.args.get('id'))
    return json.dumps(user.__dict__)

@app.route('/plannings')
@cross_origin()
def get_planning():
    plannings = get_plannings_repo(mysql, request.args.get('id'))
    planningsJson = []
    for plan in plannings:
        plan.dateEnd = plan.dateEnd.strftime('%Y-%m')
        planningsJson.append(plan.__dict__)
    return json.dumps(planningsJson)

@app.route('/mensual')
@cross_origin()
def get_mensual():
    mensuals = get_mensuals_repo(mysql)
    print(mensuals)
    mensualsJson = []
    for mensual in mensuals:
        mensual.date = mensual.date.strftime('%Y-%m')
        mensualsJson.append(mensual.__dict__)
    print(mensualsJson)
    return json.dumps(mensualsJson)

@app.route('/user', methods=['POST'])
@cross_origin()
def post_user():
    #Get data from request
    data = request.json
    user = User(data['id'], "", data['save'], data['saveTotal'], data['mensualSaveEstimated'])
    #Get old user data
    oldUser = get_user_repo(mysql, user.id)
    user.name = oldUser.name
    #Update user data
    save_user(mysql, user)

    return json.dumps(user.__dict__)

@app.route('/plannings', methods=['POST'])
@cross_origin()
def post_planning():
    #Get data from request
    data = request.json
    planningToInsert = Planning(0, data['name'], data['saves'], data['savesAcu'], datetime.datetime.now(), data['cost'])
    #Get user data
    idUser = int(request.args.get('id'))
    user = get_user_repo(mysql, idUser)
    #Get all plannings
    plannings = get_plannings_repo(mysql, idUser)
    #Calculate total saves
    totalSaves = 0
    for planning in plannings:
        print(planning.__dict__)
        totalSaves += planning.saves
    if totalSaves + planningToInsert.saves > 100:
        return json.dumps({"error": "Te estas excediendo del ahorro total"})
    #Save planning
    monthlySaves = planningToInsert.cost / (user.mensualSaveEstimated * (planningToInsert.saves/100))
    planningToInsert.dateEnd = planningToInsert.dateEnd + datetime.timedelta(days=(30*int(monthlySaves)))
    save_planning(mysql, planningToInsert, int(request.args.get('id')))
    planningToInsert.dateEnd = planningToInsert.dateEnd.strftime('%Y-%m')
    return json.dumps(planningToInsert.__dict__)

@app.route('/mensual', methods=['POST'])
@cross_origin()
def post_mensual():
    #Get data from request
    data = request.json
    mensual = Mensual(0, data['save'], data['date'], data['notes'])
    saveTotal = mensual.save
    plannings = get_plannings_repo(mysql, int(request.args.get('id')))
    user = get_user_repo(mysql, int(request.args.get('id')))
    print(user.__dict__)
    print(mensual.__dict__)
    print(plannings)
    for plan in plannings:
        savePlan = (plan.saves / 100) * user.mensualSaveEstimated
        if (plan.savesAcu + savePlan) > plan.cost:
            savePlan = plan.cost - plan.savesAcu
            plan.saves = 0
        plan.savesAcu += savePlan
        mensual.save -= savePlan
        update_planning(mysql, plan)
    user.save += mensual.save
    user.saveTotal += saveTotal
    print("---------------")
    print(user.__dict__)
    print(mensual.__dict__)
    print(plannings)
    save_user(mysql, user)
    #Save mensual
    save_mensual(mysql, mensual, int(request.args.get('id')))

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

@app.route('/testCrypto')
def testCrypto():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    crypto_prices = {
        "BTC": data['price']
    }
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    data = requests.get(key)
    data = data.json()
    crypto_prices["ETH"] = data['price']
    return json.dumps(crypto_prices)

@app.route('/testStock')
def testStock():
    stocks = json.dumps(getQuotes('AAPL'))
    #stocksShow = {}
    #for stock in stocks:
    #    stocksShow[stock['StockSymbol']] = stock['LastTradePrice']
    return stocks

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')