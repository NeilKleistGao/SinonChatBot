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
                    donotDisturb(msg["FromUserName"])
                else:
                    notice(msg["NickName"])
            else:
                sinonService(msg["FromUserName"], msg["Text"])
        else:
            if isDisturbOn:
                donotDisturb(msg["FromUserName"])
            else:
                notice(msg["NickName"])

def notice(name):
    print "%s send a message to you." % name

def remoteControl(text):
    if text == "-h":
        itchat.send("-s Stop auto reply\n-d Turn on the Don't disturb\n -f Turn off the Don't disturb", "filehelper")
    elif text == "-s":
        itchat.logout()
    elif text == "-d":
        isDisturbOn = True
        itchat.send("Turn on the Don't disturb", "filehelper")
    elif text == "-f":
        isDisturbOn = False
        itchat.send("Turn off the Don't disturb", "filehelper")

def sinonService(name, text):
    itchat.send("woops!There is no function can be used yet~", name)

def donotDisturb(name):
    if not visit.get(name, False):
        visit[name] = True
        itchat.send("@img@%s" % "sinon.jpg", name)
        itchat.send("Sorry!%s can't reply you immediately!\nI'm auto-reply bot called sinon. Send #sinon and chat with me!(If you are in a group please @Fa1sePRoMiSe first.)\nsinon's github:https://github.com/NeilKleistGao/SinonChatBot\nWechatAPI github:https://github.com/littlecodersh/itchat\nImage is from Pixiv:https://www.pixiv.net/member_illust.php?mode=medium&illust_id=66989215" % username, name)

@itchat.msg_register([TEXT, MAP, CARD, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat = False)
def autoRecieve(msg):
    if msg["ToUserName"] == "filehelper" and msg["Type"] == "Text":
        remoteControl(msg["Text"])
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
itchat.send("You have started Sinon on your PC.Please enter -h for help.", "filehelper")
itchat.run()