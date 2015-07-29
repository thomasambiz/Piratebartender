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

def ask():
    like_strong = False
    like_salty = False
    like_bitter = False
    like_sweet = False
    like_fruity = False
    
    print"Arrrr! I be yer personal pirate bartender.  Ye have ta pick yer poison.  Answer yes or no to these questions"
    
    strong_input = raw_input(questions['strong'])
    strong_input
    if strong_input == "yes":
        like_strong = True
    salty_input = raw_input(questions['salty'])
    salty_input
    if salty_input == "yes":
        like_salty = True
    bitter_input = raw_input(questions['bitter'])
    bitter_input
    if bitter_input == "yes":
        like_bitter = True
    sweet_input = raw_input(questions['sweet'])
    sweet_input
    if sweet_input == "yes":
        like_sweet = True
    fruity_input = raw_input(questions['fruity'])
    fruity_input
    if fruity_input == "yes":
        like_fruity = True
        
    mix_li = [] 
    
    if like_strong == True:
        mix_li.append(random.choice(ingredients['strong']))
    if like_strong == False:
        mix_li.append(random.choice(ingredients['weak']))
    if like_salty == True:
        mix_li.append(random.choice(ingredients['salty']))
    if like_bitter == True:
        mix_li.append(random.choice(ingredients['bitter']))
    if like_sweet == True:
        mix_li.append(random.choice(ingredients['sweet']))
    if like_fruity == True:
        mix_li.append(random.choice(ingredients['fruity']))
    print "You'll love this, it has"
    print(", ".join(mix_li))

ask()

if __name__ == '__main__':
    ask()