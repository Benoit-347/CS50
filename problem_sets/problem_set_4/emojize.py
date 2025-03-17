import emoji    # need to install
Input = input("Input: ")
text_with_emoji = emoji.emojize(Input, language='alias')    #converts text with alias to emoji

print(text_with_emoji)
