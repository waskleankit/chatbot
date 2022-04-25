import json
data = json.loads(open('conver.json','r').read())

train = []
# print(data['conversations'])
for k,row in enumerate(data['conversations']):
    # print(k , row['question'])
    train.append(row['question'])
    train.append(row['answer'])

    # if k > 1024:
    #     break

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('QA')

trainer = ListTrainer(chatbot)

trainer.train(train)

while True:
    request = input('You: ')

    if request != data['conversations'][1]['question']:
        convers = "conver.json"


        def write_json(new_data, filename=convers):
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data['conversations'].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent=4)


        y = {
            "question": request,
            "answer": ""  # conver['conversations'][0]['answer']
        }
        write_json(y)

        # print("Spydi: ", y["answer"])
        # print('------------------- 2 ---------------------')

    response = chatbot.get_response(request)
    print('Bot:', response)