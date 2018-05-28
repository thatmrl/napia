import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    player_1 = itchat.search_friends('Bicycle')[0]
    player_2 = itchat.search_friends('青春如火!')[0]

    if msg.fromUserName == player_1.userName:
        itchat.send(msg.text, toUserName=player_2.userName)
        print('player_1 -> player_2: ' + msg.text)

    if msg.fromUserName == player_2.userName:
        itchat.send(msg.text, toUserName=player_1.userName)
        print("player_1 <- player_2: " + msg.text)


itchat.auto_login()
itchat.run()
