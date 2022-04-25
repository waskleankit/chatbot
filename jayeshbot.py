import tensorflow as tf
from tensorflow import keras

from keras import optimizers

# #######  Optimizers
# from keras.optimizers import Adam
# from keras.optimizers import SGD

import keras
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
import random
import numpy as np
import pickle
import json
# from copyreg import pickle
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
lemmatizer = nltk.WordNetLemmatizer()


words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']
data_file = open('Intents.json').read()
intents = json.loads(data_file)
# print(intents)


# ########## Pre-Processing Data
for i, intent in enumerate(intents["intents"]):  # ['intents']:
    # print(intent)
    for pattern in intent['patterns']:  # ['patterns']:
        # print(pattern)
        # Tokenize each word in sentence
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # print(pattern)

        # # Add documents in the corpus
        documents.append((w, intent['tag']))
        # s = [(k, intents[k]) for k in intents]
        # documents.append((w, s))

        # # Add to our classes list
        # if intent['tag'] not in classes:
        #     classes.append(intent['tag'])

        intents = json.loads(data_file)
        # for value in intents: #.items():
        #     # s = value[1][0].values()
        #     # s = value[1][0]['tag']
        #     s = intents['intents'][0]['tag']
    s = intents['intents'][i]['tag']  # ['intent']
    classes.append(s)

# lemmatize, lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(set(classes))
# print(words)
#
# print('Remove duplicates & lower case: ', words)
# print('length of words', len(words))
# print('documents: ', documents)
# print('length of words', len(documents))
# print('classes: ', classes)
# print('length of words', len(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# ########## Creating Training Data
training = []
output_empty = [0] * len(classes)
# print(output_empty)

for doc in documents:
    bag = []

    pattern_words = doc[0]   # here in all strings ist letter is capital
    # print(pattern_words)

    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]  # apply for small letters
    # print(pattern_words)
    # for word in pattern_words:
    #     l = [lemmatizer.lemmatize(word)]
    # print(l, end='')

    for w in words:
        if w in pattern_words:
            bag.append(1)
        else:
            bag.append(0)
        # bag.append(1) if w in pattern_words else bag.append(0)
    # print(bag)
    output_row = list(output_empty)
    # print(output_row)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])
# print(training)

# Shufffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# print(training)

# Creating train and test lists X-patterns, Y-intents
train_x = list(training[:, 0])
# print(len(train_x[0]))
train_y = list(training[:, 1])
# print(train_y)

# ############################### print('Training data created')

#  ################### Build The Machine Learning Model
# model = Sequential()
# model.add(Dense(128, input_shape=(len(train_x[0]), ), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(train_y[0]), activation='softmax'))


model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
# model.add(Dense(32, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
# model.add(Dropout(0.5))

# Compile Keras model with SGD optimizer:
# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model

# sgd = tf.keras.optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

adam = tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=False, name="Adam")
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])

# Fit the model — execute training and construct classification model.
hist = model.fit(np.array(train_x), np.array(train_y), validation_split=0.33, epochs=500, batch_size=32, verbose=1)
# print(type(hist))
# print("SGD optimizers run successfully!")
print("Adam optimizers run successfully!")

# evaluate the model
import numpy
cvscores = []
scores = model.evaluate(train_x, train_y, verbose=1)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
print(cvscores)

model.save('Chatbot_model.h5', hist)
# model.save('Chatbot_model.model', hist)
print('Hip, hip, hooray! Model Successfully Trained & Created.')
