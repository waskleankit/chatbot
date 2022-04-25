# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# creating a chatbot

myBot = ChatBot(
    name = 'Sakura',
    read_only = True,
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        # 'chatterbot.logic.TimeLogicAdapter'
        ]
        )


import json
data = json.loads(open('nfL6.json','r').read())

# print('-----------------------------------------------')
# print(data)
# print('-----------------------------------------------')
train = []
for k,row in enumerate(data):
    # print(k , row['question'])
    train.append(row['question'])
    train.append(row['answer'])
    if k > 1024:
        break

small_convo = [
    "hello",
    "hi, how can I help you?",
    "sure, I'd like to book a flight to Iceland.",
    "your flight has been booked.",
    "i am jayesh bhawsar",
    "ohh yes, I rememberd you, you are working in VKAPs, Indore.",
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
]


math_convo_1 = [
    'Pythagorean theorem',
    'a squared plus b squared equals c squared.'
]

math_convo_2 = [
    'Law of Cosines',
    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)'
]

# trainer.train(train)
# corpus_trainee = ChatterBotCorpusTrainer(myBot)
# corpus_trainee.train('chatterbot.corpus.english')
trainer = ListTrainer(myBot)
# using the ListTrainer class
list_trainee = ListTrainer(myBot)
for i in (small_convo, math_convo_1, math_convo_2,train):
    list_trainee.train(i)


query = ''
# using the ChatterBotCorpusTrainer class
while query != "exit":
    query = str(input("you : "))
    if query=='exit':
        break
    print("Bot :", myBot.get_response(query))




# training the chatbot
# small_convo = [
#     'Hi there!',
#     'Hi',
#     'How do you do?',
#     'How are you?',
#     'I\'m cool.',
#     'Always cool.',
#     'I\'m Okay',
#     'Glad to hear that.',
#     'I\'m fine',
#     'I feel awesome',
#     'Excellent, glad to hear that.',
#     'Not so good',
#     'Sorry to hear that.',
#     'What\'s your name?',
#     ' I\'m Sakura. Ask me a math question, please.',
#     'Who built you',
#     'Ankit waskle',
#
# ]
# bot = ChatBot(
#     'Exact Response Example Bot',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             'import_path': 'chatterbot.logic.BestMatch'
#         },
#         {
#             'import_path': 'chatterbot.logic.SpecificResponseAdapter',
#             'input_text': 'specific',
#             'output_text': 'ankit'
#         }
#     ]
# )
