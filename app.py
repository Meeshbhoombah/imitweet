# -*- encoding: utf-8 -*-
from flask import Flask
from random import randrange
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Homapage'

@app.route('/random/word')
def random_word():
    with open('ganja.txt', 'r') as f:
        words = f.read()

    words = words.split()
    random_word_index = randrange(0, len(words))
    random_word = words[random_word_index]
    print(random_word)
    
    return random_word

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

