#coding=utf8
import itchat
import re
import sys
from itchat.content import *

global author
global isDisturbOn
global visit
global username

def messageProccess(msg):
    if not msg["FromUserName"] == author:
        if msg["Type"] == "Text":
            if re.search("#sinon", msg["Text"]) == None:
                if isDisturbOn:
                    donotDisturb(msg)
                else:
                    notice(msg["NickName"])
            else:
                sinonService(msg)
        else:
            if isDisturbOn:
                donotDisturb(msg)
            else:
                notice(msg["NickName"])

def notice(name):
    print "%s send a message to you." % name

def remoteControl(msg):
    print "woops!There is no function can be used yet~"

def sinonService(msg):
    itchat.send("woops!There is no function can be used yet~", msg["FromUserName"])

def donotDisturb(msg):
    if not visit.get(msg["FromUserName"], False):
        visit[msg["FromUserName"]] = True
        itchat.send("@img@%s" % "sinon.jpg", msg["FromUserName"])
        itchat.send("Sorry!%s can't reply you immediately!\nI'm auto-reply bot called sinon. Send #sinon and chat with me!(If you are in a group please @Fa1sePRoMiSe first.)\nsinon's github:https://github.com/NeilKleistGao/SinonChatBot\nWechatAPI github:https://github.com/littlecodersh/itchat\nImage is from Pixiv:https://www.pixiv.net/member_illust.php?mode=medium&illust_id=66989215" % username, msg["FromUserName"])

@itchat.msg_register([TEXT, MAP, CARD, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat = False)
def autoRecieve(msg):
    if msg["ToUserName"] == "filehelper":
        remoteControl(msg)
    else:
        messageProccess(msg)

@itchat.msg_register([TEXT, MAP, CARD, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat = True)
def autoRecieveInGroup(msg):
    if msg["isAt"]:
        messageProccess(msg)

visit = {}
username = "Fa1sePRoMiSe"
isDisturbOn = True
if len(sys.argv) == 2:
    username = sys.argv[1]
elif len(sys.argv) == 3:
    username = sys.argv[1]
    isDisturbOn = sys.argv[2]
itchat.auto_login(hotReload=True)
author = itchat.search_friends(nickName=username)[0]["UserName"]
itchat.run()