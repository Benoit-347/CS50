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
        The program then searches the results of food search, for a food that mathes this criteria. If None completely mathces, the first, most matched, food result is provided."""

list_1 = string_1.split()

list_2 = [i for i in list_1 if len(i) > 2]
print(f"\nThe number of words in pasted text is: {len(list_2)}\n")
string_2 = ' '.join(list_2)
print(string_2)