string_1 = """This is a project to help users obtain nutritional info about any common food.
The project makes use of a easy to develop ui 'streamlit' To give a ease of use interface to interact with the python program.
The program starts by asking the user 2 food names.
It then fetches nutritional info on these foods. (Using a API request to 'usda' which is a reputed food information source providing a 1000calls/hr free api package to signed up users)
    The users also have an option to select which nutrients are to be displayed.
Finally a bar graph is displayed to the user, comparing the nutrients of the 2 foods; Displaying all selected nutrients.

Additional features:
    The program also automatically manages a local json file, used to store food search results. This drastically reduces search times from ~2s to ~.2s and also 1 less api call usage.
        It only handles handles the file- i.e. opening/creating it and proving a way to save ur progress. You can make use of it by simply pressing the save button; saving all food searches done in your entire session.

    The users can apply a certian minimum value of a nutrient.
        The program then searches the results of food search, for a food that mathes this criteria. If None completely mathces, the first, most matched, food result is provided.

Design decisions-
Starting with the project theme, i picked food nutrition as my project as i wanted to create a project that would be useful to me personally, not just for educational purpose.
    Obtaining any food's nutrient info, and being able to customize its features by your liking is a big player of creation of this project.
Started out with finding a source for food nutrients. Found usda and learnt of how it use and set up its api from usda's documentation.
    This api provides 1000 api calls /hr limit for free; which is plenty for a personal project. You only need to setup a usda account (or loging with google account) and you can obtain a free api key.
Now i could access nutrients of majority of foods and display each nutrient's value. But this proved difficult to obtain appealing display of a food's nutients.
    I choose to use matplotlib to showcase bargraphs to depict the nutrients.

Another challenge was that all user interaction with the program was being done through terminal, which does not provide a easy way to present features like say the user selecting nutrients from a given list, to display.
And for convience of not using multiple nested if conditions and complex while loops, a decision was made to switch to using a ui instead of providing input throught the terminal.
Streamlit was chosen to develop the ui; as it is very easy to implement and handles most of the work for you, while proving a simple and neat ui.

The UI was developed after multiple searches on syntaxes of using streamlit, and after a lot of trial and error, the ui was designed with two food names to input, a list of nutrients to select to diaplay at bar graph.
Small note: some food searches yeilded None type for a particular nutrient. A condition was implemented to change a None type value to 0. As an int val is required for ,matplotlib to plot successfully
The progarm worked well, every food search yeiled nutrient bar graphs as intended. But there was a minor wait between each food search, which the program took to send and recive an api request.
Then i took advantage of a concept i leant in one of my college courses called "memoization". Where each searched result is stored. So any subsequent seaches yields the stored up result direcly. 
Using this concept along reading and writing to a json file (from file handling lecture);
    I setup the program such that any food search if yields non empty result, stores entire result to a json file, with the food search as the key. Every time the program starts, it loads the food searches and result from this json file as a dictionary. If the user searches a food and it exactly matches the food seach in the dict, it returns this result instead.
    Now we may face a challenge- too frequent writes: Each time the user searches a new food, it will write to json file, . Which is not optimal (as this causes frequent writing to a json file including a significant time to write).
    A interesting way to solve this would be to maybe write only a part of the dict, that is new, to the json file. But this would be too complex for our scope.
    On some self though, i decided i will let the saving part be left to the user's descretion.
    Hence i added a button called 'save' at the end of the UI of the program. Which is pressed, triggers a write operation to the json file on all the food searches done until now. (The program will maintain a dict which loads the existing data in json and, every new food search would insert the search and its results; Finally, this would be written on pressing 'save' button).

    Later for ease of comparision; seperate graphs were made for viewing desired and un-desired nutrients. With a toggle, optionally displaying the graph of un-desired nutrients."""
list_1 = string_1.split()

list_2 = [i for i in list_1 if len(i) > 2]
print(f"\nThe number of words in pasted text is: {len(list_2)}\n")
string_2 = ' '.join(list_2)
print(string_2)