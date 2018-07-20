import itchat
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

deepThought = ChatBot('deepThought')
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train('chatterbot.corpus.chinese')


@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    response = deepThought.get_response(msg['Text'])
    itchat.send(msg=str(response), toUserName=msg['FromUserName'])


itchat.auto_login(enableCmdQR=2)
itchat.run()
