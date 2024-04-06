import sys
sys.path.append('../')

from models.user import *
from models.planning import *
from models.mensual import *

import datetime

def get_user_repo(mysql, id):
    cur = mysql.connection.cursor()
    select = "SELECT * FROM user WHERE idUser=%d" % int(id)
    cur.execute(select)
    rv = cur.fetchall()
    user = User(rv[0][0], rv[0][1] + " " + rv[0][2], rv[0][3], rv[0][4], rv[0][5])
    return user

def get_plannings_repo(mysql, id):
    cur = mysql.connection.cursor()
    select = "SELECT * FROM plan WHERE idUser=%d" % int(id)
    cur.execute(select)
    rv = cur.fetchall()
    plannings = []
    print(rv)
    for i in rv:
        print(i)
        plannings.append(Planning(i[0], i[1], i[2], i[3], i[4], i[5]))
    return plannings

def get_mensuals_repo(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM payment")
    rv = cur.fetchall()
    mensuals = []
    for i in rv:
        mensuals.append(Mensual(i[0], i[1], i[2], i[4]))
    return mensuals

def save_user(mysql, user):
    cur = mysql.connection.cursor()
    update = "UPDATE user SET unassignedSavings=%f, totalSavings=%f, estimatedMonthlySavings=%f WHERE idUser=%d" % (float(user.save), float(user.saveTotal), float(user.mensualSaveEstimated), int(user.id))
    print(update)
    cur.execute(update)
    mysql.connection.commit()

def save_planning(mysql, planning, idUser):
    cur = mysql.connection.cursor()
    insert = "INSERT INTO plan (namePlan, estimatedSaved, totalSaved, estimatedDate, totalCost, idUser, percentageAssigned) VALUES ('%s', %f, %f, '%s', %f, %d, %f)" % (planning.name, float(planning.saves), float(planning.savesAcu), planning.dateEnd, float(planning.cost), int(idUser), float(planning.saves))
    cur.execute(insert)
    mysql.connection.commit()

def save_mensual(mysql, mensual, idUser):
    cur = mysql.connection.cursor()
    date = datetime.datetime.strptime(mensual.date, '%Y-%m')
    insert = "INSERT INTO payment (paymentAmount, paymentDate, idUser, paymentNote) VALUES (%f, \'%s\', %d, \"%s\");" % (float(mensual.save), date.strftime('%Y-%m-%d %H:%M:%S'), int(idUser), mensual.notes)
    print(insert)
    cur.execute(insert)
    mysql.connection.commit()

def update_planning(mysql, planning):
    cur = mysql.connection.cursor()
    update = "UPDATE plan SET namePlan='%s', estimatedSaved=%f, totalSaved=%f, estimatedDate='%s', totalCost=%d WHERE idPlan='%d'" % (planning.name, float(planning.saves), float(planning.savesAcu), planning.dateEnd, int(planning.cost), int(planning.id))
    cur.execute(update)
    mysql.connection.commit()

def update_mensual(mysql, mensual):
    cur = mysql.connection.cursor()
    update = "UPDATE mensual SET save=%f, date='%s', notes='%s' WHERE id=%d" % (float(mensual.save), mensual.date, mensual.notes, mensual.id)
    cur.execute(update)
    mysql.connection.commit()