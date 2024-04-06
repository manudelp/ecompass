from ..models.user import User
from ..models.planning import Planning
from ..models.mensual import Mensual

def get_user(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    rv = cur.fetchall()
    user = User(rv[0][0], rv[0][1] + " " + rv[0][2], rv[0][3], rv[0][4], rv[0][5])
    return user

def get_plannings(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM planning")
    rv = cur.fetchall()
    plannings = []
    for i in rv:
        plannings.append(Planning(i[1], i[2], i[3], i[4], i[5]))
    return plannings

def get_mensuals(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mensual")
    rv = cur.fetchall()
    mensuals = []
    for i in rv:
        mensuals.append(Mensual(i[1], i[2], i[3]))
    return mensuals

def save_user(mysql, user):
    cur = mysql.connection.cursor()
    update = "UPDATE user SET name=%s, unassignedSavings=%d, totalSavings=%d, estimatedMonthlySavings=%d WHERE id=%d" % (user.name, int(user.save), int(user.saveTotal), int(user.mensualSaveEstimated), int(user.id))
    cur.execute(update)

def save_planning(mysql, planning):
    cur = mysql.connection.cursor()
    insert = "INSERT INTO planning (name, saves, savesAcu, dateEnd, cost) VALUES ('%s', %d, %d, '%s', %d)" % (planning.name, int(planning.saves), int(planning.savesAcu), planning.dateEnd, int(planning.cost))
    cur.execute(insert)

def save_mensual(mysql, mensual):
    cur = mysql.connection.cursor()
    insert = "INSERT INTO mensual (save, date, notes) VALUES (%d, '%s', '%s')" % (int(mensual.save), mensual.date, mensual.notes)
    cur.execute(insert)

def update_planning(mysql, planning):
    cur = mysql.connection.cursor()
    update = "UPDATE planning SET name='%s', saves=%d, savesAcu=%d, dateEnd='%s', cost=%d WHERE id='%d'" % (planning.name, int(planning.saves), int(planning.savesAcu), planning.dateEnd, int(planning.cost), int(planning.id))
    cur.execute(update)

def update_mensual(mysql, mensual):
    cur = mysql.connection.cursor()
    update = "UPDATE mensual SET save=%d, date='%s', notes='%s' WHERE id=%d" % (int(mensual.save), mensual.date, mensual.notes, mensual.id)
    cur.execute(update)