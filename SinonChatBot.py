#coding=utf8
import itchat
import re
from itchat.content import *

global author
global isDisturbOn
global visit

def remoteControl(msg):
    print "rua!"

def sinonService(msg):
    itchat.send("woops!There is no function can be used yet~", msg["FromUserName"])

def donotDisturb(msg):
    if not visit.get(msg["FromUserName"], False):
        visit[msg["FromUserName"]] = True
        itchat.send("@img@%s" % "sinon.jpg", msg["FromUserName"])
        itchat.send("Sorry!Neil Kleist Gao can't reply you immediately!\nI'm auto-reply bot called sinon. Send #sinon and chat with me!\nsinon's github:https://github.com/NeilKleistGao/SinonChatBot\nWechatAPI github:https://github.com/littlecodersh/itchat\nImage is from Pixiv:https://www.pixiv.net/member_illust.php?mode=medium&illust_id=66989215", msg["FromUserName"])

@itchat.msg_register([TEXT, MAP, CARD, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat = False)
def autoRecieve(msg):
    if msg["ToUserName"] == "filehelper":
        remoteControl(msg)
    else:
        if not msg["FromUserName"] == author:
            if msg["Type"] == "Text":
                if re.search("#sinon", msg["Text"]) == None:
                    if isDisturbOn:
                        donotDisturb(msg)
                else:
                    sinonService(msg)
            else:
                if isDisturbOn:
                    donotDisturb(msg)

visit = {}
isDisturbOn = True
itchat.auto_login(hotReload=True)
author = itchat.search_friends(nickName='Fa1sePRoMiSe')[0]["UserName"]
itchat.run()