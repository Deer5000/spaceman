from random import choice

compliment = ['coolio', 'smashing', 'neato', 'fantabulous']
    def get_compliments():
        compliment = choice(compliment)
        return f'Hello there, user! You are so {compliment}!'
