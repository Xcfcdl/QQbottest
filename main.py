"""QQbot for Japanese's kana learn test"""
# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot
from kanaTest import TestSystem
import sql_do
from tuling import tuling
from GetTecentNew import GetTecentNew
from duanzi import duanzi
from netmusic import Get_music
from Tenseijinngo import Tenseijinngo

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if contact.ctype == 'buddy':
        if not sql_do.get_oneusers(contact.qq):
            try:
                sql_do.bulid_db()
            except:
                pass
            finally:
                sql_do.usersinsert(contact.qq, 1, 0, 0, 0, 0)
        _qq, _model1, _model2, _model3, _model4, _model5 = sql_do.get_oneusers(contact.qq)[0]
        if content == '开始五十音测试':
            _model1 = 0
            _model2 = 1
            _model3 = 0
            _model4 = 0
            _model5 = 0
            #TestSystem(contact.qq, content).main()
            #bot.SendTo(contact, '开始测试：\n{}'.format())

        elif content == '结束':
            _model1 = 1
            _model2 = 0
            _model3 = 0
            _model4 = 0
            _model5 = 0
            bot.SendTo(contact, "已退出")

        elif content == 'mo3':
            _model1 = 0
            _model2 = 0
            _model3 = 1
            _model4 = 0
            _model5 = 0
            bot.SendTo(contact, "333")

        elif content == 'mo4':
            _model1 = 0
            _model2 = 0
            _model3 = 0
            _model4 = 1
            _model5 = 0
            bot.SendTo(contact, "444")

        elif content == 'mo5':
            _model1 = 0
            _model2 = 0
            _model3 = 0
            _model4 = 0
            _model5 = 1
            bot.SendTo(contact, "555")

        elif content == '段子':
            bot.SendTo(contact, str(duanzi().get_duanzi()))
        elif '天声人语' in content:
            a = str(content).replace('天声人语', '').replace(' ', '')
            if len(a) == 0:
                number = 1
            else:
                number = int(a)
            essay = str(Tenseijinngo(number).run())
            bot.SendTo(contact, str(essay))

        elif '点歌' in content:
            music_name = str(content).split(" ")[-1]
            music_ID = Get_music(music_name).get_musicID()
            if music_ID.isdigit():
                bot.SendTo(contact, "用户点歌：{}\n".format(
                    music_name) + "http://music.163.com/#/song?id={ID}".format(ID=music_ID))
            else:
                bot.SendTo(contact, "对不起，未找到歌曲：{}".format(music_name))
        elif content == '腾讯新闻':
            get_new = GetTecentNew().get_TecentNew()
            bot.SendTo(contact, str(get_new))

        elif '查询' in content:
            """回复可查询指令"""
            bot.SendTo(contact, '回复可查询指令:1,2,3,4,')

        elif content == '测试成绩':
            """"""
            bot.SendTo(contact, '成绩')

        elif _model1:
            bot.SendTo(contact, tuling(content))

        elif _model2:
            # msg = TestSystem(contact.qq, content).main()
            # bot.SendTo(contact, msg)
            bot.SendTo(contact, '_model2')

        elif _model3:
            bot.SendTo(contact, '_model3')

        elif _model4:
            bot.SendTo(contact, '_model4')

        elif _model5:
            bot.SendTo(contact, '_model5')

        sql_do.update_users(_qq, _model1, _model2, _model3, _model4, _model5)




if __name__ == '__main__':
    RunBot()