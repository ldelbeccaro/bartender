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

answers = {}

def preferences():
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
  drinkname = str(random.choice(adjectives)) + " " + str(random.choice(nouns))
  return drinkname

def drink(dictionary):
  contents = []
  for i in dictionary:
    if dictionary[i] == True:
      ingredient = random.choice(ingredients[i])
      contents.append(ingredient)
  return contents

if __name__ == '__main__':
  preferences()
  while True:
    print 'Ah, the', name()
    print drink(answers)
    cont = raw_input('Would you like another drink?')
    if not(cont == 'y' or cont == 'yes'):
      break