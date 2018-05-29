import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    player_1 = itchat.search_friends('Bicycle')[0]
    player_2 = itchat.search_friends('青春如火!')[0]

    if msg.fromUserName == player_1.userName:
        itchat.send(msg.text.replace("李晨", "谈楚"), player_2.userName)
        print('player_1 -> player_2: ' + msg.text)

    if msg.fromUserName == player_2.userName:
        itchat.send(msg.text.replace("谈楚", "李辰"), player_1.userName)
        print("player_1 <- player_2: " + msg.text)


@itchat.msg_register(itchat.content.ATTACHMENT)
def attachment_clap(msg):
    team = itchat.search_chatrooms('博悦斋')[0]

    ext = msg.fileName[-3:]
    if msg.fromUserName == team.userName and (ext == 'm4a' or ext == 'mp3'):
        itchat.send('👏', toUserName=team.userName)
        print('-> ' + msg.fileName)


itchat.auto_login()
itchat.run()
