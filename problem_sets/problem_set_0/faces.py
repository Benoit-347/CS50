def convert(user_input):
    result = user_input.replace(":)", "🙂")      # Returns a replaced string with ":)" to "🙂"
    result = result.replace(":(", "🙁")
    return result

def main():
    user_input = input()
    emoji_string = convert(user_input)     # Fn call
    print(emoji_string)

main()
