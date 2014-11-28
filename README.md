The basic requirements

Create questions and ingredient dictionaries
The bartender should ask questions that determine your tastes and then identify ingredients to suit those tastes. 

Write a function to ask what style of drink a customer likes
The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary. The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean value. If the customer answers y or yes to the question then the value should be True, otherwise the value should be False. The function should return the new dictionary.

Remember that you can use the raw_input function to get an answer from the customer. If you can't remember how this works then take a look back over assignment five in lesson four.

Write a function to construct a drink
The function should take the preferences dictionary created in the first function as a parameter. Inside the function you should create an empty list to represent the drink. For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the random.choice function. This selects a random item from a list.

Provide a main function
Use if __name__ == '__main__': to run this function from the command line. The main function should call your two functions in order, passing your list of preferences to the drink creation function. It should then print out the contents of the drink.



Extra challenges

If you found completing the basic requirements fairly straightforward then you should try to extend your app to add the following features:

Give the cocktails a name
All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog").

Keep 'em coming
At the moment you can only get one drink at a time from the bartender. A well trained pirate bartender should offer his customer another drink when they've finished their previous one. Try adding a loop in the main function which will ask the customer whether they want another drink, and keep creating new recipes as long as they agree.



Extension exercises

If the extra challenges were not a problem and you're running ahead of schedule then you could try to implement one or two of the following features in your app:

Multiple customers: The bartender could ask for the customer's name before they are served. They could then remember the customer's preferences for when the same customer asks for another drink.
Stock control: Even pirate bars don't have a limitless supply of ingredients. You could add a stock count for each ingredient which decreases whenever the bartender makes a drink. The bartender could restock the ingredients when supplies are low.