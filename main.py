
import random
from nltk import tokenize, corpus, stem

class Model:

    def __init__(self):
        self.lemmatizer = stem.WordNetLemmatizer()
        self.stopwords = set(corpus.stopwords.words("english"))
        self.data = [
            (["hello", "hi", "hey"], ["Hello!", "Hi!"]),
            (["name"], ["I am WordNET.", "I am your personal assistant, WordNET."]),
            (["how are you"], ["I am doing great!"])
        ]
        while True:
            self.reply(input(" > "))

    def reply(self, text):
        self.answer = []
        self.token = tokenize.word_tokenize(text.lower())
        self.filtered = [self.lemmatizer.lemmatize(token) for token in self.token]
        for self.item in self.data:
            if len([part for part in self.item[0] if part in self.filtered]) > 0:
                self.answer.append(random.choice(self.item[1]))
            elif len([part for part in self.item[0] if part in " ".join(self.filtered)]) > 0:
                self.answer.append(random.choice(self.item[1]))
        if len(self.answer) < 1:
            print(self.filtered)
        else:
            print(" ".join(self.answer))

Model()
