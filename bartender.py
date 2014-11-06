# Pirate Bartender Project
import random

questions = {
    'strong': 'Do ye like yer drinks strong?',
    'salty': 'Do ye like it with a satly tang?',
    'bitter': 'Are ye a lubber who likes it bitter?',
    'sweet': 'Would ye like a bit of sweetness with yer poison?',
    'fruity': 'Are ye one for a fruity finish?'
}

ingredients = {
    'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],
    'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],
    'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],
    'sweet': ['sugar cube', 'spoonful of honey', 'splash of cola'],
    'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']
}

# key -> value
# ingredient -> amount
stock = {}

def stock_all():
    for taste in ingredients.values():
        for ingred in taste:
            stock[ingred] = 10

def preferences():
    answers = {}
    for question in questions:
        answer = raw_input(questions[question])
        if answer == 'y' or answer == 'yes':
            answers[question] = True
        else:
            answers[question] = False
    return answers

def name():
    adjectives = ['Salty', 'Fluffy', 'Sappy', 'Crispy', 'Groggy']
    nouns = ['Seahorse', 'Log', 'Giraffe']
    drinkname = str(random.choice(adjectives)) + ' ' + str(random.choice(nouns))
    return drinkname

def drink(dictionary):
    contents = []
    for i in dictionary:
        if dictionary[i] == True:
            ingredient = random.choice(ingredients[i])
            if not stock[ingredient] == 0:
                contents.append(ingredient)
                stock[ingredient] -= 1
            if stock[ingredient] < 3:
                restock = raw_input(ingredient, 'low! Do you want to restock?')
                if restock == 'y' or restock == 'yes':
                    stock[ingredient] = 10
    return contents

customers = {} 

if __name__ == '__main__':
    customer = raw_input('What is your name?')
    if customer in customers:
        answers = customers[customer]
    else:
        customers[customer] = preferences()
    while True:
        print 'Ah, the', name()
        print drink(answers)
        cont = raw_input('Would you like another drink?')
        if not(cont == 'y' or cont == 'yes'):
            break