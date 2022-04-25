from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox,filedialog
#import wolframalpha
# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# creating a chatbot
import json
myBot = ChatBot(
    name = 'Sakura',
    read_only = True,
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
        ]
        )
data = json.loads(open('nfL6.json','r').read())
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
from tkinter import *

root = Tk()

def getvals():
    print(f"{namevalue.get()} ")
    query=namevalue.get()
    print("Bot :", myBot.get_response(query))
    bot_answr = myBot.get_response(query)
root.geometry("400x500")

#Heading
Label(root, text="chatterbot", font="comicsansms 13 bold", pady=190).grid(row=0, column=3)
#Text for our form
name = Label(root, text="Name")
#Pack text for our form
name.grid(row=1, column=2)
# Tkinter variable for storing entries
namevalue = StringVar()
#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
# Packing the Entries
nameentry.grid(row=1, column=3)
#Button & packing it and assigning it a command
Button(text="Submit", command=getvals).grid(row=7, column=3)
chatWindow = Text(root,bd=1, bg='white', width=50 , height=8)
chatWindow.place(x=6,y=6,height=385,width=370)
root.mainloop()
# # if __name__ == ''__main__'':
# #create the tkinter object(this is the parent window)
# root = Tk()
#
# # def getvals():
# #     print("It works")
#
# #Give the window title
# root.title("Pybot - pythonadviser")
# #give the window some dimensions or geiometry
# root.geometry('400x500')
# #create a main menu bar
# main_menu = Menu(root)
# #create the submenu
# file_menu = Menu(root)
# file_menu.add_command(label='New..')
# file_menu.add_command(label='Save As..')
# file_menu.add_command(label='Exit')
# main_menu.add_cascade(label='File', menu=file_menu)
# main_menu.add_command(label='Edit')
# main_menu.add_command(label='Quit')
# root.config(menu=main_menu)
# #create the chat window
# chatWindow = Text(root,bd=1, bg='white', width=50 , height=8)
# chatWindow.place(x=6,y=6,height=385,width=370)
# #create the message window
# messageWindow = Text(root,bg='white',width=30,height=4)
# messageWindow.place(x=128,y=400 ,height=88 ,width=260)
#
#
# #create a button to send the message
# # Button = Button(root,text='send',command="getvals",bg='blue',activebackground='light blue' , width=12 ,height=5,font=('Arial',20))
# Button = Button(root,text='send',bg='blue',activebackground='light blue' , width=12 ,height=5,font=('Arial',20))
# Button.place(x=6,y=400,height=88,width=120)
# # Button.pack(padx=6,pady=400,height=88,width=120)
#
# #Add a scrollbar
# scrollbar = Scrollbar(root,command=chatWindow.yview())
# scrollbar.place(x=375 , y=5,height=385)
# # root.resizable(0,0)
# # Pybot(root)
# root.mainloop()


# #using the ChatterBotCorpusTrainer class
# query = "hello"
# while query != "exit":
#     print("Bot :", myBot.get_response(query))
#     query = str(input("you : "))

























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
