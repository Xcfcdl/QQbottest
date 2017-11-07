#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

class TestSystem():
    """接收信息返回信息"""
    def __init__(self, qq, content):
        with open('test_db.txt', 'rt',encoding='utf-8') as f:
            self.test_db = list(f.read())
            # 必须要数据库了
        self.msg =content.lower()
        self.answer_now = ''
        self.qq = qq
        self.mode = ''
        self.goals = ''
        self.testtime = ''

    def getStart(self):
        user_db = sqlite3.connect('user_db.db')
        # QQ INT PRIMARY KEY, MODE VARCHAR(20), KANAGOALS FLOAT, TESTTIME INT
        c = user_db.cursor()
        try:
            c.execute('''CREATE TABLE USERS 
                      (
                        QQ INT PRIMARY KEY, MODE VARCHAR(20), KANAGOALS FLOAT, TESTTIME INT
                      )''')
        except:
            print('erro rebulid db or no need')
        try:
            c.execute("SELECT * from USERS where qq=?", (self.qq,))
            res = c.fetchall()
            if len(res) > 0:
                self.test_db = res[0]
            else:
                ins = 'insert into users (qq, mode, kanagoals, testtime) VALUES(?, ?, ?, ?)'
                c.execute(ins, (self.qq, 'kanatest', 0, 0))
                print('write newer in user_db')
                c.execute("SELECT * from USERS where qq=?", (self.qq,))
                self.test_db = c.fetchall()[0]
            qq, self.mode, self.goals, self.testtime = self.test_db
        except:
            print('Erro in db_read_getstart')
        finally:
            c.close()
            user_db.commit()
            user_db.close()

    def update(self):
        try:
            user_db = sqlite3.connect('user_db.db')
            # QQ INT PRIMARY KEY, MODE VARCHAR(20), KANAGOALS FLOAT, TESTTIME INT
            c = user_db.cursor()
            c.execute("UPDATE users set KANAGOALS=? WHERE qq=?", (self.goals, self.qq))
            c.execute("UPDATE users set TESTTIME=? WHERE qq=?", (self.testtime, self.qq))
        except:
            print("erro in update_db")
        finally:
            c.close()
            user_db.commit()
            user_db.close()

    def qes_ans(self):
        # 出题与比对答案，然后计算分数，更新数据库
        # get_qes()
        # if self.msg
        return '下一题'

    def result_cul(self):
        return '已结束测试，题目总数为：{a}，您的答对了 {b} 题，打错了 {c} 题。得分是： {d}分。\n错题分别是{e}'.format(a='10', b='5', c='5', d='50',e=' wrong')

    def main(self):
        """
        首先检测现在模式是否符合，让后检测输入是否合法， 让后开始出题、比对、计算分数、更新数据库，再此过程中特别接受命令（查分，退出，显示答案，暂停与继续）
        :return:
        """
        if self.msg == "五十音测试":
            try:
                self.getStart()
            except:
                print("erro msgcheck")
                return False
            return self.qes_ans()
        elif self.msg in ["结束", "退出"]:
            return self.result_cul()

        elif self.msg in self.test_db:
            return self.qes_ans()

