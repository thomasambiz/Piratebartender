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
    "weak": ["a finger of rum", "a shot of liqueur", "a squirt of schnapps"], 
    "salty": ["a olive on a stick", "a salt-dusted rim", "a rasher of bacon"],
    "bitter": ["a shake of bitters", "a splash of tonic", "a twist of lemon peel"],
    "sweet": ["a sugar cube", "a spoonful of honey", "a spash of cola"],
    "fruity": ["a slice of orange", "a dash of cassis", "a cherry on top"]
}

like = {'strong': False, 'weak': False, 'salty': False, 'bitter': False, 'sweet': False, 'fruity': False}

def ask():
    print "I be a pirate what can make a smashin drink.  Just lem'me know what ye be likin'.  I'm as daft me peg leg, so please keep yer answers simple... like 'yes' or 'no'"
    raw_input(questions['strong'])
    if raw_input == "yes":
        like['strong'] = True
    elif raw_input == "no":
        like['weak'] = True
    raw_input(questions['salty'])
    if raw_input == "yes":
        like['salty'] = True
    raw_input(questions['bitter'])
    if raw_input == "yes":
        like['bitter'] = True
    raw_input(questions['sweet'])
    if raw_input == "yes":
        like['sweet'] = True
    raw_input(questions['fruity'])
    if raw_input == "yes":
        like['fruity'] = True
 
def answer():
    mix_li = []
    if like['strong'] == True:
        mix_li.append(random.choice(ingredients['strong']))
    if like['strong'] == False:
        mix_li.append(random.choice(ingredients['weak']))
    if like['salty'] == True:
        mix_li.append(random.choice(ingredients['salty']))
    if like['bitter'] == True:
        mix_li.append(random.choice(ingredients['bitter']))
    if like['sweet'] == True:
        mix_li.append(random.choice(ingredients['sweet']))
    if like['fruity'] == True:
        mix_li.append(random.choice(ingredients['fruity']))
        
    print "yer gonna love this, it has"
    print(", ".join(mix_li))
    
ask()
answer()
