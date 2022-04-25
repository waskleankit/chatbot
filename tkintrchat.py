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
        # 'chatterbot.logic.TimeLogicAdapter'
        ]
        )
intents = json.loads(open('Intents.json','r').read())
train = []
# for k,row in enumerate(data):
#     # print(k , row['question'])
#     train.append(row['question'])
#     train.append(row['answer'])
#     if k > 1024:
#         break


for i, intent in enumerate(intents["intents"]):  # ['intents']:
    # for pattern in intent['patterns']:
    train.append(intent['patterns'])
    train.append(intent['responses'])

print(train)


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

# if __name__ == ''__main__'':
#create the tkinter object(this is the parent window)

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
class Pybot:
    def __init__(self,root):
        self.root = root
        self.front = ('arial',12)
        self.background_color = '#7e7a79'
        self.text_color = '#ffffff'
        menubar = Menu(self.root)
        option_menu = Menu(menubar,tearoff=0)
        # option_menu.add_command(label="Clear Chat",command=self.clear_chat)
        # option_menu.add_command(label="Save Chat",command=self.save_chat)
        option_menu.add_separator()
        option_menu.add_command(label="Exit",command=self.root.quit)
        menubar.add_cascade(label="Options",menu=option_menu)
        self.root.config(menu=menubar)

        self.text_area = ScrolledText(self.root, font=self.front,bg=self.background_color,fg=self.text_color)
        self.text_area.place(x=10,y=10,width=400,height=440)

        frame = Frame(self.root,bg=self.background_color)
        frame.place(x=10,y=460,width=480,height=50)

        self.entry_box = Entry(frame,font=('arial',14))
        self.entry_box.grid(row=0,column=0,pady=9,padx=5)

        self.send_button = Button(frame,text="send",command=self.human_input)
        self.send_button.grid(row=0,column=1,pady=9,padx=5)

    def human_input(self):
        input = self.entry_box.get()
        if input:
            self.text_area.insert(END, "Human : " + input)
            self.entry_box.delete(0, END)
            self.bot_output(input)

    def bot_output(self,input):
        answer = myBot.get_response(input)
        # print(res)
        # answer = next(answer).text
        if answer:
            # self.text_area.insert(END,"\n PyBot : "+answer+'\n')
            self.text_area.insert(END, answer)
            # self.text_area.insert("\n PyBot : ",answer ,'\n',end='')
# root.resizable(0,0)
# Pybot(root)



if __name__ == '__main__':
    root = Tk()
    root.title("Pybot - pythonadvisor")
    root.geometry("500x520")
    root.config(bg="#403b3a")
    root.resizable(0,0)
    Pybot(root)
    root.mainloop()








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
