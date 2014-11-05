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

def style():
  answers = {}
  for question in questions:
    answer = raw_input(questions[question])
    if answer == 'y' or answer == 'yes':
      answers[question] = True
    else:
      answers[question] = False
  return answers

def drink(dictionary):
  contents = []
  for preference in dictionary:
    if dictionary[value] == True:
      ingredient = random.choice(ingredients[preference])
    contents.append(ingredient)