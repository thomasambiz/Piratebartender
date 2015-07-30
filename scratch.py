
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["a glug of tequilla", "a slug of whisky", "a splash of gin"],
    "salty": ["an olive on a stick", "a salt-dusted rim", "a rasher of bacon"],
    "bitter": ["a shake of bitters", "a splash of tonic", "a twist of lemon peel"],
    "sweet": ["a sugar cube", "a spoonful of honey", "a spash of cola"],
    "fruity": ["a slice of orange", "a dash of cassis", "a cherry on top"]
}

like = {'strong': False, 'salty': False, 'bitter': False, 'sweet': False, 'fruity': False}

def ask():
    print "I be a pirate what can make a smashin drink.  Just lem'me know what ye be likin'.  I'm as daft me peg leg, so please keep yer answers simple... like 'yes' or 'no'"
    for key in questions:
        ans = raw_input(questions[key])
        if ans == "yes":
            like[key] = True

def answer():   
    mix_li = []
    for key in like:
        if like[key] == True:
            mix_li.append(random.choice(ingredients[key]))
    
            
    print "\n Yer gonna love this, it has:\n"
    print(", ".join(mix_li))
    
# ask()
# answer()

if __name__ == '__main__':
    ask()
    answer()