"""
bulid_db()新建数据库
get_all()查询数据库所有数据
get_kanagoals(cur)查询kanagoals所有数据
get_users(cur):查询users
usersinsert(_qq, _mode1, _model2, _model3, _model4, _model5):插入一行users数据
kanamodelinsert(_qq, _modeswitch, _count, _starttime) 插入一个kanamodel数据
usergoalsinsert(_qq, _time, _goals, _modelswitch) 插入一个分数数据
update_users(_qq, _model1, _model2, _model3, _model4, _model5)更新users数据，改model状态时用
update_kanamodel(_qq, _modeswitch, _count, _starttime)更新kanamodel状态，进入kana模式用
update_usergoals(_qq, _time, _goals, _modelswitch)更新分数数据， 结束kana一个循环时用
get_onekana(_qq)获取某一用户kana数据
get_oneusers(_qq)获取某一用户users数据
get_onegoals(_qq)获取某一用户goals数据
"""

import sqlite3

def get_con(func):
    data_path = r"user_db.db"

    def sql_exc():
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = func(cur)
        cur.close()
        conn.commit()
        conn.close()
        return data

    return sql_exc


@get_con
def get_users(cur):
    # 查询users
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows


@get_con
def get_kana_model(cur):
    # 查询kanamodel所有数据
    cur.execute("SELECT * FROM KANAMODEL")
    rows = cur.fetchall()
    return rows


@get_con
def get_kanagoals(cur):
    # 查询所有goals数据
    cur.execute("SELECT * FROM USERGOALS")
    rows = cur.fetchall()
    return rows


@get_con
def userstable(cur):
    cur.execute('''CREATE TABLE USERS 
              (
                QQ1 INT PRIMARY KEY, MODEL1 INT NULL, MODEL2 INT NULL, MODEL3 INT NULL, MODEL4 INT NULL, MODEL5 INT NULL
              )''')
    return True


@get_con
def kanamodeltable(cur):
    """DATETIME: YYYY-MM-DD HH:MM:SS.SSS"""
    cur.execute('''CREATE TABLE KANAMODEL 
              (
                QQ2 INT PRIMARY KEY, MODELSW INT NOT NULL, COUNT INT NOT NULL, STARTTIME TEXT NOT NULL
              )''')
    return True


@get_con
def usergoalstable(cur):
    cur.execute('''CREATE TABLE USERGOALS
              (
                QQ3 INT PRIMARY KEY, TIME INT NOT NULL ,  GOALS INT NULL, MODELswitch INT NULL
              )''')
    return True


def bulid_db():
    """数据库初始化在此"""
    try:
        userstable()
    except:
        print('已有user表')
    try:
        usergoalstable()
    except:
        print('已有goals表')
    try:
        kanamodeltable()
    except:
        print('已有kanamodel表')

def get_all():
    print('user' + str(get_users()))
    print('kanagoals' + str(get_kanagoals()))
    print('kana_model' + str(get_kana_model()))



def usersinsert(_qq, _mode1, _model2, _model3, _model4, _model5):
    """插入一行users数据"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _mode1, _model2, _model3, _model4, _model5,)
        ins = 'INSERT INTO users (qq1, model1, model2, model3, model4, model5) VALUES(?, ?, ?, ?, ?, ?)'
        cur.execute(ins, data)
        return True
    except:
        print('eroo userinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()


def kanamodelinsert(_qq, _modeswitch, _count, _starttime):
    # 插入一个kanamodel数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _modeswitch, _count, _starttime,)
        ins = 'INSERT INTO KANAMODEL (qq2, modelsw, count, starttime) VALUES(?, ?, ?, ?)'
        cur.execute(ins, data)
        return True
    except:
        print('eroo kanamodelinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()


def usergoalsinsert(_qq, _time, _goals, _modelswitch):
    # 插入一个分数数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _time, _goals, _modelswitch)
        ins = 'INSERT INTO USERGOALS (qq3, time, goals, modelswitch) VALUES(?, ?, ?, ?)'
        cur.execute(ins, data)
        return True
    except:
        print('eroo usergoalsinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()


def update_users(_qq, _model1, _model2, _model3, _model4, _model5):
    # 更新users数据，改model状态时用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _model1, _model2, _model3, _model4, _model5,)
        ins = 'update users set model1 = ? where qq1 = ?'
        cur.execute(ins, (data[1],data[0]))
        ins = 'update users set model2 = ? where qq1 = ?'
        cur.execute(ins, (data[2], data[0]))
        ins = 'update users set model3 = ? where qq1 = ?'
        cur.execute(ins, (data[3], data[0]))
        ins = 'update users set model4 = ? where qq1 = ?'
        cur.execute(ins, (data[4], data[0]))
        ins = 'update users set model5 = ? where qq1 = ?'
        cur.execute(ins, (data[5], data[0]))
        return True
    except:
        print('eroo update_users')
    finally:
        cur.close()
        conn.commit()
        conn.close()


def update_kanamodel(_qq, _modeswitch, _count, _starttime):
    # 更新kanamodel状态，进入kana模式用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _modeswitch, _count, _starttime)
        """qq2, modelsw, count, starttime"""
        ins = 'update kanamodel set modelsw = ? where qq2 = ?'
        cur.execute(ins, (data[1], data[0]))
        ins = 'update kanamodel set count = ? where qq2 = ?'
        cur.execute(ins, (data[2], data[0]))
        ins = 'update kanamodel set starttime = ? where qq2 = ?'
        cur.execute(ins, (data[3], data[0]))
        return True
    except:
        print("update_kanamodel")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()


def update_usergoals(_qq, _time, _goals, _modelswitch):
    # 更新分数数据， 结束kana一个循环时用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _time, _goals, _modelswitch)
        "qq3, time, goals, modelswitch"
        ins = 'update USERGOALS set time = ? where qq3 = ?'
        cur.execute(ins, (data[1], data[0]))
        ins = 'update USERGOALS set goals = ? where qq3 = ?'
        cur.execute(ins, (data[2], data[0]))
        ins = 'update USERGOALS set modelswitch = ? where qq3 = ?'
        cur.execute(ins, (data[3], data[0]))
        return True
    except:
        print('update_usergoals')
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def get_onegoals(_qq):
    """获取某一用户goals数据"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        "qq3, time, goals, modelswitch"
        ins = 'select * from USERGOALS where qq3 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        return rows
    except:
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()


def get_oneusers(_qq):
    # 获取某一用户users数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        ins = 'select * from USERS where qq1 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        return rows
    except:
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()


def get_onekana(_qq):
    # 获取某一用户kana数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        ins = 'select * from kanamodel where qq2 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        return rows
    except:
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()
# u1 k2 g3
